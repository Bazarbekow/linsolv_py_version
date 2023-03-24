import tkinter as tk
#from tkinter import Spinbox,Tk,PhotoImage,Label,Frame,Entry,Button
from tkinter import messagebox
import numpy as np
#from numpy import linalg

#Made in more OOP-oriented, see oop.py
root = tk.Tk()
root.title("Linear Equation Solver")
photo = tk.PhotoImage(file = "icon.png")
root.iconphoto(False, photo)

m_size = 2
n_size = 2
m_size_spinbox = tk.Spinbox(root, from_=2, to=5, command = lambda:create_entries(m_size, n_size))
m_size_spinbox.grid(row=1, column=n_size + 4)
m_size = int(m_size_spinbox.get())

n_size_spinbox = tk.Spinbox(root, from_=2, to=5, command = lambda:create_entries(m_size, n_size))
n_size_spinbox.grid(row=1, column=n_size + 5)
n_size = int(n_size_spinbox.get())

m_size_label = tk.Label(root, text="Rows of A matrix:")
m_size_label.grid(row=0, column=n_size + 4)

n_size_label = tk.Label(root, text="Columns of A matrix:")
n_size_label.grid(row=0, column=n_size + 5)

entries = []
b_entries = []

def clear_zero(event): #Untested function
    widget = event.widget
    if widget.get() == "0":
        widget.delete(0, "end")

def create_entries(m_size, n_size): #for matrice A
    entries.clear()
    b_entries.clear()
    matrix_frame = tk.Frame(root)
    matrix_frame.grid(row=1, column=0, columnspan=n_size, rowspan=m_size)
    for i in range(m_size): # Generates m x n entry rows for the matrix A
        entries.append([])
        for j in range(n_size):
            entry = tk.Entry(matrix_frame)
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

matrix_frame = create_entries(m_size, n_size)

def on_size_change():
    pass

def solve_linsys(A, b):
    try:
        x = np.linalg.solve(A, b)
        print("Solution: ", x)
        return x
    except:
        messagebox.showerror("Error", "Input is invalid. Please enter the correct matrix and vector.")

def on_solve():
    try:
        m_size = int(m_size_spinbox.get())
        n_size = int(n_size_spinbox.get())
        A = [[float(entries[i][j].get()) for j in range(n_size)] for i in range(m_size)]
        b = [float(b_entries[i].get()) for i in range(m_size)]
        x = solve_linsys(A, b)
        result_label.config(text=x)
    except ValueError:
        messagebox.showerror("Error", "Input is invalid. Please enter the correct matrix and vector.")

solve_button = tk.Button(root, text="Solve", command=on_solve) #Solve button
solve_button.grid(row=m_size + 3, column=n_size + 2)
create_entries_button = tk.Button(root, text="Create Entries", command = lambda: create_entries(int(m_size_spinbox.get()), int(n_size_spinbox.get()) )) #Creates m x n entries
create_entries_button.grid(row=m_size + 2, column=n_size + 4) #its location in grid
label1 = tk.Label(root, text = "Matrix A")
label1.grid(row=0, column=0, padx=10, pady=10)
result_label = tk.Label(root, text="")
result_label.grid(row=m_size + 4, column=n_size + 3)
label2 = tk.Label(root, text="Vector b")
label2.grid(row=0, column=n_size, padx=10, pady=10)

root.mainloop()