from modelo_de_preguntas import Question 
from datas  import questionne_data
from modelo_de_quizzes import QuizBrain


question_bank = []

#donde results esta dentro del diccionario questione y es una lista de  diccionarios y esos a su ves para accedera ellos se necesita un indice a la lista y 
#luego indicar la lista de diccionarios
for question in questionne_data["results"]:
      question_text = question["question"]
      question_answer = question ["correct_answer"]
      new_question = Question( question_text,question_answer)
      question_bank.append(new_question) #esta agreagandolo a la lista 

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions():
   quiz.next_question()