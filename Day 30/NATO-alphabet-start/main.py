import pandas

DataFrame_NATO = pandas.read_csv("Day 26/NATO-alphabet-start/NATO-alphabet-start/nato_phonetic_alphabet.csv")
#print(DataFrame_NATO)
#Conversion de Datafrme a diccionario 
# {new_key : new_value for (index,row) in data.iterrows()}

NATO_dict = {row.letter :row.code for (index,row) in DataFrame_NATO.iterrows()}

def generate_phonetic():
    Word = input("Enter any word that youd like converted to NATO  alphabet \n ").upper()

    try:
        NATO_INPUT = {letter: NATO_dict[letter] for letter in Word}
    except KeyError:
        print("Sorry  only letters in the alphabet ")
        generate_phonetic()
    else:
        for letter in Word:
            print(f"{letter} as in {NATO_dict[letter]}")

generate_phonetic()
