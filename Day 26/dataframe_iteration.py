import pandas

students_dict = {
    "student" : ["Angela" , "James", "Lilly"],
    "score" : [56,76,98]
}

#Iteracion en diccionarios
#Looping through dictionaries

#
new_DataFrame = pandas.DataFrame(students_dict)
print (new_DataFrame)
#Looping through a dataframe
 
for (index , row) in new_DataFrame.iterrows():
    print(row.score)
