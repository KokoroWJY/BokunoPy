username = input("请输入用户的名字: ")
with open('guest_book.txt', 'w') as a:
    a.write("欢迎" + username + "你的加入!\n")

while username != '':
    username = input("请输入其他用户输入的名字: ")
    if username != '':
        with open('guest_book.txt', 'a') as user:
            user.write("欢迎" + username + "你的加入!" + "\n")