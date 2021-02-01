from tkinter import *
import pandas
import random as rand

BACKGROUND_COLOR = "#B1DDC6"
FRONT_CARD_IMG = "images/card_front.png"
BACK_CARD_IMG = "images/card_back.png"
RIGHT_IMG = "images/right.png"
WRONG_IMG = "images/wrong.png"
TITLE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

# --------- DATA MANAGEMENT ----------
try:
    df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pandas.read_csv("data/french_words.csv")

words_dict = df.to_dict(orient="records")
current_card = {}


# --------------------- SAVE TO NEW CSV ------------------------------
def correct_card():
    global current_card
    words_dict.remove(current_card)
    new_data = pandas.DataFrame(words_dict)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    new_card()


# --------------------------FLIP CARD-------------------------
def flip_card():
    translation = current_card['English']
    canvas.itemconfig(card_display, image=back_card)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=translation, fill="white")


# ----------------------- NEW FLASH CARD ---------------------


def new_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = rand.choice(words_dict)
    new_word = current_card['French']

    canvas.itemconfig(card_display, image=front_card)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=new_word, fill="black")

    flip_timer = window.after(3000, func=flip_card)


# --------------------- UI BUILD ------------------------------

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card = PhotoImage(file=FRONT_CARD_IMG)
back_card = PhotoImage(file=BACK_CARD_IMG)
card_display = canvas.create_image(400, 263, image=front_card)
title_text = canvas.create_text(400, 150, text="Title", font=TITLE_FONT)
word_text = canvas.create_text(400, 263, text="Word", font=WORD_FONT)
canvas.grid(column=1, row=1, columnspan=2)

# Labels

# Right button
right_image = PhotoImage(file=RIGHT_IMG)
right_button = Button(image=right_image, highlightthickness=0, borderwidth=0, command=correct_card)
right_button.grid(column=2, row=2)

# Wrong button
wrong_image = PhotoImage(file=WRONG_IMG)
wrong_button = Button(image=wrong_image, highlightthickness=0, borderwidth=0, command=new_card)
wrong_button.grid(column=1, row=2)

new_card()

window.mainloop()
