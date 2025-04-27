import pandas 
from collections import deque

from tkinter import *
from PIL import Image, ImageTk

BACKGROUND_COLOR = "#B1DDC6"
SECONDS = 2000

df = pandas.read_csv(r"Day 31\flash-card-project-start\data\french_words.csv")
queue = deque()


for _ , row in df.iterrows():
   queue.append({"French": row["French"], "English": row["English"]})
   


def fetch_word():
    if not queue:
        print("Queue is empty, no more words to show.")
        canvas.itemconfig(language, text="All done!")
        canvas.itemconfig(word, text="Great job!")

    
    current_card = queue[0]
    if canvas.itemcget(current_image, "image") == str(flipped_card):
     canvas.itemconfig(current_image, image = unflipped_card)

    canvas.itemconfig(language,text = "French", fill ="black")
    canvas.itemconfig(word,text=current_card["French"], fill ="black")


def wrong_guess():

     
    if not queue:
        print("Queue is empty, no more words to show.")
        canvas.itemconfig(language, text="All done!")
        canvas.itemconfig(word, text="Great job!")
        return

    current_card = queue[0]
    canvas.itemconfig(current_image, image = flipped_card)
    canvas.itemconfig(language, text ="English", fill ="white")
    canvas.itemconfig(word,text=current_card["English"], fill ="white")

    card = current_card
    queue.popleft()
    queue.append(card)

    window.after(SECONDS,fetch_word)

    

def right_guess():

   
    if not queue:
        print("Queue is empty, no more words to show.")
        canvas.itemconfig(language, text="All done!")
        canvas.itemconfig(word, text="Great job!")

    queue.popleft()
    fetch_word()
    

# UI elements:

window= Tk()
window.config(bg=BACKGROUND_COLOR)
window.title("Flash card App")

canvas = Canvas(width=1000, height=700, bg=BACKGROUND_COLOR, highlightthickness=0)
unflipped_card= Image.open(r"Day 31\flash-card-project-start\images\card_front.png")
unflipped_card= unflipped_card.resize((800,526))
unflipped_card= ImageTk.PhotoImage(unflipped_card)


flipped_card= Image.open(r"Day 31\flash-card-project-start\images\card_back.png")
flipped_card= flipped_card.resize((800,526))
flipped_card= ImageTk.PhotoImage(flipped_card)

current_image = canvas.create_image(500,350, image=unflipped_card)

language= canvas.create_text( 500, 250, text= '', font= ("Ariel", 40, "italic"))
word= canvas.create_text(500, 363, text= '', font= ("Ariel", 40, "italic"))


canvas.grid(row=0, column=0, columnspan=2)




right_button = PhotoImage(file=r"Day 31\flash-card-project-start\images\right.png")
r_button = Button(image=right_button, highlightthickness=0, command=right_guess)  # Removed quotes


left_button = PhotoImage(file=r"Day 31\flash-card-project-start\images\wrong.png")
l_button = Button(image=left_button, highlightthickness=0, command=wrong_guess)  # Removed quotes


l_button.grid(row=1, column=0)  # Add vertical padding
r_button.grid(row=1, column=1)


window.after(1, fetch_word)

window.mainloop()