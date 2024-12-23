import tkinter 
#from tkinter import *

window = tkinter.Tk()  #This one shall go at the very begginign of every tkinter program you ever make
window.title("My first GUI program")
window.minsize(width= 700 , height = 500) #scales to include all components


#Label 


my_label = tkinter.Label(text = "I am a label " , font = ("Arial", 24, "bold"))
my_label.grid(column= 0, row= 0)

my_label["text"] = "New text"
my_label.config(text="New Text")

#Button
def button_clicked():
    
    my_label["text"] = input.get()



button = tkinter.Button(text = "Click Me", command = button_clicked)
button.grid(column=1, row= 1)

new_button = tkinter.Button(text = "A button", command = button_clicked)
new_button.grid(column= 2, row = 0)



input = tkinter.Entry(width=10)
input.grid(column=3 , row= 2)



window.mainloop() #Goes at the very end always

