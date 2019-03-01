try:
    with open('cat_name.txt', 'r', encoding='UTF-8') as cat:
        neko = cat.read()
        print("cat_name.txt 文件的内容是: ")
        print(neko)
    with open('dog_name.txt', 'r', encoding='UTF-8') as dog:
        # emcoding= 将所有的转变为UTF-8的模式
        inu = dog.read()
        print("\ndog_name.txt 文件的内容是: ")
        print(inu)
except:
    print("您输入的文件不正确或不存在")
