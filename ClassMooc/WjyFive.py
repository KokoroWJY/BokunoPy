#函数
def greet_user():
    """显示简单的问候语"""
    print("Hello")


greet_user()


# username 形参, WJY 实参
def greet_user(username):
    """显示简单的问候语"""
    print("Hello " + username.title() + "!")


greet_user('WJY')


def display_message():
    print("我现在在学习函数")


display_message()


def facorite_book(title):
    print("One of my favorite books is " + title + " in Wonderland.")


facorite_book('Alice')


# # 传递实参
def describe_pet(pet_name, animal_type='cat'):  # 默认 animal_type 为 cat
    """显示宠物信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('kuro')


def make_shirt(size='T', style='I love Python'):
    print("This shirt size is " + size + ". And the style is " + style + ".")


make_shirt(size='xxl', style='blue')


def describe_city(city_name='Beijing', city_country='China'):
    print(city_name.title() + " is in " + city_country.title() + ".")


describe_city('Tokyo', 'Japan')


def get_formatted_name(first_name, last_name, middle_name='', ):
    """返回整洁的名字"""
    if middle_name:
        full_name = first_name + last_name + middle_name
    else:
        full_name = first_name + last_name
    return full_name.title()


musician = get_formatted_name('w', 'jy')
print(musician)


def build_person(first_name, last_name, age):
    """返回一个字典, 其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix', '21')
print(musician)


def city_country(city_name, city_country):
    print(city_country.title() + "," + city_name.title())


city_country('北京', '中国')
city_country('Tokyo', 'Japan')


def make_album(songer_name, song_name, total=''):
    if total:
        print("这位歌手是: " + songer_name + ", 他的专辑是: " + song_name + ", 本专辑有" + total + "张")
    else:
        print("这位歌手是: " + songer_name + ", 他的专辑是: " + song_name + "!")


make_album('张杰', '这,就是爱!', '4')
make_album('邓紫棋', '轮回之间', '')

song_dictionary = {}
def make_album(songer_name, song_name):
    song_dictionary[songer_name] = song_name
    return song_dictionary


while True:
    """a == songer_name"""
    a = input('请输入歌手的名字:(如果想要退出请输入"退出") ')
    a = str(a)
    if a == '退出':
        break
    else:
        """b == song_name"""
        b = input("请输入这位歌手的专辑名字: ")
        b = str(b)
        make_album_true = make_album(a, b)
print(make_album_true)
