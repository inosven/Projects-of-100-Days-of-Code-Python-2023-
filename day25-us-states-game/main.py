import turtle
import pandas as pd
from pen import Pen

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
pen = Pen()

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
guessed_states = []

df = pd.read_csv("50_states.csv")
while guessed_states != len(df):
    answer_states = screen.textinput(title=f"Guess the State: {len(guessed_states)}/{len(df)}",
                                     prompt="What's another state's name?")
    if answer_states == "exit":
        break
    current_row = df[df.state.str.lower().isin([answer_states.lower()])]
    if not current_row.empty:
        pen.draw_at_location(current_row.state.item(), int(current_row.x.iloc[0]), int(current_row.y.iloc[0]))
        guessed_states.append(answer_states.title())

to_learn = df[~df.state.isin(guessed_states)]
to_learn.state.to_csv("states_to_learn.csv")
# screen.exitonclick()
