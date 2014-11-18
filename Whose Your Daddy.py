#Created by Tyler Kapusniak
#Created on: 11/12/14
import random
#Create list
dads = ["John", "Dave", "Bob"]
grandpas = ["Jake", "Barney", "Link"]
#input statement
my_dad_is = input("Whose Your Daddy? (Enter your name) ")
#if statement
if my_dad_is != "":
    print(random.choice(dads))
else:
    print("Ok, bye.")
my_grandpa_is = input("Want to know who your Grandpa is? (Enter your name) ")
if my_grandpa_is != "":
    print(random.choice(grandpas))
    
