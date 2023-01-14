import tkinter as tk
from tkinter import messagebox
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

def solve_linsys(A, b):
    try:
        x = np.linalg.solve(A, b)
        print("Solution: ", x)
        return x
    except:
        messagebox.showerror("Error", "Input is invalid. Please enter the correct matrix and vector.")

def on_solve():
    try:
        A = [[float(entry_1.get()), float(entry_11.get()), float(entry_111.get())],
             [float(entry_2.get()), float(entry_22.get()), float(entry_222.get())],
             [float(entry_3.get()), float(entry_33.get()), float(entry_333.get())]]
        b = [float(b_entry.get()), float(b_entry1.get()), float(b_entry2.get())]
        x = solve_linsys(A, b)
        result_label.config(text=x)
        if x is not None:
            fig.clear()
            ax = fig.add_subplot(111)
            ax.scatter(x, np.zeros(len(x)), label='Solution')
            ax.legend()
            canvas.draw()
    except:
        messagebox.showerror("Error", "Input is invalid. Please enter the correct matrix and vector.")
root = tk.Tk()
root.title("Linear Equation Solver")

entry_1 = tk.Entry(root)
entry_11 = tk.Entry(root)
entry_111 = tk.Entry(root)
entry_2 = tk.Entry(root)
entry_22 = tk.Entry(root)
entry_222 = tk.Entry(root)
entry_3 = tk.Entry(root)
entry_33 = tk.Entry(root)
entry_333 = tk.Entry(root)

b_entry = tk.Entry(root)
b_entry1 = tk.Entry(root)
b_entry2 = tk.Entry(root)

solve_button = tk.Button(root, text="Solve", command=on_solve)

label1 = tk.Label(root, text = "Matrix A")
label1.grid(row=0, column=0, padx=10, pady=10)
result_label = tk.Label(root, text="")
result_label.grid(row=4, column=3)

entry_1.grid(row=1, column=0)
entry_11.grid(row=1, column=1)
entry_111.grid(row=1, column=2)
entry_2.grid(row=2, column=0)
entry_22.grid(row=2, column=1)
entry_222.grid(row=2, column=2)
entry_3.grid(row=3, column=0)
entry_33.grid(row=3, column=1)
entry_333.grid(row=3, column=2)

label2 = tk.Label(root, text="Vector b")
label2.grid(row=0, column=3, padx=10, pady=10)

b_entry.grid(row=1, column=3)
b_entry1.grid(row=2, column=3)
b_entry2.grid(row=3, column=3)

solve_button.grid(row=4, column=2)

fig = Figure(figsize=(5, 4), dpi=100)
canvas = FigureCanvasTkAgg(fig, root)
fig = Figure(figsize=(5, 4), dpi=100)
canvas = FigureCanvasTkAgg(fig, root)
canvas.get_tk_widget().grid(row=5, column=0, columnspan=4, padx=10, pady=10)

root.mainloop()