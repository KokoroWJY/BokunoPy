# 徐
import turtle as t

t.setup(800, 600, 0, 0)
t.pencolor("black")
t.width(10)
#第一笔
t.pu()
t.goto(-260, 250)
t.pd()
t.right(90)
t.circle(-150, 50)
#第二笔
t.pu()
t.circle(-150, 330)
t.goto(-250, 150)
t.pd()
t.circle(-150, 50)
#第三笔
t.pu()
t.circle(-150, 290)
t.goto(-280, 85)
t.pd()
t.fd(180)
#第四笔
t.pu()
t.goto(-130, 250)
t.right(10)
t.pd()
t.circle(-270, 40)
#第五笔
t.pu()
t.left(10)
t.left(30)
t.circle(-270, 320)
t.goto(-130, 230)
t.pd()
t.circle(280, 40)
#第六笔
t.pu()
t.circle(280, 320)
t.left(60) #返回水平面朝x正方向
t.left(5)
t.goto(-180, 85)
t.pd()
t.fd(120)
#第七笔
t.pu()
t.goto(-200, 20)
t.pd()
t.fd(200)
# 第八笔(竖)
t.pu()
t.right(95) #返回竖直面向 y负方向
t.goto(-120, 88)
t.pd()
t.fd(180)
# 第八笔(勾)
t.pu()
t.left(-120)
t.pd()
t.fd(35)
# 第九笔
t.pu()
t.left(50)
t.goto(-200, -10)
t.pd()
t.left(20)
t.circle(280, 10)
#第十笔
t.pu()
t.circle(280, 350)
t.left(110)
t.goto(-50, -10)
t.pd()
t.circle(-220, 15)

t.done()