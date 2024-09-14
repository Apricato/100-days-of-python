
Placeholder = "[name]"

with open(".\\Mail+Merge+Project+Start\\Input\\Names\\invited_names.txt")as names:
    invitees = names.readlines()


with open(".\\Mail+Merge+Project+Start\\Input\\Letters\\starting_letter.txt") as template:
    contents = template.read()
    for name in invitees :
        stripped_name = name.strip()
        new_letter = contents.replace("[name]",stripped_name)
        with open (f".\\Mail+Merge+Project+Start\\Output\\{stripped_name}.txt", mode="w") as named_letter:
            named_letter.write(new_letter)







#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp