file = open ('\\Users\\Pidamas4\\Desktop\\Sample_text.txt')
contents = file.read()

print (contents)

file.close()

#The root is a slash not a C or a MacintoshHD
#For going down on a folder more than once use ../ ../

archive = open ("..\\..\\..\\..\\Sample_text.txt")
contents = archive.read()
print(contents)
file.close()