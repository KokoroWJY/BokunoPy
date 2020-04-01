""" 将散列表用于查找 """

phone_books = dict()  # phone_books = {} 等效
phone_books['jenny'] = 8675309
phone_books['emergency'] = 911

print(phone_books['jenny'])

# 防止重复 (投票 一人仅可以投一次)
voted = {}


def check_voter(name):
    if voted.get(name):
        print("kick them out!")
    else:
        voted[name] = True
        print("let them vote!")


# 将散列表用作缓存
cache = {}


def get_page(url):
    if cache.get(url):
        return cache[url]
    else:
        data = get_data_from_server(url)  # 从服务器获取的信息
        cache[url] = data
        return data


def main():
    check_voter('tom')
    check_voter('mike')
    check_voter('mike')


if __name__ == '__main__':
    main()
