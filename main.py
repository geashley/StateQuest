import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

score = 0
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state name?")
    title_answer = answer_state.title()
    if title_answer == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if title_answer in all_states and title_answer not in guessed_states:
        score += 1
        guessed_states.append(title_answer)
        select_state = data[data["state"] == title_answer]
        x = select_state.x.tolist()[0]
        y = select_state.y.tolist()[0]
        tim = turtle.Turtle()
        tim.up()
        tim.hideturtle()
        tim.goto(x, y)
        tim.write(title_answer, align="center", font=('Arial', 8, 'normal'))
    else:
        continue

# states_to_learn.csv



