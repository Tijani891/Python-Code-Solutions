
import random
names = "Angela, Ben, Jenny, Micheal, Chloe"

name = names.split(", ")

random_number = random.randint(0,(len(name)-1))


print(f"{name[random_number]} is going to buy dinner today. ")
