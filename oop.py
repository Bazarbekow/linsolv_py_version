import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QPushButton, QSpinBox, QFrame, QLineEdit, QMessageBox
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
        self.grid_layout.addWidget(result_label,self.m_size + 3,self.n_size)

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
        self.grid_layout.addWidget(create_entries_button, self.m_size + 2, self.n_size + 4)

        label1 = QLabel("Matrix A")
        self.grid_layout.addWidget(label1, 0, 0, 1, self.n_size)

        label2 = QLabel("Vector b")
        self.grid_layout.addWidget(label2, 0, self.n_size)

    def create_entries(self, m_size, n_size):
        self.entries.clear()
        self.b_entries.clear()

        matrix_frame = QFrame()
        matrix_frame.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        self.grid_layout.addWidget(matrix_frame, 1, 0, m_size, n_size)

        for i in range(m_size):
            self.entries.append([])
            for j in range(n_size):
                entry = QLineEdit("0")
                entry.textChanged.connect(self.clear_zero)
                self.grid_layout.addWidget(entry, i + 1, j)
                self.entries[i].append(entry)
            entry = QLineEdit("0")
            entry.textChanged.connect(self.clear_zero)
            self.grid_layout.addWidget(entry, i + 1, n_size)
            self.b_entries.append(entry)
            
    def clear_zero(text):
        if text == "0":
            sender = QApplication.focusWidget()
            sender.setText("")

    def solve_linsys(self, A, b):
        try:
            x = np.linalg.solve(A, b)
            print("Solution: ", x)
            return x
        except:
             QMessageBox.critical(self, "Error", "Input is invalid. Please enter the correct matrix and vector.")

    def on_solve(self):
        try:
            m_size = self.m_size_spinbox.value()
            n_size = self.n_size_spinbox.value()
            A = [[float(self.entries[i][j].text()) for j in range(n_size)] for i in range(m_size)]
            b = [float(self.b_entries[i].text()) for i in range(m_size)]
            x = self.solve_linsys(A, b)
            result_label = self.central_widget.findChild(QLabel, "")
            result_label.setText(str(x))
        except ValueError:
            QMessageBox.critical(self, "Error", "Input is invalid. Please enter the correct matrix and vector.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    linear_equation_solver = LinearEquationSolver()
    linear_equation_solver.show()
    sys.exit(app.exec_())