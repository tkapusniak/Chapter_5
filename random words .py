#Created by: Tyler Kapusniak
#Created on: 11/14/2014
import random

pick = ["Apple", "Banana", "Cookie", "Durian", "Eggfruit"]

while pick != []:
    choice = (random.choice(pick))
    print(choice)
    pick.remove(choice)
