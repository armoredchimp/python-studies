import turtle
import pandas as p

screen = turtle.Screen()
screen.setup(width=750, height=550)
screen.title('StatesGame')
img = 'D:/Python/States/blank_states_img.gif'
screen.addshape(img)
turtle.shape(img)
pen = turtle.Turtle()
pen.penup()
pen.hideturtle()

states_doc = p.read_csv('D:/Python/States/50_states.csv')
answered = []


def question(score):
    while score < 50:
        answer_state = screen.textinput(
            title=f"{score}/50 states Correct", prompt="Name another state:")
        if answer_state is None:
            print("Exiting now")
            return
        for state in states_doc.state:
            if answer_state.lower() == state.lower() and answer_state.lower() not in answered:
                x, y = states_doc[states_doc.state ==
                                  state].x.iloc[0], states_doc[states_doc.state == state].y.iloc[0]
                pen.goto(x, y)
                pen.write(f'{state}')
                answered.append(state.lower())
                score += 1
                return question(score)
        print('Invalid input')
        question(score)
    print('You win')


question(0)

screen.exitonclick()
