from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
ORANGE = "#ffc85c"
RED = "#c05555"
GREEN = "#59886b"
YELLOW = "#fff8c1"
FONT_NAME = "Courier"
WORK_MIN = 0.25
SHORT_BREAK_MIN = 0.5
LONG_BREAK_MIN = 1
BG_IMG = "tomato.png"
CHECKMARK = " ✓ "
reps = 0
num_checks = 0


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text=f"00:00")





# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps, num_checks
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60


    if reps == 8:
        count_down(long_break_sec)
        num_checks = 0
        title_label.config(text="BREAK", fg=RED)

    elif reps % 2 == 0:
        num_checks += 1
        count_down(short_break_sec)
        title_label.config(text="BREAK", fg=RED)
        check_marks.config(text=CHECKMARK * num_checks)

    else:

        count_down(work_sec)
        title_label.config(text="WORK", fg=ORANGE)
    #if re
    # while reps < 5:
    #     if reps < 3:
    #         title_label.config(text="WORK", fg=ORANGE)
    #         count_down(work_sec)
    #         title_label.config(text = "BREAK", fg = RED)
    #         count_down(short_break_sec)
    #         reps += 1
    #     if reps == 4:
    #         title_label.config(text="WORK", fg=ORANGE)
    #         count_down(work_sec)
    #         title_label.config(text = "BREAK", fg = ORANGE)
    #         reps = 0








# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000,count_down,count-1)
    else:
        start_timer()



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg = YELLOW)

canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)
bg_img = PhotoImage(file = BG_IMG)
canvas.create_image(100,112, image = bg_img)
timer_text = canvas.create_text(100,130,text = "00:00", fill = "white", font = (FONT_NAME,35,"bold"))
canvas.grid(column = 2, row = 2)

title_label = Label(text="Timer", font = (FONT_NAME, 50, "normal"), fg = GREEN, bg = YELLOW)
title_label.grid(column = 2, row = 1)

check_marks = Label(text =CHECKMARK*num_checks, fg = GREEN, bg = YELLOW, font = (FONT_NAME, 24, "normal"))
check_marks.grid(column = 2, row = 4)

start_button = Button(text = "Start", bg = "white", command = start_timer)
start_button.grid(column = 1, row = 3)

reset_button = Button(text = "Reset", bg = "white", command = reset_timer)
reset_button.grid(column = 3, row = 3)


window.mainloop()