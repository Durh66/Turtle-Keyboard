import turtle
import math

bob = turtle.Turtle()
s = turtle.Screen()
bob.pencolor("green")
s.bgcolor("black")
bob.penup()
bob.goto(-200,0)
bob.pendown()

def letter_r(t):
    t.lt(90)
    t.fd(100)
    t.penup()
    t.bk(40)
    t.rt(90)
    t.lt(45)
    t.pendown()
    t.fd(55)
    t.penup()
    t.bk(55)
    t.lt(45)
    t.rt(180)
    t.fd(60)
    t.lt(90)
    t.fd(75)
    t.pendown()

def letter_M(t):
    t.lt(90)
    t.fd(100)
    t.rt(150)
    t.fd(50)
    t.lt(120)
    t.fd(50)
    t.rt(150)
    t.fd(100)
    t.penup()
    t.lt(90)
    t.fd(100)
    t.pendown()

def letter_O(t):
    def circle(t, radius):
        circumference = 2 * math.pi * radius
        sides = 100
        length = circumference / sides
        for i in range(sides):
            t.forward(length)
            t.lt(360/sides)
    circle(t, 50)
    t.penup()
    t.fd(125)
    t.pendown()

def letter_V(t):
    t.lt(75)
    t.fd(100)
    t.penup()
    t.bk(100)
    t.lt(100)
    t.rt(75)
    t.pendown()
    t.fd(100)

def letter_D(t):
    t.lt(90)
    t.fd(100)
    def circle(t, radius, angle):
        circumference = 2 * math.pi * radius
        sides = 100
        length = circumference / sides
        steps = int(sides * angle / 360)

        t.rt(90)
        t.pendown()
        for _ in range(steps):
            t.forward(length)
            t.rt(angle / steps)
    circle(bob, 50, 180)
    t.rt(180)
    t.penup()
    t.fd(100)
    t.pendown()

def letter_B(t):
    t.lt(90)
    t.fd(50)
    def circle(t, radius, angle):
        circumference = 2 * math.pi * radius
        sides = 100
        length = circumference / sides
        steps = int(sides * angle / 360)

        t.rt(90)
        t.pendown()
        for _ in range(steps):
            t.forward(length)
            t.rt(angle / steps)
    circle(t, 25, 180)
    t.fd(2)
    t.rt(90)
    t.penup()
    t.fd(50)
    t.pendown()
    t.fd(50)
    circle(t, 25, 180)
    t.fd(2)
    t.lt(90)
    t.penup()
    t.fd(50)
    t.lt(90)
    t.fd(75)
    t.pendown()

def letter_L(t):
    t.fd(65)
    t.penup()
    t.bk(65)
    t.lt(90)
    t.pendown()
    t.fd(100)
    t.penup()
    t.bk(100)
    t.rt(90)
    t.fd(150)
    t.pendown()

def letter_H(t):
    t.lt(90)
    t.fd(100)
    t.penup()
    t.bk(100)
    t.rt(90)
    t.fd(50)
    t.lt(90)
    t.pendown()
    t.fd(100)
    t.penup()
    t.bk(50)
    t.lt(90)
    t.pendown()
    t.fd(50)
    t.penup()
    t.lt(90)
    t.fd(50)
    t.lt(90)
    t.fd(100)
    t.pendown()

def letter_k(t):
    t.lt(90)
    t.fd(100)
    t.penup()
    t.bk(50)
    t.rt(90)
    t.lt(60)
    t.pendown()
    t.fd(50)
    t.penup()
    t.bk(50)
    t.rt(60)
    t.rt(60)
    t.pendown()
    t.fd(50)
    t.penup()
    t.bk(50)
    t.rt(30)
    t.fd(50)
    t.lt(90)
    t.fd(75)
    t.pendown()

def letter_I(t):
    t.fd(25)
    t.bk(50)
    t.penup()
    t.fd(50)
    t.lt(90)
    t.pendown()
    t.fd(100)
    t.rt(90)
    t.fd(50)
    t.bk(100)
    t.penup()
    t.fd(50)
    t.rt(90)
    t.fd(100)
    t.lt(90)
    t.fd(150)
    t.pendown()

def letter_P(t):
    t.lt(90)
    t.fd(35)
    t.penup()
    t.bk(35)
    t.pendown()
    t.rt(90)
    def circle(t, radius, angle):
        circumference = 2 * math.pi * radius
        sides = 100
        length = circumference / sides
        steps = int(sides * angle / 360)
        t.rt(90)
        t.pendown()
        for _ in range(steps):
            t.forward(length)
            t.rt(angle / steps)
    circle(t, 25, 180)
    t.fd(35)
    t.penup()
    t.bk(60)
    t.rt(90)
    t.fd(100)
    t.pendown()

def letter_A(t):
    t.lt(60)
    t.fd(100)
    t.rt(120)
    t.fd(100)
    t.bk(50)
    t.rt(120)
    t.fd(50)
    t.penup()
    t.lt(60)
    t.fd(50)
    t.lt(120)
    t.fd(150)
    t.pendown()

