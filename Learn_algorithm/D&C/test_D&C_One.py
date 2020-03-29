""" D&C算法 (快速排序) """


# 计算list里面值的和
def sum(list):
    if 0 < len(list):
        sum_ = list[0] + sum(list[1:])
        return sum_
    else:
        return 0


# 递归计算list包含的元素数
def amount(list):
    if list == []:
        return 0
    else:
        return 1 + amount(list[1:])


# 计算最大值
def max(list):
    if len(list) == 0:
        return '无'
    elif len(list) == 1:
        return list[0]
    else:
        if list[0] > list[1]:
            list[1] = list[0]
        return max(list[1:])


if __name__ == '__main__':
    print(sum([1, 2, 3]))
    print(amount([1, 2, 3, 4]))
    print(max([1, 3, 6, 11, 2]))
