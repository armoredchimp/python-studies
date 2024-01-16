import tkinter as tk
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

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    count_down(300)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

window.after(1000, )

canvas = tk.Canvas(width=250, height=250, bg=YELLOW, highlightthickness=0)
tomato = tk.PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato)
timer = tk.Label(text='Timer', font=(FONT_NAME, 40), fg=GREEN, bg=YELLOW)
timer.grid(column=1, row=1)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white',
                                font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=2)

start = tk.Button(text='Start', command=start_timer, font=(FONT_NAME, 10))
start.grid(column=0, row=3)
reset = tk.Button(text='Reset', font=(FONT_NAME, 10))
reset.grid(column=0, row=4, padx=30, pady=50)
check = tk.Label(text='✓', font=(FONT_NAME, 20, 'bold'), fg=GREEN, bg=YELLOW)
check.grid(column=1, row=4)

window.mainloop()


# lab = tkinter.Label(text='is equal to', font=('Arial', 12, 'normal'))
# lab.grid(column=0, row=1)
