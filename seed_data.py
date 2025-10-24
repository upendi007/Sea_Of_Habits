import random
from datetime import datetime, timedelta
from habit import Habit
from database import save_habits

def generate_history(habit, weeks=4, success_rate=0.8):
    """
    Generates random check-off history for a habit over a given number of weeks.
    Args:
        habit (Habit): The habit object to add history to.
        weeks (int): Number of weeks to go back in time.
        success_rate (float): Probability (0.0 to 1.0) of checking off the habit on any given day.
    """
    today = datetime.now()
    days_back = weeks * 7

    for i in range(days_back, 0, -1):
        current_date = today - timedelta(days=i)

        if random.random() < success_rate:
            habit.check_offs.append(current_date)


print("Generating sample data...")

habits = [
    Habit("Morning Water", "Drink a glass of water after waking up.", "daily"),
    Habit("Read 15 mins", "Read a book for at least 15 minutes.", "daily"),
    Habit("Gym Workout", "Go to the gym for a full workout.", "3-day"),
    Habit("Yoga Session", "Do a 30-minute yoga session.", "weekly"),
    Habit("Code Practice", "Solve one coding problem.", "daily")
]

generate_history(habits[0], success_rate=0.95)

generate_history(habits[1], success_rate=0.8)

generate_history(habits[2], success_rate=0.6)

today = datetime.now()
habits[3].check_offs = [
    today - timedelta(days=3),   
    today - timedelta(days=10),  
    today - timedelta(days=17),  
    today - timedelta(days=24)   
]

generate_history(habits[4], success_rate=0.4)

save_habits(habits)

print("Success! 'habits.json' has been created with 5 sample habits and 4 weeks of history.")