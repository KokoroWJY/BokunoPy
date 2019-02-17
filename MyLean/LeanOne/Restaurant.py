class Restaurant():

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print("本店的视频名字有: " + str(self.name))
        print("本店的风格是: " + str(self.type))

    def open_restaurant(self):
        print("本店现在营业中.")


restaurant = Restaurant("Virus", "西餐厅")

restaurant.describe_restaurant()
restaurant.open_restaurant()


class User():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(str(self.first_name).title() + " " + str(self.last_name.title()))


Virus = User("w", "jy")

Virus.describe_user()