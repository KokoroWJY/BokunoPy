from Restaurant import *

# 第一个类的实例
restaurant = Restaurant("Virus", "西餐厅", )

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.set_number_served()

restaurant.increment_number_served(50)
restaurant.set_number_served()

restaurant.increment_number_served(800)
restaurant.set_number_served()

# 第二个类的实例
IceCreamStandOne = IceCreamStand('Viruses', '日式餐厅', )
IceCreamStandOne.printOne()
