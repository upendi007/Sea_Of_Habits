import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from habit import Habit
from datetime import datetime, timedelta

def test_habit_creation():
    """Tests if a Habit object is initialized correctly."""
    habit = Habit(name="Test Name", description="Test Desc", periodicity="daily")
    assert habit.name == "Test Name"
    assert habit.periodicity == "daily"
    assert habit.check_offs == []

def test_check_off_adds_timestamp():
    """Tests if the check_off method adds a timestamp to the list."""
    habit = Habit("Test Checkoff", "Test Desc", "daily")
    assert len(habit.check_offs) == 0  
    habit.check_off()
    assert len(habit.check_offs) == 1 

def test_current_streak_simple_case():
    """Tests calculating a simple, unbroken streak."""
    habit = Habit("Daily Run", "Run 5k", "daily")
    today = datetime.now()
    
    habit.check_offs = [
        today - timedelta(days=1),
        today - timedelta(days=2),
        today - timedelta(days=3)
    ]
    
    assert habit.calculate_current_streak() == 3

def test_current_streak_with_a_break():
    """Tests that the streak is correctly broken after a missed day."""
    habit = Habit("Daily Meditation", "Meditate 10m", "daily")
    today = datetime.now()
    
    habit.check_offs = [
        today - timedelta(days=1),  
        today - timedelta(days=3)
    ]
    
    assert habit.calculate_current_streak() == 1

def test_calculate_longest_streak_simple():
    habit = Habit("Daily Meditation", "Meditate 10m", "daily")
    today = datetime.now()

    habit.check_offs = [
        today - timedelta(days=1),
        today - timedelta(days=2)
    ]
    longest_streak = habit.calculate_longest_streak()
    assert longest_streak == 2

def test_calculate_longest_streak_with_multiple_streaks():
    habit = Habit("Daily Meditation", "Meditate 10m", "daily")
    today = datetime.now()

    habit.check_offs = [
        today - timedelta(days=1),
        today - timedelta(days=2),
        today - timedelta(days=5),
        today - timedelta(days=6),
        today - timedelta(days=7),
        today - timedelta(days=8),
    ]
    longest_streak = habit.calculate_longest_streak()
    assert longest_streak == 4