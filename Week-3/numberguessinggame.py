import math
import random
number = random.randint(1,10)
guess = int(input("Guess a number between 1 and 10: "))
correct = "Well done, you guessed correctly!: "
wrong = "Incorrect, try again: "
while True :
    if guess == number:
        print (correct)
        break
    else :
        print (wrong)
        guess = int(input())
