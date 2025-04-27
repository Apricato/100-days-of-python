import tkinter as tk

import json
from tkinter import messagebox
from random import choice , randint, shuffle 
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pasword():
    
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


  password_letters  = [choice(letters) for char in range(randint(8, 10)) ]
  password_symbols = [choice(symbols)  for char in range(randint(2, 4)) ]
  password_numbers = [choice(numbers) for char in range (randint(2, 4))]


  password = password_letters + password_symbols + password_numbers

  shuffle(password)
  password= "".join(password)

  messagebox.showinfo(title="Password generated", message="Password succcesfully generated" )
  enter_password.insert(0,password)


def search():
    
    with open("file.json", "r" ) as file:
        data = json.load(file)
        print(data)
        website=enter_website.get()
        try:
            website = data[website]
        except KeyError:
            messagebox.showerror(title="No match was found", message="That website is not registered yet")
        else:
 
            emaill = website['email']
            passwordd = website['password']
            messagebox.showinfo(title="Yes, we've found a match", message=f"{website},  {emaill}, {passwordd}")

# ---------------------------- SAVE PASSWORD ------------------------------- #

#Note there is no need to import the json lib cause it is by default on python
def getinput( ):
   
    emaile= enter_username.get()
    websitee= enter_website.get()
    passwordd = enter_password.get()
    new_data = { 
       websitee: {
          "email": str(emaile),
          "password":  str(passwordd)
          
       }
    } 

    if len (websitee) == 0 or len(passwordd) == 0:
        messagebox.showinfo(title="oops", message="Please make sure you have not left anything blank")


    else: 
         
         try:
            with open("file.json", "r") as file:
                 data= json.load(file)
         except FileNotFoundError:
            with open("file.json", "w") as file:
               json.dump(new_data, file ,indent=4)
               data= json.load(file)

         else:
               data.update(new_data)
               with open("file.json", "w") as file:
                  json.dump(data,file, indent=4)

         finally:
                  enter_password.delete(0,tk.END)
                  enter_website.delete(0 ,tk.END )
 
# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200)
logo = tk.PhotoImage(file="Day 29/password-manager-start/logo.png")


canvas.create_image(100 ,100 ,image=logo)


canvas.grid(row=0, column=1)

# Labels
website = tk.Label(text="Website:")
email = tk.Label(text="Email/Username:")
password = tk.Label(text="Password:")
#Button
add =tk.Button(text="Add",width=36, command= getinput)
generate = tk.Button(text="Generate Password", command=generate_pasword)
search= tk.Button(text= "search", command=search)
#Entry

enter_website = tk.Entry(width=35)
enter_username= tk.Entry(width=35)
enter_password= tk.Entry(width=21)
#Grids
website.grid(row=1,column=0)
enter_website.grid(row=1,column=1,columnspan=2)
email.grid(row=2,column=0 )

enter_username.grid(row=2,column=1,columnspan=2)
enter_password.grid(row=3,column=1)
password.grid(row=3,column=0)
add.grid(row=4,column=1,columnspan=2)
search.grid(row=1 ,column= 2)
generate.grid(row=3, column=2)


enter_website.focus()
enter_username.insert(0,"youremail@gmail.com")

window.mainloop()




