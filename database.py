import json
from datetime import datetime
from habit import Habit

def save_habits(habits, filepath="habits.json"):
    """Converts a list of Habit objects to dictionaries and saves them to a JSON file."""
    data_to_save = []
    for habit in habits:
        habit_dict = {
            "name": habit.name,
            "description": habit.description,
            "periodicity": habit.periodicity,
            "creationdate": habit.creationdate.isoformat(),
            "check_offs": [check_off.isoformat() for check_off in habit.check_offs]
        }
        data_to_save.append(habit_dict)

    with open(filepath, "w") as file:
        json.dump(data_to_save, file, indent=4)

def load_habits(filepath="habits.json"):
    """Loads habits from a JSON file and converts them back into a list of Habit objects."""
    try:
        with open(filepath, "r") as file:
            data_from_file = json.load(file)
    except FileNotFoundError:
        return []

    habits_objects = []
    for habit_dict in data_from_file:
        new_habit = Habit(
            name=habit_dict["name"],
            description=habit_dict["description"],
            periodicity=habit_dict["periodicity"]
        )
        new_habit.creationdate = datetime.fromisoformat(habit_dict["creationdate"])
        new_habit.check_offs = [datetime.fromisoformat(date_str) for date_str in habit_dict["check_offs"]]
        
        habits_objects.append(new_habit)
        
    return habits_objects