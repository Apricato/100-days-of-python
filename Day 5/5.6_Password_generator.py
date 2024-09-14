#Password Generator 

import random 


letters = [ "a", "b","c","d", "e", "f", "g", "h", "i", 
                      "k ", "l", "m", "n", "o" , "p", "q", "r", "s", "t", "u", "v",
                      "w", "x", "y", "z", "A","B", "C","D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V"]

numbers=  ["1", "2", "3", "4", "5", "6", "7", "8", "9","0"]
symbols = [ ".", "!", "#", "?","#","¿"]
password= []



print ("-------  PYTHON PASSWORD GENERATOR-------  \n")
Number_letters = int (input ("How  many letters  you like in your password \n "))
number_Of_symbols= int (input ("How many symbols  would you like in your password \n "))
number_Of_Numbers = int (input ("How many numbers would you like in your password \n "))

total= Number_letters+number_Of_symbols+number_Of_Numbers
n_l=0
n_s=0
n_r=0


for i in range (0, total  ):
     
     if n_l != Number_letters : 
         password.append(random.choice(letters))
         n_l += 1 
     elif  n_s != number_Of_symbols:
         password.append(random.choice(symbols))
         n_s += 1 
     else: 
          password.append(random.choice(numbers))

     
random.shuffle(password)
password_string = ''.join(password)
print ( f"Your password is {password_string}")

      

    
   