from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

question_bank = []
for i in question_data:
    question_bank.append(Question(i["question"], i["correct_answer"]))
quiz = Quizbrain(question_bank)
while quiz.question_number < len(quiz.question_list):
    quiz.next_question()
print(f"Your score: {quiz.score}")
