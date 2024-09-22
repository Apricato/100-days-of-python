#Lists and Dictionary Comprehensions

Very unique to python, makes the code easier to read and shorter
Las list comprehensions y dictionary comprehensions en Python son maneras concisas y elegantes de crear listas y diccionarios a partir de iterables, en lugar de usar bucles convencionales como for o funciones como map. Se utilizan para simplificar y hacer más legible el código cuando deseas construir nuevas listas o diccionarios en una sola línea.
What is it? 


_______________________________________________________________
BRIEF EXAMPLE:

numbers = [1,2,3]

new_list = []
 for n in list:
    add_1 = n + 1

new_list.apprend(add_1)

For that list you'd probably have to iterate over each for performing a basic operation which is a really
long and annoying thing to do something

so instead you have the following structure:

new_list = [new_item  for item in list]

the equivalent for the numbers example:

new_list = [n+1 for n in numbers]


CONDITIONAL LIST COMPREHENSION

new_list = [new_item for item in list if test]




DICTIONARY COMPREHENSION:

new_dict = { new_key :new_value for item in list }

create a dictionary based of the values of an existing dictionaries:

new_dict = {new_key:new_value for (key,value) in dict.items()}

So you take the dictionary and then take hold of all of the items inside the dictionary , split it into key and value and then you can create a new one


new_dict = {new_key:new_value for (key,value) in dict.items() if test}