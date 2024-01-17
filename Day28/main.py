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
reps = 0
t = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    window.after_cancel(t)
    canvas.itemconfig(timer_text, text='00:00')
    top_text.config(text='Timer')
    check.config(text='')
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        top_text.config(text='LONG BREAK', fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        top_text.config(text='QUICK BREAK', fg=PINK)
    else:
        count_down(work_sec)
        top_text.config(text='GET TO WORK!', fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global t
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        t = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            cur = check.cget('text')
            check.config(text=cur + '✓')


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

window.after(1000, )

canvas = tk.Canvas(width=400, height=250, bg=YELLOW, highlightthickness=0)
tomato = tk.PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato)
top_text = tk.Label(text='Timer', font=(
    FONT_NAME, 40, 'bold'), fg=GREEN, bg=YELLOW)
top_text.grid(column=1, row=1)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white',
                                font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=2)

start = tk.Button(text='Start', command=start_timer, font=(FONT_NAME, 10))
start.grid(column=0, row=3)
reset = tk.Button(text='Reset', font=(FONT_NAME, 10), command=reset_timer)
reset.grid(column=0, row=4, padx=30, pady=50)
check = tk.Label(text='', font=(FONT_NAME, 20, 'bold'), fg=GREEN, bg=YELLOW)
check.grid(column=1, row=4)

window.mainloop()


# lab = tkinter.Label(text='is equal to', font=('Arial', 12, 'normal'))
# lab.grid(column=0, row=1)
# labool.config(text=input_text.get())
# text='✓'
