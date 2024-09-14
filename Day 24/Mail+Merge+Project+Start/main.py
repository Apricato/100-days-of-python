
with open(".\\Input\\Names\\invited_names.txt")as names:
    invitees = names.readlines()


with open(".\\Input\\Letters\\starting_letter.txt") as template:
    lines = template.readlines()
    for name in invitees :
        new_letter = lines.replace("[name]",name)
        print(new_letter)







#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp