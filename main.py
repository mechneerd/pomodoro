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
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset():
    window.after_cancel(timer)
    title_label.config(text='TIMER')
    canvas.itemconfig(count_text, text='00:00')
    check_marks.config(text='')

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_time():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps == 1 or 3 or 5 or 7:
        title_label.config(text='WORK', fg=GREEN)
        count(work_sec)
    elif reps == 2 or 4 or 6:
        title_label.config(text='BREAK', fg=PINK)
        count(short_break)
    elif reps == 8:
        title_label.config(text='BREAK', fg=RED)
        count(long_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count(c):
    minute_count = math.floor(c/60)
    second_count = c % 60
    if second_count < 10:
        second_count = f'0{second_count}'
    canvas.itemconfig(count_text, text=f'{minute_count}:{second_count}')
    if c > 0:
        global timer
        timer = window.after(1000, count, c-1)
    else:
        start_time()
        tick = ''
        for i in range(math.floor(reps/2)):
            tick += '✔'
        check_marks.config(text=tick)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('pomodoro')
window.config(width=200, height=224)
window.config(padx=100, pady=50, bg=YELLOW)


title_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50,))
title_label.grid(column=1, row=0)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato)
count_text = canvas.create_text(103, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)


start_button = Button(text='Start', command=start_time, bg=YELLOW, font=(FONT_NAME, 20), highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', command=reset, bg=YELLOW, font=(FONT_NAME, 20), highlightthickness=0)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
