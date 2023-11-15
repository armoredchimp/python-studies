import turtle
import pandas as p

screen = turtle.Screen()
screen.setup(width=800, height=600)

screen.title('StatesGame')
img = 'D:/Python/States/blank_states_img.gif'
screen.addshape(img)
turtle.shape(img)
pen = turtle.Turtle()
pen.penup()
pen.speed(10)
pen.hideturtle()

states_doc = p.read_csv('D:/Python/States/50_states.csv')
answered, remaining = [], []


def question(score, guesses):
    while score < 50 and guesses < 65:
        answer_state = screen.textinput(
            title=f"{score}/50 states Correct", prompt="Name another state:")
        if answer_state is None:
            print("Exiting now")
            return
        for state in states_doc.state:
            if answer_state.lower() == state.lower() and answer_state.lower() not in answered:
                write_state(state)
                answered.append(state.lower())
                score, guesses = score + 1, guesses + 1
                return question(score, guesses)
        print('Invalid input')
        guesses += 1
        question(score, guesses)
    if guesses == 65:
        top_text('Here are the states you missed:')
        education()
    elif score == 50:
        top_text('You win')


def write_state(state):
    x, y = states_doc[states_doc.state ==
                      state].x.iloc[0], states_doc[states_doc.state == state].y.iloc[0]
    pen.goto(x, y)
    pen.write(f'{state}')


def top_text(text):
    top_pen = turtle.Turtle()
    top_pen.penup()
    top_pen.goto(-250, 250)
    top_pen.write(f'{text}', font=("Arial", 14, "normal"), align="center")


def education():
    for state in states_doc.state:
        if state not in answered:
            remaining.append(state)
    for state in remaining:
        write_state(state)


question(0, 0)

screen.exitonclick()
# self.write(f"{self.score}", font=(
#             "Arial", 12, "normal"), align="right")
