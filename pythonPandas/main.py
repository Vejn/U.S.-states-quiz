import turtle
import pandas

# Creating screen
screen = turtle.Screen()
screen.setup(width=700, height=600)
screen.title("U.S. States Quiz")
image = "blank_states_img.gif"

# Adding background image
screen.addshape(image)

# Extracting data with pandas
data = pandas.read_csv("50_states.csv")

# Creating pen for states and pen for score
turtle.shape(image)
pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
score_pen = turtle.Turtle()
score_pen.penup()
score_pen.hideturtle()

# List of states to help us checking for right answer
state_list = data.state.values


# Main loop of game
num_try = 0
number_of_states = 0
while number_of_states != 50:
    score_pen.clear()
    score_pen.goto(250, 280)
    score_pen.write(f"Score: {number_of_states}/50")

    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
    num_try += 1
    if answer_state in state_list:
        answer = data[data.state == answer_state]
        x = int(answer.x)
        y = int(answer.y)
        pen.goto(x - 10, y)
        pen.write(answer_state)
        number_of_states += 1

score_pen.goto(0, 0)
score_pen.write(f"Congratulations, you guessed all states! It took you {num_try} guesses!")

screen.exitonclick()
