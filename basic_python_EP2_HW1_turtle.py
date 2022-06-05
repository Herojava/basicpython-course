import turtle
from random import *
tao = turtle.Pen()
tao.shape('turtle')

def Rectangle(l1=50):
    for i in range(4):
        tao.forward(l1)
        tao.left(90)

def Triangle1(l2=50):
    for i in range(3):
        tao.fd(l2)
        tao.right(120)

def Triangle2(l2=50):
    for i in range(3):
        tao.fd(l2)
        tao.left(120)

def Circle(r=50):
    tao.circle(r)
    
def Go(x=100, y=100):
    tao.penup()
    tao.goto(x, y)
    tao.pendown()




random_position_x = 0
random_position_y = 0
random_r = 0
random_l1 = 0
random_l2 = 0

for i in range(30):
    if i % 3 == 0:
        random_l1 = randint(10, 100)
        Rectangle(random_l1)

        random_position_x = randint(-200, 200)
        random_position_y = randint(-200, 200)
        Go(random_position_x, random_position_y)
        
        random_l2 = randint(10, 100)
        Triangle2(random_l2)

        random_position_x = randint(-200, 200)
        random_position_y = randint(-200, 200)
        Go(random_position_x, random_position_y)
        
    elif i % 3 == 1:
        random_r = randint(10, 100)
        Circle(random_r)
        
        random_position_x = randint(-200, 200)
        random_position_y = randint(-200, 200)
        Go(random_position_x, random_position_y)

        random_l1 = randint(10, 100)
        Rectangle(random_l1)
        
        random_position_x = randint(-200, 200)
        random_position_y = randint(-200, 200)
        Go(random_position_x, random_position_y)
        
    elif i % 3 == 2:       
        random_l2 = randint(10, 100)
        Triangle1(random_l2)
        
        random_position_x = randint(-200, 200)
        random_position_y = randint(-200, 200)
        Go(random_position_x, random_position_y)

        random_r = randint(10, 100)
        Circle(random_r)
        
        random_position_x = randint(-200, 200)
        random_position_y = randint(-200, 200)
        Go(random_position_x, random_position_y)


    

    
