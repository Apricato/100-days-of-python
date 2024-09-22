numbers = [1,2,3]
new_numbers = [ n+1 for n in numbers]
print(new_numbers)

name = "Angela"
letters_list_list = [letter for letter in name]
print(letters_list_list)


double_range = [n*2 for n in range(1,5)]
print(double_range)

people = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
four_names = [name for name in people if len(name) == 4]
print(four_names)

all_caps = [name.upper() for name in people if len(name) > 5]
print (all_caps)