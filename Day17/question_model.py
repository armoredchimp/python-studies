from data import question_data
import random


class Question:
    def __init__(self):
        random_question = random.choice(question_data)
        self.text = random_question['text']
        self.answer = random_question['answer'].lower()
        question_data.remove(random_question)
        print(self.text)
