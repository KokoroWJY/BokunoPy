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
