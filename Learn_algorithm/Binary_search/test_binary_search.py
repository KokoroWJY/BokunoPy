""" 二分查找 """


def binary_search(list, item):
    # low, hight用于跟踪其中查找的部分
    low = 0
    hight = len(list) - 1

    while low <= hight:
        mid = int((low + hight) / 2)  # 查找中间元素
        guess = list[mid]

        if guess == item:
            return mid
        elif guess > item:
            hight = mid - 1
        else:
            low = mid + 1

    return None


if __name__ == '__main__':
    my_list = [1, 3, 5, 7, 9]
    print(binary_search(my_list, 3))
    print(binary_search(my_list, -1))
