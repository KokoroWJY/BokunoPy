f = open("test.txt")
names = f.readlines()
print(len(names[0]))
a = 0
b = 0
for i in names:
    name = names[b]
    if (len(name) <= 4):
        a = a + 1
    b = b + 1
print(a)