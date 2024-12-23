def add (*args):   #the default is args but it can be other n numbers and it doesnt matter at all 
    
    total = 0 
    for n in args:
        total += n
    return total

#Its unlimite dpositional arguments or free real state y'all so nice !11!


print (add (3,5,6,4,6,7,2,3,3,3,3,3,3,3,3,3,3,3,3,3,))


def calculate(n , **kwargs): #unlimited  keyword arguments
    print(kwargs) #and you get a dictionary  with your keyword arguments
    for key, value in kwargs.items():
        print (key)
        print (value)
    print (kwargs["add"])

    n += kwargs["add"]
    print(n)
    n *= kwargs["multiple"]
    print(n)



#look thought the imputs and fins what you want
calculate ( 2, add = 3 , multiple = 5 )


class Car :
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]

#So to avoid mistakes when making dictionaries in which you might not get all **kwargs you can use .get
#if theres no argument youll get none

class Flower:
    def __init__(self,**kw):
        self.colour = kw.get("color")
        self.petals = kw.get("petals")
        self.height = kw.get("height")


car_1 = Car(make = "Nissan" , model = "GT-R")
print(car_1.make)

flower_1 = Flower(colour= "red", petals = "5")
print(flower_1.height) #this is going to return none! no problem :)
