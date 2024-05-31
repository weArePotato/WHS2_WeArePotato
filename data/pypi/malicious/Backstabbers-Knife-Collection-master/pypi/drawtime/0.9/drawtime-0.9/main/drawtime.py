from turtle import *

def sqUp(side):
    for a in range(4):
        fd(side)
        left(90)
def sqDown(side ):
    for a in range(4):
        fd(side)
        left(-90)
def position(x,y):
    goto(x,y)
def le(angle):
    left(angle)
def ri(angle):
    right(angle)
def curvR(length):
    for a in range(length):
        fd(1)
        right(1)
def curvL(length):
    for a in range(length):
        fd(1)
        left(1)
def colorStart(color):
    begin_fill()
    color(color)
def colorEnd():
    end_fill()
def cir(radius):
    circle(radius)
def cirAng(radius,angle):
    circle(radius,angle)
def test():
    import webbrowser
    from time import sleep
    webbrowser.open_new_tab('https://youtube.com/watch?v=dQw4w9WgXcQ&feature=share')
    sleep(5)
    print("you just got rick rolled baby")
