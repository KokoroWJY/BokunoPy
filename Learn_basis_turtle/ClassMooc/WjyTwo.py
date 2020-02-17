# 列表切片
players = ['charles', 'martina', 'minchael', 'florence', 'eli']
print(players[0:3])

# 遍历切片
players1 = ['charles', 'martina', 'minchael', 'florence', 'eli']
print('Here ate the first three players on my team: ', end='\t')
for player in players1[:3]:
    print(player.title(), end='\t')

# 复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print('My favorite foods are: ' + str(my_foods))
print("My friend's favorite foods are: " + str(friend_foods))

# 习题
players2 = ['charles', 'martina', 'minchael', 'florence', 'eli']
print("The first three items in the list are:")
print(players2[:3])
print("Three items from the middle of the list are:")
print(players2[1:-2])
print("The last three items in the list are:")
print(players2[-3:])

my_pizzas = ['apple', 'falafel', 'carrot cake']
friend_pizzas = my_pizzas[:]
friend_pizzas.append('ice cream')
print('My favourte pizzas are:')
for my_pizza in my_pizzas:
    print(my_pizza, end=' ')
print('Friend favourite pizzas are:')
for friend_pizza in friend_pizzas:
    print(friend_pizza, end=' ')

'''
元组
元组是值不可以改变的列表
'''
dimensions = (200, 50)
print(dimensions)
# 元组可以直接改变所有的变量
dimensions = (400, 80)
print(dimensions)

# 元组习题
buffet_foodes = ('pizza', 'apple', 'ice cream', 'ijigo', 'suikau')
for buffet_food in buffet_foodes:
    print(buffet_food, end='\t')
print()
new_buffet_foodes = ('pizza', 'banana', 'pine', 'chicken', 'beef')
for new_buffet_food in new_buffet_foodes:
    print(new_buffet_food, end='\t')
print()

alien_coclor = 'green'
if alien_coclor == 'green':
    print('恭喜你! 你获得了5个点')
elif alien_coclor == 'yellow' or 'red':
    print('抱歉! 你没有获得任何点数')

alien_coclor1 = ['red', 'yellow']
if 'red' and 'yellow' in alien_coclor1:
    print('恭喜你! 获得了10个点')
else:
    print('Sorry, you lost!')

'''
确定列表是否为空 若是空列表
if requested_toppings:
不会运行
'''
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding" + requested_topping + ".")
    print("Finished making your pizza!")
else:
    print('Ate you sure you want a plain pizza?')

# 使用多个列表
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print('Adding' + requested_topping + '.')
    else:
        print("Sorry, we don't have" + requested_topping + '.')
print('Finished making your pizza!')

# 习题
usernames = ['admin', 'wjy', 'xbz', 'gyb', 'lw']
if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + username + ", thank you for logging in again")
else:
    print("We need to find some users!")
del usernames[:]
print(usernames)

current_users = ['zzy', 'WJL', 'ZIP', 'XM', 'zjc']

new_new_users = []
new_users = ['zzy', 'HQR', 'Zd', 'WcL']
for new_users in new_users:
    new_new_users.append(new_users.lower())
ina = input('请输入用户名 :')
for new_new_user in range(0):
    if ina in new_new_users:
        input('对不起, 你输入的用户名已被使用!')
    else:
        input('恭喜你, 你的用户名可是使用!')
