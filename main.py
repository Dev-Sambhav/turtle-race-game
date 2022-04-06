from turtle import Turtle, Screen
import random

screen = Screen()
# set up the screen size
screen.setup(width=500, height=400)
screen.title("Turtle Race")

# taking user bet choice
user_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Enter a color: ").lower()

# each turtle color
turtle_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# set each turtle initial position
turtle_pos = [150, 90, 30, -30, -90, -150]
# init. a empty list for storing each turtle information
all_turtles = []

# initially set race is too off
is_race_on = False

# defining each turtle information and then appending into all_turtle list
for index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(turtle_colors[index])
    new_turtle.goto(x=-230, y=turtle_pos[index])
    all_turtles.append(new_turtle)

# if user_bet is given then we just start the race
if user_bet:
    is_race_on = True

# defining game_logic
while is_race_on:
    # checking each turtle information
    for turtle in all_turtles:
        # if turtle touches the end screen then i just end the race
        if turtle.xcor() > 230:
            is_race_on = False
            # getting winner turtle color
            winning_color = turtle.pencolor()
            # checking if winner turtle color is match with user_bet color or not ?
            if winning_color == user_bet:
                print(f"You've won the bet! {winning_color} turtle is the winner!")
            else:
                print(f"You've lost the bet! {winning_color} turtle is the winner!")
        # move each turtle with random step from 1 to 10 here 1 and 10 is included
        random_step = random.randint(1, 10)
        turtle.forward(random_step)

# finally, exit our screen with click
screen.exitonclick()
