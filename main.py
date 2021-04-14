import turtle
import pandas


screen = turtle.Screen()
screen.title("US states game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



# building lists of states and x and y coordinates from CSV file
states_data = pandas.read_csv("50_states.csv")
state_list = states_data["state"].to_list()
state_x = states_data["x"].to_list()
state_y = states_data["y"].to_list()

#create turtle that will write name on image when correct answer

turt = turtle.Turtle()
turt.hideturtle()
turt.penup()
turt.pencolor("black")

#create function to go to x and y coordinate and write name of state
def write_name(index):
    turt.goto(state_x[index], state_y[index])
    turt.pendown()
    turt.write(arg=state_list[index],align="center")
    turt.penup()
    state_list.pop(index)
    state_x.pop(index)
    state_y.pop(index)

#create game loop
game_is_on = True
count_correct = 0
while game_is_on:
    answer_state = screen.textinput(f"{count_correct}/50 States correct", "What's another state name?")
    #check if correct
    title_answer = answer_state.title()
    if title_answer in state_list:
        index = state_list.index(title_answer)
        write_name(index)
        count_correct += 1


screen.exitonclick()

