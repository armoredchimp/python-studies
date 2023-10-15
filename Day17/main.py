import data
import quiz_brain

quiz = quiz_brain.Quiz()
length = len(data.question_data)
while (quiz.asked < length):
    quiz.ask()
    print(f"You have a score of {quiz.score} out of {length}.\n")
else:
    print(f"The quiz has ended. You scored {quiz.score}")
