import turtle as t
import random
import time
import wordcloud

in_name_c = input("我们很想知道你的名字啊, 请问你是谁: ")
in_name_e = input("英文名: ")
print(in_name_c + ", 你好, 画圣诞树的时间大概要在三分钟左右, 请稍等! 你可以一边听歌一边欣赏我的表演! 嘻嘻~")
print("start！")
tim = time.perf_counter()
n = 80.0
t.setup(800, 600)
t.speed("fastest")
t.screensize(bg='seashell')
t.left(90)
t.forward(3 * n)
t.color("orange", "yellow")
t.begin_fill()
t.left(126)

for i in range(5):
    t.forward(n / 5)
    t.right(144)
    t.forward(n / 5)
    t.left(72)
t.end_fill()
t.right(126)

t.color("dark green")
t.backward(n * 4.8)

print("我要开始画树了. ")


def tree(d, s):
    if (d <= 0):
        return
    t.forward(s)
    tree(d - 1, s * .8)
    t.right(120)
    tree(d - 3, s * .5)
    t.right(120)
    tree(d - 3, s * .5)
    t.right(120)
    t.backward(s)


tree(15, n)
t.backward(n / 2)

print("树画完了, 咱们再来装饰一下吧!!")

for i in range(200):
    a = 200 - 400 * random.random()
    b = 10 - 20 * random.random()
    t.up()
    t.forward(b)
    t.left(90)
    t.forward(a)
    t.down()
    if (random.randint(0, 1)) == 0:
        t.color('tomato')
    else:
        t.color('wheat')
    t.circle(2)
    t.up()
    t.backward(a)
    t.right(90)
    t.backward(b)
    if (i == 100):
        print("就快完成了, 来都来了, 可别半途而废啊!!")
time.sleep(30)
tim2 = time.perf_counter()
print("大功告成!! 树只会停留30秒哦, 如果想留念的话可以截个屏哦! 而且不要关闭, 等30s之后会有惊喜的哦~")

print("画图用时: ", end='')
print(tim2 - tim)

print(in_name_c + " Merry Christmas")
print("end!! 感谢观看!")
print("备注: 因为贺卡的代码在打包的时候出现了错误, 所以以后修改过来的时候再发, 要是有想要的就找我吧")
t.done()

red = random.randint(0, 255)
green = random.randint(0, 255)
blue = random.randint(0, 255)

w = wordcloud.WordCloud(background_color=(red, green, blue))
w.generate(in_name_e + " Merry Christmas")
print("亲爱的" + in_name_c + "我们为你生成了一个专属于你的圣诞贺卡, 请查收. 文件名为: " + in_name_c + ".png")
w.to_file(str(in_name_c) + ".png")
