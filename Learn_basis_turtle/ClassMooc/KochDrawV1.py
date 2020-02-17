import turtle


def koch(size, n):
    # 科赫雪花公式
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koch(size / 3, n - 1)


def main():
    # 绘制雪花
    turtle.setup(700, 800)
    turtle.penup()
    turtle.goto(-300, 200)
    turtle.pendown()
    turtle.pensize(2)
    level = 3
    koch(600, level)
    turtle.right(120)
    koch(600, level)
    turtle.right(120)
    koch(600, level)
    turtle.hideturtle()
    turtle.done()

main()
