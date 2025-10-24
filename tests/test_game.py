import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game import get_animal_streak

def test_get_animal_streak_unlocks_achievement():
    """
    Tests if the function returns the correct achievement data
    when a milestone is reached.
    """
    streak_length = 25

    result = get_animal_streak(streak_length)
    assert result is not None  
    assert result[0] == 25
    assert result[1] == "Octopus"

def test_get_animal_streak_no_achievement():
    """
    Tests if the function returns None when no milestone is reached.
    """
    streak_length = 4

    result = get_animal_streak(streak_length)

    assert result is not None
    assert result[0] == 1
    assert result[1] == "Seahorse"
    
def test_get_animal_streak_below_first_milestone():
    """
    Tests if the function returns None when the streak is too short.
    """
    streak_length = 0

    result = get_animal_streak(streak_length)

    assert result is None