# 求圆的面积
r = 25
area = 3.14 * r * r
print(area)
print("{:.2f}".format(area))

# 绘制多个同切圆
import turtle

turtle.pensize(2) #线的粗细

# 圆的大小
turtle.circle(10)
turtle.circle(40)
turtle.circle(80)
turtle.circle(160)

# 绘制一个五角星
from turtle import *

color('red', 'red') # 线的颜色 填充的颜色
begin_fill()
for i in range(5):
    fd(200) # 五角星的大小
    rt(144)
end_fill()
done()
