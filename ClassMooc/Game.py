#测试
favorite_language = "  python  "
print(favorite_language)
print(favorite_language.rstrip()) # rstrip 去掉最后的空白
print(favorite_language.lstrip()) # lstrip 去掉前面的空白
print(favorite_language.strip()) #去掉两端空格

name = input("Plase tell me your name :")
print("Hello " + name + ", would you like to learn some Python today?")

print(name.lower()) # 全部小写输出
print(name.upper()) # 全部大写输出
print(name.title()) # 首字母大写输出