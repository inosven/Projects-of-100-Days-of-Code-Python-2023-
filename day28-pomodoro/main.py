from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
my_timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(my_timer)
    global reps
    reps = 1
    timer.config(text="Pomo")
    canvas.itemconfig(time_countdown, text="00:00")
    check_marks.config(text="")
    start_button.config(state="normal")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    start_button.config(state="disabled")
    if reps % 2 ==1:
        count_down(WORK_MIN * 60)
        timer.config(text="Work", fg=GREEN)
    elif reps == 8:
        count_down(LONG_BREAK_MIN * 60)
        timer.config(text="Break", fg=RED)
    else:
        count_down(SHORT_BREAK_MIN * 60)
        timer.config(text="Break", fg=PINK)
    reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global my_timer
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(time_countdown, text=f"{count_min}:{count_sec}")
    if count > 0:
        my_timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            marks += "✔ "
            check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
time_countdown = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer = Label(text="Pomo", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
timer.grid(row=0, column=1)

check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 16, "bold"))
check_marks.grid(row=3, column=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()
