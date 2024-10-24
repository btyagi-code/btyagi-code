# Hi! This is my version of the popular snake game in Python. Enjoy!


# imports
import turtle
import time
import random

delay = 0.1

score =0
high_score=0

# Now we have to set up the screen 
sn = turtle.Screen()
sn.title("Snake Game by Bhawna.T")
sn.bgcolor("green")
sn.setup(width =600, height =600)
sn.tracer(0) # This turns off the animation

#Creating the head of the snake
head = turtle.Turtle()
head.speed(0) # This is the animation speed of the turtle
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction ="stop"

#Snake Food
food = turtle.Turtle()
food.speed(0) # This is the animation speed of the turtle
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

body = []

#writing
pen =turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0  High Score:0", align="center", font=("Courier", 24, "normal") )


#Funtions 
def move():
    if head.direction== "up":
        y= head.ycor()
        head.sety(y+20)
    if head.direction== "down":
        y= head.ycor()
        head.sety(y-20)
    if head.direction== "right":
        x= head.xcor()
        head.setx(x+20)
    if head.direction== "left":
        x= head.xcor()
        head.setx(x-20)

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_left():
    if head.direction != "right":
        head.direction = "left"


#Connecting to the keys
sn.listen()
sn.onkeypress(go_up, "Up")
sn.onkeypress(go_down, "Down")
sn.onkeypress(go_right, "Right")
sn.onkeypress(go_left, "Left")

#The Main Loop

while True:
    sn.update()

    #Checking for any border collisions
    if (head.xcor() > 290) or (head.xcor()< -290) or (head.ycor() > 290 )or ( head.ycor() < -290):
        time.sleep(1)
        head.goto(0,0)
        head.direction ="stop"

        # hide the body
        for bod in body:
            bod.goto(10000,10000)

        #clear 
        body.clear()

        #Reset Score
        score =0
        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score} ", align="center",font=("Courier", 24, "normal") )

        #Reset the delay 
        delay = 0.1 
        
            


    
    
    #collision
    if head.distance(food) < 20:
         x= random.randint(-290,290)
         y =random.randint(-290,290)
         food.goto(x,y)

         body_grow = turtle.Turtle()
         body_grow.speed(0)
         body_grow.shape("square")
         body_grow.color("blue")
         body_grow.penup()
         body.append(body_grow)

         delay -=0.001

         # increasing the score 
         score += 10

         if score > high_score:
             high_score = score
             pen.clear()
             pen.write(f"Score: {score}  High Score: {high_score} ", align="center",font=("Courier", 24, "normal") )

            
        
            


             

    #Move the end of the body first
    for index in range(len(body)-1, 0,-1):
        x = body[index-1].xcor()
        y= body[index-1].ycor()
        body[index].goto(x,y)

    # Move 1st body square to the front
    if len(body) > 0:
        x= head.xcor()
        y=head.ycor()
        body[0].goto(x,y)

    move()

    #Checking for head collsions with itself
    for bod in body:
        if  bod.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction ="stop"
            
            for bod in body:
                bod.goto(10000,10000)

        #clear 
            body.clear()
        #Reset the delay 
            delay = 0.1

            


    time.sleep(delay)





sn.mainloop()