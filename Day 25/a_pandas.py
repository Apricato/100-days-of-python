import pandas

data = pandas.read_csv("Day 25\weather_data.csv")
print(type(data))


print (data)
print (data ["temp"]) #print a single column 

#En oandas tenemos data frames ( dos dimensiones ) y series (Una sola dimensión una columa por ejemplo, uns lista)

print(data.to_dict())

temp_list = data["temp"].to_list()
print (temp_list)