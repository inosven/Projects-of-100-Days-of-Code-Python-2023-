import tkinter

window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=50,pady=50)
# Label

my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))

# my_label.pack(side="top")
my_label.grid(row=0, column=0)

# my_label["text"] = "New Text1"
my_label.config(text="New text2")
my_label.config(padx=100, pady=100)

# Button
def button_clicked():
    my_label.config(text="I got clicked!")
def click_button():
    my_label.config(text=input.get())

button = tkinter.Button(text="Click me!",command=click_button)
button.grid(row=1,column=1)

new_button = tkinter.Button(text="Help me!")
new_button.grid(row=0, column=2)
# Entry

input = tkinter.Entry(width=10)
input.grid(row=2, column=3)

# print(input.get())
window.mainloop()