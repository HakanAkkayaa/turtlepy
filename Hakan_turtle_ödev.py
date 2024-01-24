import turtle

kalem=turtle.Turtle()
kalem.pensize(2)
kalem.speed(50)

kalem.color("silver")
# H Harfi #
kalem.penup() 
kalem.goto(-425,-50)
kalem.pendown()


kalem.left(90)
for i in range(15):
    kalem.forward(10)
    kalem.circle(10)

kalem.penup() 
kalem.goto(-425,25)
kalem.pendown()

kalem.right(90)
for i in range(5):
    kalem.forward(10)
    kalem.circle(10)

kalem.penup() 
kalem.goto(-365,110)
kalem.pendown()

kalem.left(270)
for i in range(15):
    kalem.forward(10)
    kalem.circle(10)

kalem.color("purple")
# A Harfi # 
kalem.penup() 
kalem.goto(-260,100)
kalem.pendown()

kalem.left(25)
for i in range(16):
    kalem.forward(10)
    kalem.circle(10)

kalem.penup() 
kalem.goto(-260,100)
kalem.pendown()

kalem.right(50)
for i in range(15):
    kalem.forward(10)
    kalem.circle(10)

kalem.penup() 
kalem.goto(-280,5)
kalem.pendown()

kalem.left(115)
for i in range(6):
    kalem.forward(10)
    kalem.circle(10)

kalem.color("black")
# K Harfi #
kalem.penup() 
kalem.goto(-130,-50)
kalem.pendown()

kalem.left(90)
for i in range(15):
    kalem.forward(10)
    kalem.circle(10)

kalem.penup() 
kalem.goto(-50,105)
kalem.pendown()

kalem.left(135)
for i in range(11):
    kalem.forward(10)
    kalem.circle(10)

kalem.left(90)
for i in range(10):
    kalem.forward(10)
    kalem.circle(10)

kalem.color("gray")
# A Harfi #
kalem.penup() 
kalem.goto(55,100)
kalem.pendown()

kalem.right(20)
for i in range(16):
    kalem.forward(10)
    kalem.circle(10)

kalem.penup() 
kalem.goto(55,100)
kalem.pendown()

kalem.right(50)
for i in range(15):
    kalem.forward(10)
    kalem.circle(10)

kalem.penup() 
kalem.goto(30,5)
kalem.pendown()

kalem.left(115)
for i in range(6):
    kalem.forward(10)
    kalem.circle(10)

kalem.color("brown")
# N Harfi # 
kalem.penup() 
kalem.goto(195,-50)
kalem.pendown()

kalem.left(90)
for i in range(16):
    kalem.forward(10)
    kalem.circle(10)

kalem.penup() 
kalem.goto(190,112)
kalem.pendown()    

kalem.right(155)    
for i in range(17):
    kalem.forward(10)
    kalem.circle(10)

kalem.penup() 
kalem.goto(275,114)
kalem.pendown() 

kalem.left(335)
for i in range(16):
    kalem.forward(10)
    kalem.circle(10)


turtle.done()