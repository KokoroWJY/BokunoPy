""" 递归调用栈 """


# factorial(x) == x!
# 计算阶乘的递归函数
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


if __name__ == '__main__':
    print(factorial(5))
