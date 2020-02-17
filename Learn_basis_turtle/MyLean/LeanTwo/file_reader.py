a = 'pi_digits.txt'

with open(a) as file_object:
    """读取整个文件"""
    for line in file_object:
        print(line)

with open(a) as file_object:
    print(file_object.read())
    print()
    print(file_object.read().rstrip())
