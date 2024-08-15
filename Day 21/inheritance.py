class Animal:
    def __init__(self):
          self.num_eye = 2
    def breather(self):
         print ("Inhale, exhale.")


class Fish (Animal): # en parentesis la clase heredada
     def __init__(self):
          super().__init__()

     def breather(self):
          super().__init__() # Overrides the earlier method so you can write new code and expand the method
          print ("doing this underwater.")

     def swim (self):
        print ("moving in the water")

nemo = Fish()
nemo.swim()
nemo.breather() #This is inhrited
print (nemo.num_eye)