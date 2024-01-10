from turtle import *


def text_new_year(name):
    left(180)
    up()
    forward(200)
    right(90)
    forward(100)
    color('red')
    write(f'С Новым годом, {name}! Забирай подарки!', font=('Times New Roman', 20, 'normal'))

    right(180)
    forward(100)


def box():
    down()
    begin_fill()

    stop = 0
    while True:
        if stop == 4:
            break
        else:
            forward(80)
            left(90)
            stop += 1
    end_fill()


def bow():
    stop = 0
    begin_fill()
    while True:
        if stop == 3:
            end_fill()
            break
        else:
            forward(40)
            right(360 / 3)
            stop += 1


def count_gift(gift):
    up()
    right(150)
    forward(100)
    right(90)
    forward(60)
    write(f'x  {gift}', font=('Times New Roman', 30, 'normal'))


def main(main_name, main_gift):
    speed(10)
    showturtle()
    clear()

    text_new_year(main_name)
    box()

    begin_fill()
    left(90)
    forward(30)
    right(90)
    color('green')
    forward(80)
    left(90)
    forward(20)
    left(90)
    forward(80)
    end_fill()

    bow()
    left(90)
    forward(20)
    right(30)
    bow()

    count_gift(main_gift)
    hideturtle()
    home()
