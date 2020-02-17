a = 3 * 3
b = 3 ** 3
print(a)
print(b)
c = pow(3, 3)
print(c)
print(0.2 + 0.1)
print(3 * 0.1)

age = 19
print("Happy " + str(age) + "rd birthday!")  # str转化为字符串

print(3 / 2)

like = input("你喜欢的一个数 :")
message = "Your like number is " + str(like)
print(message)

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
del bicycles[0]  # del删除某一列表的某位元素
print(bicycles)

names = ["张", "魏", "王"]
print("\n" + names[0] + names[1] + names[2])

print("\n" + names[-1] + "新年快乐!!")
print(names[-2] + "新年快乐!!")
print(names[-3] + "新年快乐!!")

motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
poped_motorcycles = motorcycles.pop()  # pop() 删除列表中的某一元素 但依旧保留它的值
print(motorcycles)
print(poped_motorcycles)

motorcycles1 = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles1)
motorcycles1.remove("ducati")  # remove 删除列表中某一元素 你不用知道此元素的位置 Python会自己找到并删除它
print(motorcycles1)

guest = ["李", "陈", "庞", "郭"]
guest.insert(0, "陶")  # insert() 在列表中的某一位置添加元素 只用输入两个参数即可
print(guest)
guest.insert(2, "朱")
print(guest)
guest.append("徐")  # append() 在列表最后添加一个元素 只用输入一个参数即可
print(guest)
for i in range(4):
    print("在此邀请" + guest[i] + "先生/女士, 参加本次的宴会")

local = ["Japen", "England", "China", "Ganada", "Germany"]
print(local)
print(sorted(local))
print(local)
print(sorted(local, reverse=True))
print(local)
local.reverse()
print(local)
local.reverse()
print(local)
local.sort()
print(local)
local.sort(reverse=True)
print(local)
print("我想去的地方一共有" + str(len(local)) + "个")

pizzas = ['apple', 'banana', 'nut']
for pizza in pizzas:
    print(pizza, end='\t')
print()
for pizza in pizzas:
    print("I like " + pizza + " pizza")
print("I really love pizza!")

animals = ['fish', 'rabbit', 'cat']
for animal in animals:
    print(animal, end='\t')
print()
for animal in animals:
    print("A" + animal + "would make a great pet")
print("Any of these animals would make a great pet!")

listOne = list(range(2, 10, 2))
print(listOne)
print(sum(listOne))  # 对listOne求和
print(max(listOne))  # 找出listOne最大值
print(min(listOne))  # 找出listOne最小值

squares = [value ** 2 for value in range(1, 11)]
print(squares)

for a in range(1, 21):
    print(a, end=" ")

listOne = list(range(1, 1000001))
for b in range(0, 100000):
    print(listOne[b], end=" ")
    if b % 10 == 0:
        print()
print('\n最小的数是: ' + str(min(listOne)))
print('最大的数是: ' + str(max(listOne)))

listTwo = list(range(1, 21, 2))
for Two in range(0, len(listTwo)):
    print(listTwo[Two], end=' ')

listThree = []
a = 3
while a <= 30:
    if a % 3 == 0:
        listThree.append(a)
    a = a + 1
for Three in range(0, len(listThree)):
    print(listThree[Three], end='\t')

print()

listFour = [four ** 3 for four in range(0, 11)]
for Four in range(0, len(listFour)):
    print(listFour[Four], end="\t")
