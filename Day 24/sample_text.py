file = open('Sample_text.txt')
contents = file.read()

print (contents)

file.close()

#You need to close the open file 

#Alternative way : with , allows you to not close the file
# w is for write can read it
#a is for append (doesnt get rid of the former text) and you cannot read it
with open ('Sample_text.txt' , mode = "a") as a_file:
    a_file.write("New text file")
# contents = a_file.read()
# print (contents)

#if you create a new one but it doesnt exist it will create it as long as it is in W mode

with open ("A_new_file.txt", mode = "w") as textie:
    textie.write("This is a new text file")