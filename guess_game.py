import random
def play_game():
    number = random.randint(1, 50)
    print("You have five attempts to guess the number.")

    attempts=0
    while attempts < 5:
        guess = int(input("Guess number (1-50): "))

        if guess < 1 or guess > 50:
            print("Invalid input! Enter between 1 and 50.")
            continue
        attempts += 1

        if guess == number:
            print("Correct! You won in", attempts, "attempts.")
            break
        else:
            if abs(guess - number) <= 5:
                print("Very close!")
            elif guess > number:
                print("Too high!")
            else:
                print("Too low!")

    if attempts == 5 and guess != number:
        print("Game Over! The number was", number)

    choice = input("Do you want to play the guessing game again? (yes/no): ")
    if choice.lower() == "yes":
        play_game()
    else:
        print("Thanks for playing! Goodbye!")
play_game()