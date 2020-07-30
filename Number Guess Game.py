# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 21:16:36 2020

@author: alpjr
""" 

import random
import time 
print("Here are all the numbers!")
number_list = []
for x in range(0, 100):
    number_list.append(x)
print(number_list)

guess = random.choice(number_list)
guessed = True
count = 1
score = 0
print("I got my number!")
question = input("Guess now:")
ending_list = ["BRAVO!!!!","YOU GUESSED IT!","GOOD JOB!","YOU GOT IT"]
while guessed:
    answer = input()
    if answer == "Exit" or answer == "exit":
        guessed = False
    elif int(answer) == guess:
        print(random.choice(ending_list))
        print("Your score = %i"% count)
        time.sleep(4)
        guessed = False
    elif int(answer) > guess:
        print("Down")
        score = score+1
        print("Current score = %i"% score)
        count = count+1
    elif int(answer) < guess:
        print("Up")
        score = score+1
        print("Current score = %i"% score)
        count = count+1
        
   
   