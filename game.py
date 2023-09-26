from turtle import Screen 
from snake import Snake
from mouse import Mouse
from scoreboard import Scoreboard
import time

# from test_turtle import Test 

screen = Screen()
playing = True

def run_game():
    playing = True

    screen.setup(width = 600 , height = 600)
    screen.bgcolor("black")
    screen.title("SNAKY EATS A SNACK")
    screen.tracer(0)

    onix = Snake()
    food = Mouse()
    scoreboard = Scoreboard()
    # text = Test()

    screen.listen()

    screen.onkey(onix.up,"Up")
    screen.onkey(onix.down,"Down")
    screen.onkey(onix.left,"Left")
    screen.onkey(onix.right,"Right")

    def game_over():
        scoreboard.game_over()
        restart = screen.textinput("SNAKY EATS A SNACK","REPLAY (y/n) ").capitalize()
        if restart == "Y":
            screen.clearscreen()
            run_game()
        else:
            screen.bye()
    
    while playing:
        screen.update()
        time.sleep(0.1)
        onix.move()


        if onix.head.distance(food) < 15:
            food.new_mouse()
            onix.extend()
            scoreboard.score_increase()


        
        if onix.head.xcor() > 295 or onix.head.xcor() < -295 or onix.head.ycor() > 295 or onix.head.ycor() < -295:
            playing = game_over()

        for box in onix.boxes[1:]:    
            if onix.head.distance(box) < 10:
                playing= game_over()



run_game()
#screen.exitonclick()

