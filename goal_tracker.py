# Simple Task & Goal Tracker for CUET Prep
import datetime

tasks=[]

def show_menu():
    print("\n--- CUET & Coding GOAL TRACKER ---")
    print("1. Add a New Goal")
    print("2. View All Goals")
    print("3. Exit")

while True:
    show_menu()
    choice = input("Enter choice(1-3): ")

    if choice == '1':
        goal = input("What is your goal for today? ")
        time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

        tasks.append(f"[{time_stamp}] {goal}")
        print("Goal added successfully!")

    elif choice =='2':
        print("\n--- YOUR CURRENT GOALS ---")
        if not tasks:
            print("No goals set yet. Get to work!")
        for i,t in enumerate(tasks, 1):
            print(f"{i}.{t}")

    elif choice == '3':
        print("Consistency is key. See you tommorow!")
        break
    else:
        print("Invalid choice, try again.")