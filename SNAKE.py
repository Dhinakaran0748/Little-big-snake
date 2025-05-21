import turtle, time, random
delay=0.1
#creation of screen is done
wn=turtle.Screen() 
wn.title('SNAKE XANIA')
wn.bgcolor('black')
wn.setup(width=600,height=600)
wn.tracer(0)

#creating the snake head
head=turtle.Turtle()
head.speed(0)
head.shape('triangle') #shape of the snake
head.color('white')
head.goto(0,0) #starts from the middle of axis
head.direction='stop'
head.penup() #tracing will be dissappeared
#Snake Food
food=turtle.Turtle()
food.speed(0)
food.color('white')
food.shape('square')
food.penup()
food.goto(0,90)
#score
pen=turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.goto(0,260)
pen.hideturtle()
score=0
pen.write(f"SCORE:{score}",align='center',font=('bold',28,'normal'))

def move():
    if head.direction=='up':
        y=head.ycor()
        head.sety(y+20)
    if head.direction=='down':
        y=head.ycor()
        head.sety(y-20)
    if head.direction=='right':
        x=head.xcor()
        head.setx(x+20)
    if head.direction=='left':
        x=head.xcor()
        head.setx(x-20)
    
def go_up():
    if head.direction!='down':
        head.direction='up'
def go_down():
    if head.direction!='up':
        head.direction='down'
def go_right():
    if head.direction!='left':
        head.direction='right'
def go_left():
    if head.direction!='right':
        head.direction='left'
    
wn.listen()
wn.onkeypress(go_up,'Up')
wn.onkeypress(go_down,'Down')
wn.onkeypress(go_right,'Right')
wn.onkeypress(go_left,'Left')
body=[]
score=0
pen.write(f"SCORE:{score}",align='center',font=('bold',28,'normal'))


while True:     
    wn.update()
    if head.xcor()>290 or head.xcor()<-290 or\
    head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.direction=='stop'
        head.goto(0,0)
        for i in body:
            i.goto(1000,1000)
        body.clear()
        score,delay=0,0.1
        pen.clear()
        pen.write(f"SCORE:{score}",align='center',font=('bold',28,'normal'))
        
    if head.distance(food)<20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)
        new_body=turtle.Turtle()
        new_body.speed(0)
        new_body.color('pink')
        new_body.penup()
        new_body.shape('square')
        body.append(new_body)
        score+=1
        delay=0.1
        pen.clear()
        pen.write(f"SCORE:{score}",align='center',font=('bold',28,'normal'))
        
    for i in range(len(body)-1,0,-1):
        x=body[i-1].xcor()
        y=body[i-1].ycor()
        body[i].goto(x,y)
    if len(body)>0:
        x=head.xcor()
        y=head.ycor()
        body[0].goto(x,y)
    delay-=0.0001
        
    time.sleep(delay)
    move()
    for i in body:
        if i.distance(head)<20:
            time.sleep(0)
            head.direction=='stop'
            head.goto(0,0)
            for i in body:
                i.goto(1000,1000)
            body.clear()
            score,delay=0,0.1
            score=0
            pen.clear()
            pen.write(f"SCORE:{score}",align='center',font=('bold',28,'normal'))




wn.mainloop()
