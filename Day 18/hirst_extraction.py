from turtle import Turtle
import colorgram 

list_of_colors = []
colors = colorgram.extract('spot.jpg',12)


for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    list_of_colors.append(new_color)


print (list_of_colors)

color_list= [(5,196,178),(48,100,26),(1,58,145),(247,207,32),(235,65,6),(248,181,212),(189,0,32),(76,144,225),(123,18,23),(130,21,112),(245,163,1),(1,128,207)]