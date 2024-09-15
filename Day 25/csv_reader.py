#with open("Day 25\weather_data.csv") as weather:
#   data = weather.readlines() #readline is a single not all
#  print(data)

import csv 
import pandas


with open("Day 25\weather_data.csv") as weather:
    data = csv.reader(weather)
    temperatures = []
    for row in data:
        if row[1] != "temp":
         temperatures.append(int(row[1]))
    print(temperatures)


#PANDAS HANDLING

datas = pandas.read_csv("Day 25\weather_data.csv")

print (datas)
print (datas ["temp"]) #print a single column 
