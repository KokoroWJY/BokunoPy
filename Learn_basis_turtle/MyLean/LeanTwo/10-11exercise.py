import json

file = "digital.josn"


def you_like_digital():
    """如果储存了用户喜欢的数字就获取它"""
    try:
        with open(file) as dig_ital:
            digital = json.load(dig_ital)
    except FileNotFoundError:
        return None
    else:
        return digital


def get_like_digital():
    """获取用户喜欢的数字"""
    like_digital = input('请输入你喜欢的数字: ')
    with open(file, 'w') as digit:
        json.dump(like_digital, digit)
    return like_digital


def Run_like_digital():
    """指出用户喜欢的数字, 若没有就获取用户喜欢的数字"""
    like_digital = you_like_digital()
    if like_digital:
        print("I know your favorite number! It's " + like_digital + '.')
    else:
        like_digital = get_like_digital()
        print("I know your favorite number! It's " + like_digital + '.')


Run_like_digital()