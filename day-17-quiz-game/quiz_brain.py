class Quizbrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        answer = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text} True/False? ")
        if self.check_answer(self.question_list[self.question_number].answer, answer):
            self.score += 1
            print("Correct!")
        else:
            print("That's wrong")
        self.question_number += 1

    def check_answer(self, qn, ans):
        return qn.lower() == ans.lower()
