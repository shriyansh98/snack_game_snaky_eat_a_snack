from turtle import Turtle, Screen
STARTING_POSITION = [(0,0), (-20,0) , (-40,0)]
MOVE_DISTANCE = 20
HEAD= 0
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
screen = Screen()


                     
class Snake():

    def __init__(self):
        self.boxes = []
        self.create_snake()
        self.head = self.boxes[0]
        #super().__init__()

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_box(position)

    
    def add_box(self,position):
        new_box= Turtle("square")
        new_box.penup()
        new_box.color("white")
        new_box.setposition(position)
        self.boxes.append(new_box)
    
    def extend(self):
        self.add_box(self.boxes[-1].position())

        

    def move(self):
        for seg_number in range(len(self.boxes)-1, 0, -1):
            new_x = self.boxes[seg_number-1].xcor()
            new_y = self.boxes[seg_number-1].ycor()
            self.boxes[seg_number].goto(new_x,new_y)
        self.boxes[0].forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN: 
            self.head.setheading(UP)
        # else:
        #     #return random.choice([self.right(),self.left()])
        #     self.right()
            
    
    def down(self):
        if self.head.heading() != UP: 
            self.boxes[0].setheading(DOWN)
        # else:
        #     #return random.choice([self.right(),self.left()])
        #     self.left()
            
        

    def right(self):
        if self.head.heading() != LEFT:
            self.boxes[0].setheading(RIGHT)
        # else:
        #    # return random.choice([self.up(),self.down()])
        #    self.down()
        #    screen.update()
        #    time.sleep(2)
        #    self.left()
        #    screen.update()

            

    def left(self):
        if self.head.heading() != RIGHT:
            self.boxes[0].setheading(LEFT)
        # else:
        #     #return random.choice([self.up(),self.down()])
        #     # self.up()
        #     # screen.update()
        #     # self.right()
        #     # screen.update()

        #     self.boxes[0].setheading(UP)
        #     # self.boxes[0].forward(MOVE_DISTANCE)
        #     # self.boxes[0].setheading(RIGHT)
            
        #     # time.sleep(2)
        #     # screen.update()
        #     # self.move()
        #     self.boxes[0].forward(MOVE_DISTANCE) 
        #     time.sleep(1)
        #     self.boxes[0].setheading(LEFT)
        #     self.boxes[0].forward(MOVE_DISTANCE)
        #     time.sleep(1) 
        #     # self.move()   
            
       