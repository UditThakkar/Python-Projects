class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
    
    def still_has_question(self):
        if self.question_number < 12:
            return True
        return False
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        # print(current_question.question)
        user_answer = input(f"Q.{self.question_number}: {current_question.question} (True/False): ")
        self.check_answer(user_answer,current_question.answer)
    
    def check_answer(self,user_answer, answer):
        if user_answer.lower() == answer.lower():
            print("You got it right! ")
            self.score += 1
        else:
            print("Thats wrong answer!")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")