# 环境1802
import turtle as t

t.setup(900, 600, 0, 0)
t.width(15)
t.pencolor("green")
t.penup()  # 第一笔
t.goto(-400, 200)
t.pendown()
t.fd(100)
t.pu()  # 第二笔
t.goto(-400, 130)
t.pd()
t.fd(100)
t.pu()  # 第三笔
t.goto(-400, -20)
t.pd()
t.left(35)
t.fd(100)
t.pu()  # 第四笔
t.right(125)
t.goto(-350, 200)
t.pd()
t.fd(170)
t.pu()  # 第五笔
t.goto(-250, 220)
t.left(90)
t.pd()
t.fd(180)
t.pu()  # 第六笔
t.goto(-160, 220)
t.pd()
t.right(90)
t.circle(-150, 80)
t.pu()  # 第七笔
t.circle(-150, 280)
t.goto(-170, 140)
t.pd()
t.fd(180)
t.pu()  # 第八笔
t.goto(-100, 125)
t.pd()
t.left(90)
t.circle(-180, 20)
t.done()
