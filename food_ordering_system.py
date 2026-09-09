foods = ["Burger","Pizza","Pasta","Fries","Coke"]
prices = [120,200,150,80,50]
print("----MENU----")
for food in foods:
    print(food + ":" + str(prices[foods.index(food)]))