import pandas

data = pandas.read_csv("Day 25\weather_data.csv")
'''
#Calculation of average temperature

temperature_list = data["temp"].to_list()

promedio = sum(temperature_list)/ len(temperature_list)
print (promedio)

#Con funciones de pandas

print (data["temp"].mean())
print(data["temp"].max())




''' 

maximum_temp = data["temp"].max()
#print(data.condition)


#Get data from rows

# print(data[data.day == "Monday"])

print (data[data.temp == maximum_temp])
print (data[data.temp == data["temp"].max()])


monday = data[data.day == "Monday"]
monday_temp  = monday.temp[0]
Monday_farenheit =  monday_temp * 9/5 + 32
print(Monday_farenheit)

