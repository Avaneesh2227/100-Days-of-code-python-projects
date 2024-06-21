BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas as pd
import random

try:
    data=pd.read_csv("data/words-to-learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
data=data.to_dict(orient="records")

current_card={}

def generate_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(data)
    card.itemconfig(canvas_image, image=card_front)
    card.itemconfig(title, text="French", fill="black")
    card.itemconfig(word,text=current_card["French"],fill="black")
    flip_timer=window.after(3000,flip)


def flip():
    global current_card
    card.itemconfig(canvas_image, image=card_back)
    card.itemconfig(title, text="English", fill="white")
    card.itemconfig(word, text=current_card["English"], fill="white")

def is_known():
    data.remove(current_card)
    generate_card()
    new_data=pd.DataFrame(data)
    new_data.to_csv("data/words-to-learn.csv",index=False)


window=Tk()
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
window.title("Flashy")

flip_timer=window.after(3000,flip)


card=Canvas(height=526,width=800,bg=BACKGROUND_COLOR,highlightthickness=0)
card_front=PhotoImage(file="images/card_front.png")
card_back=PhotoImage(file="images/card_back.png")
canvas_image=card.create_image(400,263,image=card_front)
card.grid(row=0,column=0,columnspan=2)




title=card.create_text(400,150,text="French",font=("Ariel",40,"italic"))
word=card.create_text(400,263,text="Word",font=("Ariel",60,"bold"))

tick=PhotoImage(file="images/right.png")
tick_btn=Button(image=tick,command=is_known)
tick_btn.grid(row=1,column=1)

cross=PhotoImage(file="images/wrong.png")
tick_btn=Button(image=cross,command=generate_card)
tick_btn.grid(row=1,column=0)

generate_card()
window.mainloop()

