import random
import time

print('Welcome to the "Guess The Object"game')
word_list = ["Apple", "Soccer Ball","Coffee Cup","IPhone","Book","Car","Video Game","Sneakers","Plane"]
object = random.choice(word_list)
guessed = True
count = 1
print("I have my object!")
print("(Remember that you have to answer has to start with capital letters)")
if object == "Apple":
    print("My object is red and round, it is a fruit.")
elif object == "Soccer Ball":
    print("My object is round and it is used in a sport.")
elif object == "Coffee Cup":
    print("My object is something that holds a liquid which is used in the mornings. And some people are usually addicted to it.")
elif object == "IPhone":
    print("My object is an electronic device. It is made by an electronics company.")
elif object == "Book":
    print("My object is something that has many pages.")
elif object == "Car":
    print("My object is something that moves very fast.")
elif object == "Sneakers":
    print("My object is a piece of clothing. They have rubber soles.")
elif object =="Plane":
    print("My object is a way of transportation. They can move at about 800km/h")
    


question = input("Guess Now:")
ending_list = ["BRAVO!!!!","YOU GUESSED IT!","GOOD JOB!","YOU GOT IT"]
while guessed:
    answer = input()
    if answer == "Exit" or answer == "exit":
        guessed = False
        time.sleep(1)
    elif answer == object:
        print(random.choice(ending_list))
        print("Your Score = %i" % count)
        time.sleep(4)
        guessed = False
    else:
        wrong_list = ["Nope!","Not the right answer!","Try Again"]
        count = count+1
        print(random.choice(wrong_list))
        
        



























