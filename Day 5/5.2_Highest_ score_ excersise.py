student_scores = input ("Enter the scores: \n ").split ()

#Cambia a  inte la lista 
for n in range ( 0, len ( student_scores )):
   student_scores [n] = int (student_scores [n])

print (student_scores)

print ( max (student_scores))  
