import random
def play_game():
    print("\n---Welcome to the Guessing Game!---")
    level = input(" Choose difficulty level (easy, medium, hard): ").lower()
     
    difficulties = {"easy": 10 , "medium": 5 , "hard": 3}
    attempts_allowed = difficulties.get(level, 5)

    if level not in difficulties:
        print("Invalid Input! Defaulting tp medium difficulty.")

    number = random.randint(1, 50)
    print("You have", attempts_allowed , "attempts to guess the number.")

    attempts=0
    won=False

    while attempts < attempts_allowed:
        try:
            guess = int(input("Guess number (1-50): "))
        except ValueError:
            print("Invalid input! Enter a number.")
            continue

        if guess < 1 or guess > 50:
            print("Invalid input! Enter between 1 and 50.")
            continue
        attempts += 1

        if guess == number:
            print("Correct! You won in", attempts, "attempts.")
            won=True
            break
        else:
            if abs(guess - number) <= 5:
                print("Very close!")
            elif guess > number:
                print("Too high!")
            else:
                print("Too low!")

    if not won:
        print("Game Over! The number was", number)

while True:
    play_game()
    while True:
        choice = input("Do you want to play the guessing game again? (yes/no): ").lower()
    
        if choice in [ "yes" , "no"]:
            break
        else:
            print("Please enter only 'yes' or 'no'.")
    if choice == "no":
        print("Thanks for playing! Goodbye!")
        break