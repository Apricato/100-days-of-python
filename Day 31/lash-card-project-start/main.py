import pandas 
from collections import deque

from tkinter import *
from PIL import Image, ImageTk

BACKGROUND_COLOR = "#B1DDC6"
SECONDS = 7000
queue = deque()


def pop_end():
    queue.popleft()

def new_word():
    #update info to show the front 

def flip_card():
    canvas.itemconfig(language, text ="English")
    canvas.itemconfig(word=)
    card = queue[0]
    pop_end()
    queue.append(card)

    window.after(SECONDS,new_word)

    

def trigger_change():
    pop_end()
    new_word()
    
#card flipping



# UI elements:

window= Tk()
window.config(bg=BACKGROUND_COLOR)
window.title("Flash card App")

canvas = Canvas(width=1000, height=700, bg=BACKGROUND_COLOR, highlightthickness=0)
unflipped_card= Image.open("Day 31\lash-card-project-start\images\card_front.png")
unflipped_card= unflipped_card.resize((800,526))
unflipped_card= ImageTk.PhotoImage(unflipped_card)


flipped_card= PhotoImage(file="Day 31\lash-card-project-start\images\card_back.png")
flipped_card = flipped_card.resize((800, 526))

canvas.create_image(500,350, image=unflipped_card)

language= canvas.create_text( 500, 250, text= 'Title', font= ("Ariel", 40, "italic"))
word= canvas.create_text(500, 363, text= 'word', font= ("Ariel", 40, "italic"))


canvas.grid(row=0, column=0, columnspan=2)




right_button = PhotoImage(file=r"Day 31\lash-card-project-start\images\right.png")
r_button = Button(image=right_button, highlightthickness=0, command=trigger_change)  # Removed quotes


left_button = PhotoImage(file=r"Day 31\lash-card-project-start\images\wrong.png")
l_button = Button(image=left_button, highlightthickness=0, command=flip_card)  # Removed quotes


l_button.grid(row=1, column=0)  # Add vertical padding
r_button.grid(row=1, column=1)


# Reading the dataframes

Dataframing = pandas.read_csv(r"Day 31\flash-card-project-start\data\french_words.csv")




window.mainloop()