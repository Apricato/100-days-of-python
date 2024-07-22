#Asking questions
#chacking ig the answer is correct
#Checking ig we are at the end of the quiz

class   QuizBrain:
    def __init__(self,question_l):
        self.question_number = 0 #no olvidar el self
        self.question_list = question_l
        self.score = 0

    def next_question (self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} : {current_question.text} (True/False)")
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len (self.question_list) #automaticamente regresa true o false sin necesidad de indicarlo , al comparar
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():   #change to lowercas so they are compaable 
          print ("You are correct! Congratualtions")
          self.score += 1
        else:
            print (f"Thats wrong")

        print (f"The correct answer was : {correct_answer}")
        print (f"Your current score is ({self.score}/{self.question_number})")