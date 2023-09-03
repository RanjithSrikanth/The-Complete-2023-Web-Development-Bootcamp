from turtle import Turtle, Screen
import numpy as np

screen = Screen()
screen.setup(1000,800)
color = np.array(['red','blue','orange','yellow','green','grey'])
print(color)
user_input = screen.textinput('CHOOSE YOUR COLOR : ','PICK A COLOR: ')

all_turtles = []

y=-200

for i in range(6):
    y += 50
    aamai = Turtle()
    aamai.shape('turtle')
    aamai.color(color[i])
    aamai.penup()
    aamai.goto(-480,y)
    all_turtles.append(aamai)

race_is_on = False

if user_input:
    race_is_on = True

    while race_is_on:
        for aamai in all_turtles:
            if aamai.xcor() > 470:
                race_is_on = False
                winner = aamai.pencolor()
                if winner == user_input:
                    print("You've won the race")
                    # Turtle.write("Hello there!", align="center", font=("Cooper Black", 25, "italic"))
                else:
                    print('Better luck next time')
                    # Turtle.write('Better luck next time', align="center", font=("Cooper Black", 25, "italic"))
            random_distance = np.random.randint(0,10)
            aamai.forward(random_distance)

screen.exitonclick()
