# 函数
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
