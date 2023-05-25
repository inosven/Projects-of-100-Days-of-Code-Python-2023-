import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)
window.columnconfigure(index=0, weight=1)
window.columnconfigure(index=1, weight=1)
window.columnconfigure(index=2, weight=1)
window.rowconfigure(index=0, weight=2)
window.rowconfigure(index=1, weight=1)
window.rowconfigure(index=2, weight=2)

label1 = tkinter.Label(text="is equal to", font=("Arial", 16))
label1.grid(row=1, column=0, stick="e")
label2 = tkinter.Label(text="0", font=("Arial", 16))
label2.grid(row=1, column=1)
label3 = tkinter.Label(text="km", font=("Arial", 16))
label3.grid(row=1, column=2, sticky="w")
label4 = tkinter.Label(text="Miles", font=("Arial", 16))
label4.grid(row=0, column=2, sticky="sw")

user_input = tkinter.Entry(width=10)
user_input.grid(row=0, column=1, sticky="s")


def convert_mile_to_km():
    ratio = 1.609344
    value_in_mile = float(user_input.get())
    value_in_km = round(value_in_mile * ratio, 2)
    return value_in_km


def update_label_2():
    label2.config(text=f"{convert_mile_to_km()}")


button = tkinter.Button(text="Calculate", command=update_label_2, font=("Arial", 16))
button.grid(row=2, column=1, sticky="n")
window.mainloop()
