class User:
    pass

user_one = User()
user_one.id = "002"
user_one.quirks = "fire"



print (user_one.quirks)

#PascalCase: capitalize the first letter in  names of classes vs Camel case
class PascalCase :
   def __init__(self,men):
       self.men = men
       self.bankaccount = 0
    #You can provide a standard value
   def get_payed(self, employer): #methods always need a self function and the user we are tracking
       employer.bankaccount -= 100
       self.bankaccount +=  100

       print("new user being created")




PascalSubject = PascalCase("A_french_man")
print (PascalSubject.men)

PascalSubject.type = "Pascal"
PascalSubject2 = PascalCase("An_english_man")
print (PascalSubject2.bankaccount)
# print (PascalSubject.type)
PascalSubject.get_payed(PascalSubject2) 
#pascal 1 gets payed from employer pascal 2

print (PascalSubject.bankaccount)
print (PascalSubject2.bankaccount)
