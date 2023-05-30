from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FRENCH_FONT = ["Ariel", 60, "bold"]
ENGLISH_FONT = ["Ariel", 40, "italic"]
try:
    data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("./data/french_words.csv")

# Random word picker
index = 0

def random_word():
    global index, flip_timer
    window.after_cancel(flip_timer)
    index = random.randint(0, len(data) - 1)
    frn = data.French[index]
    canvas.itemconfig(Title, text="French", fill="black")
    canvas.itemconfig(Word, text=frn, fill="black")
    canvas.itemconfig(card_bg, image=front_img)
    flip_timer = window.after(3000, func=flip_card)

def words_to_learn():
    data.drop(index, axis=0, inplace=True)
    data.reset_index(drop=True, inplace=True)
    random_word()

    # print(len(data))
    data.to_csv("./data/words_to_learn.csv", index=False)
def flip_card():
    eng = data.English[index]
    canvas.itemconfig(Title, text="English", fill="white")
    canvas.itemconfig(Word, text=eng, fill="white")
    canvas.itemconfig(card_bg, image=back_img)


window = Tk()
window.title("Flash Card")
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)
canvas = Canvas(width=800, height=526, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
right_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")

card_bg = canvas.create_image(400, 263, image=front_img)

Title = canvas.create_text((400, 150), text="", font=ENGLISH_FONT)
Word = canvas.create_text((400, 263), text="", font=FRENCH_FONT)
wrong_button = Button(image=wrong_img, highlightthickness=0, command=random_word)
right_button = Button(image=right_img, highlightthickness=0, command=words_to_learn)
wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)
flip_timer = window.after(3000, func=flip_card)
random_word()

window.mainloop()
