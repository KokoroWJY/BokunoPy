i = input("请输入一个数字")
if len(i) > 1 or len(i) == 0:
    print("你输入的格式不对")
else:
    i_ = i[0]
    if i_.isdigit():
        print("你输入的是数字: " + i_)
    elif i_.isalpha():
        print("你输入的是字母, 他的大写是" + i_.upper())
    else:
        print("你输入的是字符" + i_)