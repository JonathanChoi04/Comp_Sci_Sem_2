import random
restlist = ["In n out", "Mc Donalds", "Habbit"]
InnoutMenu = ["Cheese burger", "Double-Double", "Animal Fries"]
McDonaldsMenu = ["Chicken nugget", "Morning Delux", "Hash Brown"]
HabbitMenu = ["Terriyaki Burger", "Fried Onions", "Cheese burger"]
user = input("Choose a restraunt: " + restlist) 
if user == "In n out"
    print(InnoutMenu)
    print(InnoutMenu[random.randrange(0,3)])
elif user == "Mc Donalds"
    print(McDonaldsMenu)
    print(McDonaldsMenu[random.randrange(0,3)])
elif user == "Habbit"
    print(HabbitMenu)
    print(HabbitMenu[random.randrange(0,3)])