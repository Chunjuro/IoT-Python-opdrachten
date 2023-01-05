import turtle# load the turtle module

scrn = turtle.Screen() # Create/obtain the turtle screen object.
t = turtle.Turtle() # Create a turtle object, that we can use to draw. (I named it bob for some reason.)



t.penup()
for x in (-100, 100):
    for y in (-100, 100):
        t.setpos(x, y)
        t.write(t.pos())
t.setpos(-scrn.window_width() / 2 + 10, 0)
t.pendown()
t.setx(scrn.window_width() / 2 - 10)
t.penup()
t.setpos(0, -scrn.window_height() / 2 + 10)
t.pendown()
t.sety(scrn.window_height() / 2 - 10)
t.penup()


turtle.done() # cleanup