while True:
    usernameOne = input("请输入第一个数值: ")
    usernameTwo = input("请输入第二个数值: ")
    try:
        username = int(usernameOne)
        usernameTwo = int(usernameTwo)
    except:
        print("抱歉, 你输入的不是数值, 无法解读")
    else:
        print(usernameOne)
        print(usernameTwo)
