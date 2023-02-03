import tkinter as tk
from tkinter import messagebox
import numpy as np

class LinearEquationSolver:
    def __init__(self, root, m_size=2, n_size=2):
        self.root = root
        self.root.title("Linear Equation Solver")
        
        self.m_size = m_size
        self.n_size = n_size
        self.entries = []
        self.b_entries = []
        
        self.m_size_spinbox = tk.Spinbox(self.root, from_=2, to=5, command = self.create_entries)
        self.m_size_spinbox.grid(row=1, column=self.n_size + 4)
        self.m_size = int(self.m_size_spinbox.get())

        self.n_size_spinbox = tk.Spinbox(self.root, from_=2, to=5, command = self.create_entries)
        self.n_size_spinbox.grid(row=1, column=self.n_size + 5)
        self.n_size = int(self.n_size_spinbox.get())

        self.m_size_label = tk.Label(self.root, text="Rows of A matrix:")
        self.m_size_label.grid(row=0, column=self.n_size + 4)

        self.n_size_label = tk.Label(self.root, text="Columns of A matrix:")
        self.n_size_label.grid(row=0, column=self.n_size + 5)

        self.matrix_frame = self.create_entries()

        self.solve_button = tk.Button(self.root, text="Solve", command=self.on_solve)
        self.solve_button.grid(row=self.m_size + 3, column=self.n_size + 2)
        self.create_entries_button = tk.Button(self.root, text="Create Entries", command = self.create_entries)
        self.create_entries_button.grid(row=self.m_size + 2, column=self.n_size + 4)
        self.result_label = tk.Label(self.root, text="")
        self.result_label.grid(row=self.m_size + 4, column=self.n_size + 2)
    
    def clear_zero(self, event):
        widget = event.widget
        if widget.get() == "0":
            widget.delete(0, "end")
    
    def create_entries(self):
        self.entries.clear()
        self.b_entries.clear()
        self.matrix_frame = tk.Frame(self.root)
        self.matrix_frame.grid(row=1, column=0, columnspan=self.n_size, rowspan=self.m_size)
        for i in range(self.m_size): # Generates m x n entry rows for the matrix A
            entries.append([])
            for j in range(self.n_size):
                entry = tk.Entry(self.matrix_frame)
                entry.grid(row=i, column=j)
                entry.bind("<FocusIn>", clear_zero) # Theoretically, when field is selected, zero is deleted
                if entry.get() == "":
                    entry.insert(0, "0")
                    entries[i].append(entry)
                else: 
                    entries[i].append(entry)
        for i in range(m_size): #Generates m x 1 entry rows for vector b
            entry = tk.Entry(root)
            entry.grid(row=i+1, column=m_size)
            entry.bind("<FocusIn>", clear_zero)
            if entry.get() == "":
                entry.insert(0, "0")
                b_entries.append(entry)
            else: 
                b_entries.append(entry)
        #print(len(entries))
        return matrix_frame

class App(tk.Tk):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    app = LinearEquationSolver()
    app.mainloop()