# Project : Goal Tracker Pro
# Author : Samiksha Rani 
# Date : May 1, 2026
# Decription : A script to track study with categorization and status updates.

import datetime
import os

def save_to_file(category, goal_text):
    # 'a' means Append - it adds to the file instead of overwriting it
    now = datetime.datetime.now().strftime("%Y-%m-%d , %H:%M")
    with open("my_goals.txt","a") as file:
        # This saves it with a Tag like [STUDY] or [CHORE]
        file.write(f"[{now}] [{category.upper()}] {goal_text}\n")

def mark_goal_done():
    # Checking if the file exists first to prevent a crash
    if not os.path.exists("my_goals.txt"):
        print("\n[!] No goals file found. Add a goal first!")
        return
    
    # 1. Reading evrything first
    with open("my_goals.txt" ,"r") as file:
        lines = file.readlines()

    if not lines or all(line.strip() == "" for line in lines):
        print("\n[!] Your goal list is empty!")
        return
    
    print("\n--- SELECT GOALS TO COMPLETE ---")
    
    # 2. Showing the goals with numbers
    for i, line in enumerate(lines):
        print(f"{i + 1}.{line.strip()}")

    # 3. Picking which one is finished
    try:
        ch = int(input("\nEnter the number of the goal you finished: ")) - 1
        if 0 <= ch < len(lines):
            # Checking if it's already completed to avoid messy text 
            if "[COMPLETED]" in lines[ch]:
                print("\n[!] zthis goal is already marked as completed! ")
            else:
                # Adding a "COMPLETED" tag to that specific line
                lines[ch] = lines[ch].strip() + " [COMPLETED]\n"

                # 4. Saving everything back to the file
                with open("my_goals.txt", "w") as file:
                    file.writelines(lines)
                print("\n[+] Status Updated!")
        else:
            print("Invalid selection.")
    except ValueError:
        print(" Please enter a valid number. ")

def show_menu():
    print("\n"+"="*35)
    print("     MAIN GOAL INTERFACE")
    print("="*35)
    print("1. Add a New Goal")
    print("2. View All Goals")
    print("3. Mark Goal Completed")
    print("4. Exit")
    print("="*35)

# --- MAIN ENGINE ---
while True:
    show_menu()
    choice = input("Select Action(1-4): ")

    if choice == '1':
        print("\nCategories: 1. Study | 2. Personal")
        cat_choice = input("Select category number: ")
        cat_name = "STUDY" if cat_choice == '1' else "PERSONAL"
        goal = input(f"Enter your {cat_name} goal: ")

        save_to_file(cat_name, goal)
        print("\n[+] Goal saved successfully!")

    elif choice == '2':
        print("\n--- Current Logged Goals ---")
        try:
            with open("my_goals.txt", "r") as file:
                content = file.read()
                print(content if content.strip() else "File is empty. ")
        except FileNotFoundError:
            print("No goals saved yet!")

    elif choice == '3':
        mark_goal_done()
    
    elif choice == '4':
        print("\nExiting. Keep pushing your limits dear!")
        break
    else:
        print("\n[!] Invalid choice, please try again")