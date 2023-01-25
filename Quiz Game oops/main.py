from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    que = item['text']
    ans = item['answer']
    ques = Question(que,ans)
    question_bank.append(ques)
    
quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
