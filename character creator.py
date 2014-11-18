#Made by Tyler Kapusniak
#Date: 11/18/2014
#make random
import random
#make stats list
STATS = []
#get attributes
attributes = ("STR", "DEX", "CON", "INT", "WIS", "CHA")
#make for loop to add the dice rolls
for dice in range(len(attributes)):
    total = 0
    for roll in range(1,3):
        total += random.randint(1,6)
    STATS.append(total)
#print the attributes
for i in range(len(STATS)):
    print(attributes[i], ":", STATS[i])
