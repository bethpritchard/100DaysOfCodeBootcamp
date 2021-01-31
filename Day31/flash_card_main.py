from tkinter import *
from tkinter import messagebox
import pandas
import random as rand

BACKGROUND_COLOR = "#B1DDC6"
FRONT_CARD_IMG = "images/card_front.png"
BACK_CARD_IMG = "images/card_back.png"
RIGHT_IMG = "images/right.png"
WRONG_IMG = "images/wrong.png"
TITLE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")


df = pandas.read_csv("data/french_words.csv")
words_dict = df.to_dict(orient="records")
current_card ={}

# ---------------------------------------------------


# --------------------------FLIP CARD-------------------------
def flip_card():
    translation = current_card['English']
    canvas.itemconfig(current_card, image=back_card)
    canvas.itemconfig(title_text, text="English")
    canvas.itemconfig(word_text,text =translation )

# ----------------------- NEW FLASH CARD ---------------------



def new_card():
    global current_card
    current_card = rand.choice(words_dict)
    new_word = current_card['French']


    canvas.itemconfig(current_card,image=front_card)
    canvas.itemconfig(title_text, text="French")
    canvas.itemconfig(word_text, text=new_word)






# --------------------- UI BUILD ------------------------------

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card = PhotoImage(file=FRONT_CARD_IMG)
back_card = PhotoImage(file=BACK_CARD_IMG)
current_card = canvas.create_image(400, 263, image=front_card)
title_text = canvas.create_text(400, 150, text="Title", font=TITLE_FONT)
word_text = canvas.create_text(400, 263, text="Word", font=WORD_FONT)
canvas.grid(column=1, row=1, columnspan=2)

# Labels

# Right button
right_image = PhotoImage(file=RIGHT_IMG)
right_button = Button(image=right_image, highlightthickness=0, borderwidth=0, command=new_card)
right_button.grid(column=2, row=2)

# Wrong button
wrong_image = PhotoImage(file=WRONG_IMG)
wrong_button = Button(image=wrong_image, highlightthickness=0, borderwidth=0, command=new_card)
wrong_button.grid(column=1, row=2)

new_card()
flip_card()

window.mainloop()