def letter_S(t):
    t.lt(90)
    def circle(t, radius, angle):
        circumference = 2 * math.pi * radius
        sides = 100
        length = circumference / sides
        steps = int(sides * angle / 360)
        t.rt(90)
        t.pendown()
        for _ in range(steps):
            t.forward(length)
            t.lt(angle / steps)
    def circle2(t, radius, angle):
        circumference = 2 * math.pi * radius
        sides = 100
        length = circumference / sides
        steps = int(sides * angle / 360)
        t.rt(90)
        t.pendown()
        for _ in range(steps):
            t.forward(length)
            t.rt(angle / steps)
    circle(t, 25, 180)
    circle2(t, 25, 120)
    t.penup()
    t.rt(60)
    t.fd(75)
    t.lt(90)
    t.fd(50)
    t.pendown()

def letter_T(t):
    t.lt(90)
    t.fd(100)
    t.rt(90)
    t.fd(50)
    t.penup()
    t.bk(50)
    t.pendown()
    t.bk(50)
    t.penup()
    t.fd(50)
    t.rt(90)
    t.fd(100)
    t.lt(90)
    t.fd(100)
    t.pendown()

def letter_F(t):
    t.lt(90)
    t.fd(70)
    t.rt(90)
    t.fd(40)
    t.penup()
    t.bk(40)
    t.lt(90)
    t.pendown()
    t.fd(30)
    t.rt(90)
    t.fd(40)
    t.penup()
    t.bk(40)
    t.rt(90)
    t.fd(100)
    t.lt(90)
    t.fd(125)
    t.pendown()

def letter_w(t):
    t.pendown()
    t.lt(120)
    t.fd(100)
    t.penup()
    t.bk(100)
    t.rt(60)
    t.pendown()
    t.fd(100)
    t.rt(120)
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.penup()
    t.bk(100)
    t.rt(60)
    t.fd(75)
    t.pendown()

def letter_n(t):
    t.penup()
    t.fd(50)
    t.pendown()
    t.lt(90)
    t.fd(65)
    def circle(t, radius, angle):
        circumference = 2 * math.pi * radius
        sides = 100
        length = circumference / sides
        steps = int(sides * angle / 360)
        t.rt(360)
        t.pendown()
        for _ in range(steps):
            t.forward(length)
            t.left(angle / steps)
    circle(bob, 35, 180)
    t.fd(65)
    t.penup()
    t.lt(90)
    t.fd(150)
    t.pendown()

def letter_C(t):
    t.penup()
    t.bk(50)
    t.pendown()
    t.circle(50, 180)
    t.penup()
    t.lt(90)
    t.fd(100)
    t.rt(90)
    t.fd(150)
    t.pendown()

def letter_E(t):
    t.lt(90)
    t.fd(100)
    t.rt(90)
    t.fd(50)
    t.penup()
    t.bk(50)
    t.rt(90)
    t.fd(50)
    t.lt(90)
    t.pendown()
    t.fd(30)
    t.penup()
    t.bk(30)
    t.rt(90)
    t.fd(50)
    t.lt(90)
    t.pendown()
    t.fd(50)
    t.penup()
    t.bk(50)
    t.rt(90)
    t.fd(100)
    t.lt(90)
    t.fd(150)
    t.pendown()

def letter_G(t):
    t.penup()
    t.bk(50)
    t.pendown()
    t.circle(50, 270)
    t.penup()
    t.lt(90)
    t.fd(25)
    t.lt(90)
    t.pendown()
    t.fd(25)
    t.penup()
    t.bk(25)
    t.rt(90)
    t.bk(25)
    t.rt(90)
    t.fd(50)
    t.rt(90)
    t.fd(75)
    t.pendown()

def letter_J(t):
    t.penup()
    t.bk(25)
    t.lt(90)
    t.pendown()
    t.fd(100)
    t.lt(90)
    t.circle(25, 180)
    t.penup()
    t.fd(50)
    t.rt(90)
    t.fd(100)
    t.rt(90)
    t.fd(100)
    t.pendown()

def letter_Q(t):
    def circle(t, radius):
        circumference = 2 * math.pi * radius
        sides = 100
        length = circumference / sides
        for i in range(sides):
            t.forward(length)
            t.lt(360/sides)
    circle(t, 50)
    t.penup()
    t.goto(bob.xcor() - 15, bob.ycor() - 15)
    t.pendown()
    t.rt(45)
    t.fd(20)
    t.penup()
    t.goto(bob.xcor() + 65, bob.ycor() + 50)
    t.pendown()

def letter_U(t):
    t.penup()
    t.bk(50)
    t.rt(90)
    t.pendown()
    t.fd(75)
    t.circle(50, 180)
    t.fd(75)
    t.penup()
    t.lt(90)
    t.fd(150)
    t.pendown()

def letter_X(t):
    t.penup()
    t.lt(45)
    t.pendown()
    t.fd(100)
    t.penup()
    t.bk(50)
    t.rt(90)
    t.pendown()
    t.fd(50)
    t.penup()
    t.bk(100)
    t.lt(45)
    t.fd(100)
    t.pendown()

def letter_Y(t):
    t.penup()
    t.lt(45)
    t.pendown()
    t.fd(50)
    t.lt(90)
    t.fd(50)
    t.penup()
    t.bk(50)
    t.rt(90)
    t.pendown()
    t.fd(50)
    t.penup()
    t.bk(50)
    t.rt(90)
    t.fd(50)
    t.lt(90)
    t.fd(75)
    t.pendown()

letter_J(bob)
letter_A(bob)
letter_n(bob)

letter_A(bob)


turtle.mainloop()
