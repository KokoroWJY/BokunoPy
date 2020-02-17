# 用户输入
name = input('Tell me something, and I will repeat it back to you: ')
print("Hello, " + name + "!")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name + "!")

age = input("How old are you? ")
age = int(age)
if age > 18:
    print("恭喜你! 你已经是成年人了!")
else:
    print("你还是个孩子!")

car = input("请问你要租赁什么样的车? ")
print("Let me see if I can find you a " + car)

people = input("请问有多少人用餐? ")
people = int(people)
if people > 8:
    print("抱歉, 现在没有空桌子了.")
else:
    print("好的, 请来这坐.")

number = input('请输入一个数字: ')
number = int(number)
if number % 10 == 0:
    print('你输入的数是10的倍数')
else:
    print("你输入的不是10的倍数")

# while 循环
current_number = 1
while current_number <= 5:
    print(current_number, end=' ')
    current_number += 1
print()

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
print("\nThe following users hava been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

responses = {}
while True:
    name = input("Your name: ")
    responses[name] = name
    repeat = input("你是否继续?(yse/no) ")
    if repeat == 'no':
        break

sandwich_orders = ['tuna', 'salmon', 'egg', 'beff', 'vegetables']
finished_sandwiches = []
while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    finished_sandwiches.append(sandwich_order)
    print("I made your " + sandwich_order + " sandwich")

print("Pastrami is over!")
sandwich_orders_other = ['tuna', 'pastrami', 'salmon', 'pastrami', 'egg',
                         'pastrami', 'beff', 'pastrami', 'vegetables']
print("sandwich_orders_other: " + str(sandwich_orders_other))
while "pastrami" in sandwich_orders_other:
    sandwich_orders_other.remove("pastrami")
print("now sandwich_orders_other" + str(sandwich_orders_other))

travel = {}
while True:
    name = input("Place enter your name: ")
    tourist = input("If you could cisit one place in the world, where would you go?"
                    "if you haven't want to place, Place enter no!")
    if tourist == 'no':
        break
    else:
        travel[name] = tourist
