# Standard library imports.
import os
import sys
# Local library imports.
from habit import Habit
from database import save_habits, load_habits
from game import get_animal_streak

# List of predefined habits for user to choose from.
PREDEFINED_HABITS = [
    {
        "name": "Drink Water",
        "description": "Drink at least 8 glasses of water.",
        "periodicity": "daily"
    },
    {
        "name": "Read a Book",
        "description": "Read for at least 15 minutes.",
        "periodicity": "daily"
    },
    {
        "name": "Workout",
        "description": "Do any physical exercise (e.g., gym, running, yoga).",
        "periodicity": "3-day"
    },
    {
        "name": "Weekly Cleaning",
        "description": "Tidy up your living space.",
        "periodicity": "weekly"
    },
    {
        "name": "Learn Python",
        "description": "Spend 30 minutes learning to code.",
        "periodicity": "daily"
    },
    {
        "name": "Meditate",
        "description": "Practice mindfulness for 10 minutes.",
        "periodicity": "daily"
    }
]
""" The main function that runs the application's command-line interface. 
It handles the main loop, user input, and calls other functions."""
def main():
    habits = load_habits()
    # Welcome message for user.
    print("""Sea of Habits
            Welcome to the application that will help you swim in the right direction. In easy and fun way you can keep yourself accountable and as a small gift, after reaching certain points you will get sea-related fun fact. Are you ready to jump in?""")
    # Main loop that guides user thruought the application.
    while True:
        print("""
            Main Menu:
            [1] See you current habits
            [2] Add new habit
            [3] Check the habit
            [4] Statistics
            [5] Close the application. """)
        # Place of input for user.
        choice = input("Choose an option from 1 to 4: ")
        # Display of current habits.
        if choice == '1':
            print("\n--- Your current habits ---")
            
            # Safety option, in case habits were not created yet.
            if not habits: 
                print("You don't have habits yet, add them by selecting option [2].")
            else:
                for habit in habits:
                    print(habit)
            print("-----------------------------\n")
            input("Press enter to come back to menu...")
            # Place to add new habit
        elif choice == '2':
            print("\n--- Add new habit ---")
            print("""
                  Choose one option:
                  1. Predefined Habit
                  2. Your own habit""")
            option = input("Option number: ")
            # Chosing from excisting habits
            if option == "1":
                print("\n--- Predefined Habits ---")
                for idx, habit_info in enumerate(PREDEFINED_HABITS):
                    print(f"[{idx + 1}] {habit_info['name']} - {habit_info['description']}")
                # Assessing which habit user tries to choose.
                choice_str = input("\nEnter the number of the habit you want to add: ")
                try:
                    # Changing string value to integer value.
                    choice_int = int(choice_str)
                    # Assessing if habit exist.
                    if 1 <= choice_int <= len(PREDEFINED_HABITS):
                        selected_habit_info = PREDEFINED_HABITS[choice_int - 1]
                        habit_exists = False
                        for habit in habits:
                            if habit.name == selected_habit_info["name"]:
                                habit_exists = True
                                break
                        # Information for user if they already have habit in their habits list.
                        if habit_exists:
                            print(f"\nError: The habit '{selected_habit_info['name']}' already exists.")
                        # Adding new habit to user list.
                        else:
                            new_habit = Habit(
                                name=selected_habit_info["name"],
                                description=selected_habit_info["description"],
                                periodicity=selected_habit_info["periodicity"]
                            )
                            habits.append(new_habit)
                            save_habits(habits)
                            print(f"\nSuccess! Habit '{new_habit.name}' has been added.")
                    # Return information in case input was invalid.
                    else:
                        print(f"\nError: Invalid number. Please choose a number between 1 and {len(PREDEFINED_HABITS)}.")
                except ValueError:
                    print("\nError: Invalid input. Please enter a number.")
                
                input("\nPress Enter to return to the main menu...")
            # Option of creating habit from zero.
            elif option == "2":
                print("\n--- Create Your Own Habit ---")
                habit_name = input("Enter the name of your new habit: ")
                habit_description = input("Enter a short description: ")
                
                habit_periodicity = None 
                while habit_periodicity is None:
                    print("""
                            Periodicity Options:
                            [1] Daily
                            [2] Weekly
                            [3] Every 3 Days""")
                    periodicity_choice = input("Please choose a periodicity (1-3): ")
                    if periodicity_choice == "1":
                        habit_periodicity = "daily"
                    elif periodicity_choice == "2":
                        habit_periodicity = "weekly"
                    elif periodicity_choice == "3":
                        habit_periodicity = "3-day"
                    else:
                        print("Invalid choice. Please try again.")
                # Making sure two identicall habits are not created.
                habit_exists = False
                for habit in habits:
                    if habit.name.lower() == habit_name.lower(): 
                        habit_exists = True
                        break
                
                if habit_exists:
                    print(f"\nError: A habit named '{habit_name}' already exists.")
                else:
                    new_habit = Habit(
                        name=habit_name,
                        description=habit_description,
                        periodicity=habit_periodicity
                    )
                    habits.append(new_habit)
                    save_habits(habits)
                    print(f"\nSuccess! Habit '{new_habit.name}' has been added.")
                
                input("\nPress Enter to return to the main menu...")
            
            else:
                print("\nInvalid option. Please choose 1 or 2.")
                input("\nPress Enter to return to the main menu...")
        # Part responsible for checking of a habit.
        elif choice == "3":
            print("\n--- Check Off a Habit ---")
            # Assessing if any habit exist. 
            if not habits:
                    print("You don't have any habits yet. Please add a habit first.")
                    input("\nPress Enter to return to the main menu...")
                    continue
            # Choice of habit to check off.
            print("Which habit would you like to check off?")
            # Creates displey of index, habit and current streak for that habit, giving user clear picture of his progress.
            for idx, habit in enumerate(habits):
                    current_streak = habit.calculate_current_streak()
                    print(f"[{idx + 1}] {habit.name} (Current Streak: {current_streak})")
            choice_str = input("\nEnter the number of the habit: ")
            try: 
                # Changing input from string to integer.
                choice_int = int(choice_str)
                # Assessing if correct number is chosen.
                if 1<= choice_int <= len(habits):
                    selected_habit = habits[choice_int - 1]
                    selected_habit.check_off()
                    print(f"\nGreat job! Habit '{selected_habit.name}' has been checked off.")
                    current_streak = selected_habit.calculate_current_streak()
                    print(f"Your current streak for this habit is now: {current_streak}!")
                    animal_info = get_animal_streak(current_streak)
                # Display of game element of application.
                    if animal_info:
                        print("\n*** ACHIEVEMENT UNLOCKED! ***")
                        print(f"You're swimming like a {animal_info[1]}! Fun fact: {animal_info[2]}")
                    save_habits(habits)
                else:
                        print(f"\nError: Invalid number. Please choose a number between 1 and {len(habits)}.")
            except ValueError:
                print("\nPress Enter to return to the main manu...")
        # Displey of user statistics.
        elif choice == "4":
            print("\n--- Statistics ---")
            # Safety measure in case of not existing habits.
            if not habits:
                    print("You don't have any habits yet. Please add a habit first.")
                    input("\nPress Enter to return to the main menu...")
                    continue
            # Displey of option in statistic menu.
            while True:
                print("""Statistic Menu
                      1. Show longest streak overall.
                      2. Show longest streak for choosen habit
                      3. Show all the habits for choosen periodicity
                      4. Go back to main menu""")
                stat_choice = input("Choose an option (1-4): ")
                if stat_choice == "1":
                    # Finding longest streak for a habit.
                    overall_longest_streak = 0
                    habit_with_longest_streak = None 
                    for habit in habits:
                        current_habit_longest_streak = habit.calculate_longest_streak()
                        if current_habit_longest_streak > overall_longest_streak:
                            overall_longest_streak = current_habit_longest_streak
                            habit_with_longest_streak = habit.name 
                    print("\n--- Longest Streak Overall ---")
                    if habit_with_longest_streak:
                        print(f"Your longest streak ever was {overall_longest_streak} periods for the habit: '{habit_with_longest_streak}'!")
                    else:
                        print("Your longest streak overall  is 0.")
                # Displey of longest streak for selected habit.        
                elif stat_choice == "2":
                    for idx, habit in enumerate(habits):
                        print(f"[{idx + 1}] {habit.name}")
                    chosen_habit = input("Choose one of listed habits ")
                    try:
                        chosen_habit = int(chosen_habit)
                        if 1<= chosen_habit <= len(habits):
                            selected_habit = habits[chosen_habit - 1]
                            longest = selected_habit.calculate_longest_streak()
                            print(f"\nThe longest ever streak for '{selected_habit.name}' is {longest} periods.")
                        else:
                            print("Error: Invalid number.")
                    except ValueError:
                        print("Please chose a number")
                # Displey of all habits with chosen perdiocity. 
                elif stat_choice == "3":
                    print("""
                            Periodicity Options:
                            [1] Daily
                            [2] Weekly
                            [3] Every 3 Days""")
                    choice_str = input("Please choose a periodicity (1-3): ")
                    try:
                        choice_int = int(choice_str)
                        habit_in_period = []

                        if choice_int == 1:
                            for habit in habits:
                                if habit.periodicity == "daily":
                                    habit_in_period.append(habit)
                        elif choice_int == 2:
                             for habit in habits:
                                if habit.periodicity == "weekly":
                                    habit_in_period.append(habit)
                        elif choice_int == 3:
                             for habit in habits:
                                if habit.periodicity == "3-day":
                                    habit_in_period.append(habit)
                        else:
                            print("Please enter a number from 1 to 3.")
                        
                        period_str = ""
                        if choice_int == 1: period_str = "daily"
                        elif choice_int == 2: period_str = "weekly"
                        elif choice_int == 3: period_str = "3-day"

                        if period_str:
                            print(f"\n--- Habits with '{period_str}' periodicity ---")
                            if not habit_in_period:
                                print("No habits found with this periodicity.")
                            else:
                                for habit in habit_in_period:
                                    print(f"- {habit.name}")

                    except ValueError:
                        print("Please enter a number from 1 to 3.")
                elif stat_choice == "4":
                    print("\nReturning to the main menu...")
                    break
                else: 
                    print("Please select a number between 1 and 4")
        # Exit from the app.
        elif choice == "5":
            print("SEA you soon")
            sys.exit() 

        else:
            print("\nInvalid option, please try again.")