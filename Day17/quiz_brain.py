import question_model


class Quiz:
    def __init__(self):
        self.score = 0
        self.asked = 0

    def ask(self):
        q = question_model.Question()
        ask = input("Type the answer:\n").lower()
        if (ask == q.answer):
            self.score += 1
            self.asked += 1
            print("Correct!")
        else:
            self.asked += 1
            print("Wrong!")
