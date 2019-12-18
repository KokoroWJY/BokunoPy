import time

scale = 10
print("------执行开始------")
for i in range(scale + 1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i / scale) * 100
    print("{:^3.0f}%[{}->{}]".format(c, a, b))
    time.sleep(2)
print("------执行结束------")

for i in range(101):
    # 光标退回到当前行的行首
    print("\r{:3}%".format(i), end='')
    time.sleep(1)