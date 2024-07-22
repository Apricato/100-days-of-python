import pretty_tables

#Manejo basico de librerias , practica de documentacion y de librerias PYPI
colors = [ pretty_tables.Colors.red
          , pretty_tables.Colors.green,
          pretty_tables.Colors.cyan
          ,pretty_tables.Colors.bold]

Headers = [ 'ID', 'Cake', 'Flavor', 'toppings']
Rows = [ [12 , "Strawberry devil", "red velvet", "chocolate"],
       [12 , "Frustrated Moccha", "capuccino", "caramel"], 
       [12 , "Angel cake", "vainilla", "whipping cream"] ,  ]
          
table = pretty_tables.create( headers = Headers , rows = Rows ,   empty_cell_placeholder= 'No data', 
                             colors= colors )


print (table)