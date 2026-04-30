# Project : CUET & Coding Goal Tracker
# Author : Samiksha Rani 
# Date ; April 25, 2026
# Decription : A script to track study with file persistence.

import datetime

def save_to_file(category, goal_text):
    # 'a' means Append - it adds to the file instead of overwriting it
    now = datetime.datetime.now().strftime("%Y-%m-%d , %H:%M")
    with open("my_goals.txt","a") as file:
        # This saves it with a Tag like [STUDY] or [CHORE]
        file.write(f"[{now}] [{category.upper()}] {goal_text}\n")

def show_menu():
    print("\n--- CUET & CODING GOAL TRACKER ---")
    print("1. Add a New Goal")
    print("2. View All Goals")
    print("3. Exit")

while True:
    show_menu()
    choice = input("Enter choice(1-3): ")

    if choice == '1':
        print("Categories: 1. Study | 2. Personal")
        cat_choice = input("Select category number: ")
        cat_name = "STUDY" if cat_choice == '1' else "PERSONAL"
        goal = input(f"Enter your {cat_name} goal: ")

        save_to_file(cat_name, goal)
        print("Goal saved successfully!")

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