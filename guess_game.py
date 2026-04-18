import random

number=random.randint(1,10)

while True:
    guess=int(input("Guess number (1-10): "))
               
    if guess==number:
        print("Correct!")
        break
    else:
        print("Try again")
