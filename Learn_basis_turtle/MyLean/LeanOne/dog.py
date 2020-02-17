class Dog():
    """一次小狗的简单尝试"""

    def __init__(self, name, age):
        """初始化 name age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令式打滚"""
        print(self.name.title() + " rolled over!")


my_dog = Dog('white', 6)

print("My dong's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

my_dog.sit()
my_dog.roll_over()
