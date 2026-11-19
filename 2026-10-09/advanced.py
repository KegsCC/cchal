import turtle

win_size = min(turtle.Screen().window_width(), turtle.Screen().window_height()) - 100
t = turtle.Turtle()
t.penup()
t.hideturtle()
t.shape("square")
turtle.tracer(0)

with open("image.rle") as f:
    width = int(next(f))
    key = dict(clr.split(":") for clr in next(f).split(","))
    for pixel, clr in enumerate(sum([[clr]*int(times) for times, clr in zip(*[iter(next(f).split(","))]*2)], [])):
        t.goto(pixel%width*20-win_size/2, pixel//width*-20+win_size/2)
        t.color(key[clr].strip())
        t.stamp()

turtle.done()