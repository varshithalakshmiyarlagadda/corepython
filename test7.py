from turtle import*
def draw four rays(length,radius):
     for i in range(4):
          penup()
          forward(radius)
          pendown()
          forward(length)
          pendown()
          backward(length+radius)
          left(90)
penup()
goto(85,110)
fillcolor("yellow")
pendown()
begin_fill()
circle(45)
end_fill()
penup()
goto(85,169)
pendown()
drawfourrays(85,54)
right(45)
drawfourrays(85,54)
left(45)
done()