import tkinter as tk

root = tk.Tk()

# Determine the number of rows and columns in the grid
total_rows = 10
total_columns = 6

# Set the row parameter to half of the total number of rows
middle_row = total_rows // 2

# Set the column parameter to the middle column of the grid
middle_column = total_columns // 2

# Create a label and place it in the middle-top of the grid
label = tk.Label(root, text="Hello, world!")
label.grid(row=middle_row, column=middle_column)

root.mainloop()
