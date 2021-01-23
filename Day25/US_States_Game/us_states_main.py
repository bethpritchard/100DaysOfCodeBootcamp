import turtle
import pandas as pd

screen = turtle.Screen()
screen.screensize(900,900)
screen.title("U.S. States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data.state.tolist()
states_guessed = []



while len(states_guessed) < 51:
    answer_state = screen.textinput(title = f"{len(states_guessed)}/50 States Correct", prompt="Enter a state").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in states_guessed:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        states_guessed.append(answer_state)

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)

        missing_states.remove(answer_state)




screen.exitonclick()

