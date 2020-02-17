# 苗
import turtle as t

t.setup(800, 600, 0, 0)
t.pencolor("black")
t.width(10)
# 第一笔
t.up()
t.goto(-200, 150)
t.pd()
t.fd(300)
# 第二笔
t.pu()
t.goto(-130, 200)
t.right(85)
t.pd()
t.fd(100)
# 第三笔
t.pu()
t.right(10)
t.goto(30, 200)
t.pd()
t.fd(100)
# 第四笔
t.pu()
t.left(5)
t.goto(-170, 50)
t.pd()
t.fd(150)
# 第五笔
t.pu()
t.left(90)
t.goto(-170, 50)
t.pd()
t.fd(240)
# 第六笔
t.pu()
t.right(90)
t.pd()
t.fd(150)
# 第七笔
t.pu()
t.left(90)
t.goto(-170, -25)
t.pd()
t.fd(240)
# 第八笔
t.pu()
t.right(90)
t.goto(-50, 50)
t.pd()
t.fd(150)
# 第九笔
t.pu()
t.left(90)
t.goto(-170, -100)
t.pd()
t.fd(240)

t.done()
