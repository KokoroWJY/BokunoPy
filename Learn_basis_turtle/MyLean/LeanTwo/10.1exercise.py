pi = 'learning_python.txt'

with open(pi) as piOne:
    a = piOne.read()
    for i in range(3):
        print(a)

print()
with open(pi) as piTwo:
    b = piTwo.readlines()

for i in b:
    print(i)

message = "I really like dog!"
print(message)
print(message.replace('dog', 'cat'))
print()

with open(pi) as piThree:
    print(piThree.read().replace('Python', 'Python and Java'))