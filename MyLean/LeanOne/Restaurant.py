class Restaurant():

    def __init__(self, name, type, number_served=0):
        self.name = name
        self.type = type
        self.number_served = number_served

    def describe_restaurant(self):
        print("本店的视频名字有: " + str(self.name))
        print("本店的风格是: " + str(self.type))

    def open_restaurant(self):
        print("本店现在营业中.")

    def set_number_served(self):
        print("有" + str(self.number_served) + "人来这里就餐")

    def increment_number_served(self, number_served=0):
        self.number_served += number_served


restaurant = Restaurant("Virus", "西餐厅", )

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.set_number_served()

restaurant.increment_number_served(50)
restaurant.set_number_served()

restaurant.increment_number_served(800)
restaurant.set_number_served()


class IceCreamStand(Restaurant):

    def __init__(self, name, type, number_served=0):
        super(IceCreamStand, self).__init__(name, type, number_served)
        self.flavors = ['Strawberry', 'Mango', 'Chocolate', 'Vanilla']

    def printOne(self):
        print(self.flavors)


IceCreamStandOne = IceCreamStand('Viruses', '日式餐厅', )
IceCreamStandOne.printOne()
