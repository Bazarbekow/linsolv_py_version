import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QPushButton, QSpinBox, QFrame, QLineEdit, QMessageBox
from PyQt5.QtCore import QEvent
from PyQt5.QtGui import QIcon
import numpy as np

class LinearEquationSolver(QMainWindow):

    def __init__(self):
        super().__init__()

        self.m_size = 2
        self.n_size = 2
        self.entries = []
        self.b_entries = []

        self.setWindowTitle("Linear Equation Solver")
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.grid_layout = QGridLayout(self.central_widget)

        self.m_size_spinbox = QSpinBox()
        self.m_size_spinbox.setRange(2, 5)
        self.grid_layout.addWidget(self.m_size_spinbox, 1, self.n_size + 4)
        self.n_size_spinbox = QSpinBox()
        self.n_size_spinbox.setRange(2, 5)
        self.grid_layout.addWidget(self.n_size_spinbox, 1, self.n_size + 5)

        result_label = QLabel("")
        self.grid_layout.addWidget(result_label,6,6)

        self.m_size_label = QLabel("Rows of A matrix:")
        self.grid_layout.addWidget(self.m_size_label, 0, self.n_size + 4)

        self.n_size_label = QLabel("Columns of A matrix:")
        self.grid_layout.addWidget(self.n_size_label, 0, self.n_size + 5)

        self.create_entries(self.m_size, self.n_size)
        
        solve_button = QPushButton("Solve")
        solve_button.clicked.connect(self.on_solve)
        self.grid_layout.addWidget(solve_button, self.m_size, self.n_size + 4)

        create_entries_button = QPushButton("Create Entries")
        create_entries_button.clicked.connect(lambda: self.create_entries(self.m_size_spinbox.value(), self.n_size_spinbox.value()))
        self.grid_layout.addWidget(create_entries_button, self.m_size + 1, self.n_size + 4)

        label1 = QLabel("Matrix A")
        self.grid_layout.addWidget(label1, 0, 0, 1, self.n_size)

        label2 = QLabel("Vector b")
        self.grid_layout.addWidget(label2, 0, self.n_size)

        self.setStyleSheet("""
            QMainWindow {
                background-color: #FFFFFF;
            }

            QLineEdit {
                background-color: #FFFFFF;
                border: 1px solid #DDDDDD;
                padding: 6px;
                font-size: 14px;
                color: #333333;
            }

            QLabel {
                font-size: 14px;
                color: #333333;
            }

            QPushButton {
                background-color: #F3A712;
                border: none;
                color: #FFFFFF;
                padding: 8px 16px;
                font-size: 14px;
            }

            QPushButton:hover {
                background-color: #F3D39C;
            }
        """)
    def create_entries(self, m_size, n_size):
        matrix_frame = self.central_widget.findChild(QFrame)
        k = self.m_size - m_size
        print("k = " + str(k))
        if m_size < self.m_size:
            for i in range(m_size, self.m_size):
                for j in range(self.n_size):
                    print("i: " + str(i) + " j: " + str(j) + "\n")
                    entry = self.entries[i][j]
                    self.grid_layout.removeWidget(entry)
                    entry.deleteLater()
                self.entries.pop()
                entry = self.b_entries[i]
                self.grid_layout.removeWidget(entry)
                entry.deleteLater()
                self.b_entries.pop()

        if n_size < self.n_size:
            for i in range(m_size):
                for j in range(n_size, self.n_size):
                    print("i2: " + str(i) + " j2: " + str(j) + "\n")
                    entry = self.entries[i][j]
                    self.grid_layout.removeWidget(entry)
                    entry.deleteLater()
                    self.entries[i].pop()

        for i in range(m_size):
            while len(self.entries) <= i:
                self.entries.append([])
            for j in range(n_size):
                while len(self.entries[i]) <= j:
                    entry = QLineEdit("0")
                    entry.installEventFilter(self)
                    self.entries[i].append(entry)
                entry = self.entries[i][j]
                self.grid_layout.addWidget(entry, i+1, j)

        for i in range(m_size):
            while len(self.b_entries) <= i:
                entry = QLineEdit("0")
                entry.installEventFilter(self)
                self.b_entries.append(entry)
            entry = self.b_entries[i]
            self.grid_layout.addWidget(entry, i+1, n_size)

        self.m_size = m_size
        self.n_size = n_size
            
    def clear_zero(self):
        sender = self.sender()
        if sender.text() == "0":
            sender.clear()
            
    def eventFilter(self, source, event):
        if event.type() == QEvent.MouseButtonPress and isinstance(source, QLineEdit):
            if source.text() == "0":
                source.clear()
        return super().eventFilter(source, event)
    
    def solve_linsys(self, A, b):
        try:
            x = np.linalg.solve(A, b)
            print("Solution: ", x)
            return x
        except:
             QMessageBox.critical(self, "Error", "Input is invalid. Please enter the correct matrix and vector.")

    def on_solve(self):
        try:
            m_size = self.m_size
            n_size = self.n_size
            A = [[float(self.entries[i][j].text()) for j in range(n_size)] for i in range(m_size)]
            b = [float(self.b_entries[i].text()) for i in range(m_size)]
            x = self.solve_linsys(A, b)
            result_label = self.central_widget.findChild(QLabel, "")
            result_label.setText("Solution set: " + str(x))
        except ValueError:
            QMessageBox.critical(self, "Error", "Input is invalid. Please enter the correct matrix and vector.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('icon.ico'))
    linear_equation_solver = LinearEquationSolver()
    linear_equation_solver.show()
    sys.exit(app.exec_())