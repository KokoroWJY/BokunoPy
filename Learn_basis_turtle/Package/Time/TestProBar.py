import time

scale = 50
# 字符串.center(,s)类型 将一个s类型填充到两侧
print("执行开始".center(scale // 2, "-"))
start = time.perf_counter() # 开始时间
for i in range(scale + 1):
    a = '*' * i
    b = "." * (scale - i)
    c = (i / scale) * 100
    dur = time.perf_counter() - start # 当前时间-开始时间
    print("\r{:3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur), end=' ')
    time.sleep(0.1)
print("\n" + "执行结束".center(scale // 2, '-'))