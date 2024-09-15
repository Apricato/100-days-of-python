import pandas

squirrel_Data = pandas.read_csv(".\\Day 25\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_fur = (squirrel_Data[squirrel_Data["Primary Fur Color"] == "Gray"])
black_fur = (squirrel_Data[squirrel_Data["Primary Fur Color"]=="Black"])
Cinnamon_fur = (squirrel_Data[squirrel_Data["Primary Fur Color"]=="Cinnamon"])

gray_fur = gray_fur["Primary Fur Color"].squeeze()
black_fur = black_fur["Primary Fur Color"].squeeze()
Cinnamon_fur = Cinnamon_fur["Primary Fur Color"].squeeze()

gray_population = gray_fur.count() 
black_population = black_fur.count() 
Cinnamon_population = Cinnamon_fur.count() 

squirrel_dict = {
    "Gray" : [gray_population],
    "Black" : [black_population],
    "Cinnamon" : [Cinnamon_population]
}


Squirrels_df = pandas.DataFrame(squirrel_dict)

Squirrels_df.to_csv("Squirrel_csv")

print(Squirrels_df)