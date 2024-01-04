from turtle import *


def segments(sz):
    lst_segments = [60, 180, 120, 180, 120, 180]
    for i in lst_segments:
        left(i)
        forward(sz * 0.3)
    left(60)
    forward(sz)


def snowflake(sz, sh):
    clear()
    showturtle()
    speed(10)
    color('blue')
    pensize(3)
    n = 0
    while True:
        if n == sh:
            break
        else:
            forward(sz)
            segments(sz)
            left(180)
            left(360 / sh)
            n += 1
    hideturtle()
