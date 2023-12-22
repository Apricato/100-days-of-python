''' wrtie a program that calculates average height from list of height '''
Loops_Traversed = 0
gpa_adition= 0 

student_height = input( "Enter a list of heights \n ").split()
for n in range (0, len(student_height)):
    student_height[n]=int(student_height[n])
    gpa_adition = student_height[n]+ gpa_adition
    Loops_Traversed += 1
    

print (student_height)
average_height = gpa_adition / Loops_Traversed
print (f"average height is:  { average_height}"  )


#Using specific python function : 
  #sum is abstraction, lengs gets number of items in a list 
total_height = sum (student_height )
number_of_students = len (student_height)
average_height = round ( total_height/number_of_students)
print (average_height)


