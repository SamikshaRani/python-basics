# Project : CUET & Coding Goal Tracker
# Author : Samiksha Rani 
# Date ; April 25, 2026
# Decription : A script to track study with file persistence.

import datetime

def save_to_file(goal_text):
    # 'a' means Append - it adds to the file instead of overwriting it
    with open("my_goals.txt","a") as file:
        file.write(goal_text+"\n")

def show_menu():
    print("\n--- CUET & CODING GOAL TRACKER ---")
    print("1. Add a New Goal")
    print("2. View All Goals")
    print("3. Exit")

while True:
    show_menu()
    choice = input("Enter choice(1-3): ")

    if choice == '1':
        goal = input("What is your goal for today? ")
        time_stamp = datetime.datetime.now().strftime("%Y-%m-%d , %H:%M")
        entry = f"[{time_stamp}] ,{goal}"

        save_to_file(entry)
        print("Goal saved to my_goals.txt!")

    elif choice == '2':
        print("\n---Your Saved Goals ---")
        try:
            with open("my_goals.txt", "r") as file:
                print(file.read())
        except FileNotFoundError:
            print("No goals saved yet!")

    elif choice == '3':
        break
    else:
        print("Invalid choice, try again")