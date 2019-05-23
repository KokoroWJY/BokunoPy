# 求圆的面积
r = 25
area = 3.14 * r * r
print(area)
print("{:.2f}".format(area))

# 绘制多个同切圆
import turtle

turtle.pensize(2)  # 线的粗细

# 圆的大小
turtle.circle(10)
turtle.circle(40)
turtle.circle(80)
turtle.circle(160)

# 绘制一个五角星
import turtle as t

t.fillcolor("red")
t.begin_fill()
t.pencolor("red")
t.width(10)

for i in range(5):
    t.fd(280)
    t.right(144)
t.end_fill()
t.done