alien_0 = {'color': 'greem', 'points': '5'}
print(alien_0['color'])
print(alien_0['points'])
print(alien_0)

# 添加 键-值 对
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# 删除 键-值 对
del alien_0['y_position']
print(alien_0)

my_friend_name = {'first_name': 'liu', 'last_name': 'w', 'age': 23, 'city': 'wf'}
print(my_friend_name)

simulation = {'del': '删除', 'title': '首字母大写', 'upper': '字母全部大写',
              'lower': '字母全部小写', 'append': '添加'}
print('del: ' + simulation['del'])
print('title: ' + simulation['title'])
print('upper: ' + simulation['upper'])
print('lower: ' + simulation['lower'])
print('append: ' + simulation['append'])

# 遍历字典 键-值对
user_0 = {'username': 'efermi', 'first': 'enrico', 'last': 'fermi'}
for key, value in user_0.items():
    print('\nKey: ' + key)
    print('Value: ' + value)

print()

# 遍历字典所有的键
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}
for name in favorite_languages.keys():
    print(name.title())
print()
for name in sorted(favorite_languages.keys()):
    print(name.title())
print()

# 遍历字典中的所有值
for language in favorite_languages.values():
    print(language)
print()
# 不重复遍历字典中的所有值
for language in set(favorite_languages.values()):
    print(language)

simulation = {'del': '删除', 'title': '首字母大写', 'upper': '字母全部大写',
              'lower': '字母全部小写', 'append': '添加'}
# 遍历键
for simulation_key in simulation.keys():
    print(simulation_key)
# 遍历值
for simulation_value in simulation.values():
    print(simulation_value)

river = {'egypt': 'nile', 'China': 'haunghe' 'cahngjaing', 'Japen': 'sea of Japan'}
for A, B in river.items():  # A是键 , B是值
    print("The " + B.title() + " runs through " + A.title())

favorite_languagees = ['w', 'a', 'o', 'f', 'ew', 'af', 'agga']
favorite_languagees_agree = {'agree': 'w' 'a' 'f' 'af'}
for a in range(0, 7):
    if favorite_languagees_agree.values() in favorite_languagees:
        print('感谢' + favorite_languagees[a] + '您的到来')
    else:
        print('希望' + favorite_languagees[a] + '您能参加')
