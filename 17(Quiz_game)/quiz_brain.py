class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        q = self.question_list[self.question_number]
        self.question_number += 1
        user_inp = input(f"Q{self.question_number}: {q.text} (True/False): ")
        self.check_answer(user_inp, q.answer)

    def check_answer(self, usr_in, correct_answer):
        if usr_in.lower() == correct_answer.lower():
            print("You got is right!")
            self.score += 1
        else:
            print("NO! You got it wrong!")
        print(f"The correct answer is {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
