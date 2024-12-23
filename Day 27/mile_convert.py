from tkinter import *


#Set window

window= Tk()
window.title("Mile to Km converter")
window.minsize(width = 100 , height = 100)

#Functions

def to_kilometer():
    miles= int(Input.get())
    kilometer = miles * 1.60934
    convert_label.config( text= str(kilometer))



#Labels

miles_label = Label(text = "miles")
miles_label.grid(column=2, row= 0)

Kilometer_label = Label(text="Km")
Kilometer_label.grid(column=2, row=1)

sentence = Label(text = "is equal to")
sentence.grid(column=0, row= 1)

convert_label = Label(text = "0")
convert_label.grid(column= 1, row=1)

#Buttons

calc_button = Button(text="Calculate", command= to_kilometer)
calc_button.grid(column=1, row=2)
#Inputs
Input = Entry()
Input.grid(column= 1 , row= 0)



window.mainloop()

