import turtle
import pandas as pd

screen = turtle.Screen()
screen.setup(width = 1.0, height = 1.0)
screen.title("U.S. States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data.state.tolist()
states_guessed = []


def add_state(state, x, y):
    t = turtle.Turtle(visible = False)
    t.penup()
    t.speed("fastest")
    t.goto(int(x), int(y))
    t.write(state)


while len(states_guessed) < 51:
    answer_state = screen.textinput(title = f"{len(states_guessed)}/50 States Correct", prompt="Enter a state").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in states_guessed]
        for state in missing_states:
            state_data = data[data.state == state]
            add_state(state,state_data.x, state_data.y)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states and answer_state not in states_guessed:
        states_guessed.append(answer_state)
        state_data = data[data.state == answer_state]
        add_state(answer_state, state_data.x, state_data.y)




screen.exitonclick()

