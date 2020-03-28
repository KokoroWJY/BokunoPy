""" 选择排序 """


def findSmallest(arr):
    # 找出数组中最小元素
    smallest = arr[0]  # 储存最小的值
    smallest_index = 0  # 储存最小元素的索引
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    # 对数组进行排序
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


if __name__ == '__main__':
    arr = [5, 3, 6, 2, 10]
    print(selectionSort(arr))
