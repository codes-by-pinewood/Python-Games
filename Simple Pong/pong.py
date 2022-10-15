import turtle 
import os 

wn = turtle.Screen()
wn.title("Pong by @codes-by-pinewood")
wn.bgcolor("orange") #background color
wn.setup(width=800,height = 600)
wn.tracer(0) #stops the window from updating, so it has to be manually updated

#Paddle A 
paddle_a = turtle.Turtle()
paddle_a.speed(0) #sets speed to max possible speed
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup() 
paddle_a.goto(-350,0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("green")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup() 
paddle_b.goto(350,0)

#Ball 
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup() 
ball.goto(0,0)

ball.dx = 2 
ball.dy = 2

#Score 
score_a = 0
score_b = 0

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: {}, Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))



#Function to move the paddle A,b up down
def paddle_A_up():
    y = paddle_a.ycor()#ycor is from the turtle module
    y += 20
    paddle_a.sety(y)

def paddle_A_down():
    y = paddle_a.ycor()#ycor is from the turtle module
    y -= 20
    paddle_a.sety(y)

def paddle_B_up():
    y = paddle_b.ycor()#ycor is from the turtle module
    y += 20
    paddle_b.sety(y)

def paddle_B_down():
    y = paddle_b.ycor()#ycor is from the turtle module
    y -= 20
    paddle_b.sety(y)

#listen for keyboard input
wn.listen() 
wn.onkeypress(paddle_A_up,"w")
wn.onkeypress(paddle_A_down,"s")
wn.onkeypress(paddle_B_up,"Up")
wn.onkeypress(paddle_B_down,"Down")


#Main game loop 
while True:
    wn.update() #updates the screen
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking 
    if (ball.ycor() > 290):
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

        

    if (ball.ycor() < -290):
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")
        

    if (ball.xcor() > 390):
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1 
        os.system("afplay bounce.wav&")
        pen.clear()
        pen.write("Player A: {}, Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if (ball.xcor() < -390):
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1 
        os.system("afplay bounce.wav&")
        pen.clear()
        pen.write("Player A: {}, Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


    if ball.xcor() > 340 and ball.xcor() <350 and ball.ycor() < paddle_b.ycor()+50 and ball.ycor() > paddle_b.ycor() -50:
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")
        


    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < paddle_a.ycor()+50 and ball.ycor() > paddle_a.ycor() -50:
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")

