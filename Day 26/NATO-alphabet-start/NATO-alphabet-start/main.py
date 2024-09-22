import pandas

DataFrame_NATO = pandas.read_csv("Day 26/NATO-alphabet-start/NATO-alphabet-start/nato_phonetic_alphabet.csv")

#Conversion de Datafrme a diccionario 
# {new_key : new_value for (index,row) in data.iterrows()}

NATO_dict = {row.letter :row.code for (index,row) in DataFrame_NATO.iterrows()}

Word = input("Enter any word that youd like converted to NATO  alphabet \n ").upper()
print (Word)

NATO_INPUT = { letter : code for (letter,code) in NATO_dict.items() if letter in Word}

for letter in Word:
    print(f"{letter} as in {NATO_dict[letter]}")

#Checar dictionary comprehension y data frames


