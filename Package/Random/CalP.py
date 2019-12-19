# 蒙特卡罗法 计算圆周率

from random import random
from time import perf_counter

darts = 1000 * 1000 # 抛洒点的总数量
hits = 0.0 # 在圆内点的数量
start = perf_counter()
for i in range(1, darts + 1):
    x, y = random(), random()
    dist = pow(x ** 2 + y ** 2, 0.5)
    if dist < 1.0:
        hits += 1
pi = 4 * (hits / darts)
print("圆周率值是: {}".format(pi))
print("运行时间是: {:.5f}s".format(perf_counter() - start))