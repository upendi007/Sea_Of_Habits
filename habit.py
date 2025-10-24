from datetime import datetime, timedelta

class Habit:
    """Represents a single habit with its properties and check-off history."""

    def __init__(self, name: str, description: str, periodicity: str):
        """Initializes a new Habit instance."""
        self.name = name
        self.description = description
        self.periodicity = periodicity
        self.creationdate = datetime.now()
        self.check_offs = []

    def check_off(self):
        """Adds a new check-off timestamp to the habit's history."""
        self.check_offs.append(datetime.now())

    def __str__(self):
        """Returns a user-friendly string representation of the habit."""
        return f"Habit: {self.name} ({self.periodicity})"

    def was_completed_in_period(self, date_to_check: datetime) -> bool:
        """Checks if the habit was completed within the period of a given date."""
        if self.periodicity == "daily":
            for check_off_date in self.check_offs:
                if check_off_date.date() == date_to_check.date():
                    return True
        elif self.periodicity == "weekly":
            target_year, target_week, _ = date_to_check.isocalendar()
            for check_off_date in self.check_offs:
                check_off_year, check_off_week, _ = check_off_date.isocalendar()
                if target_year == check_off_year and target_week == check_off_week:
                    return True
        elif self.periodicity == "3-day":
            end_date = date_to_check.date()
            start_date = end_date - timedelta(days=2)
            for check_off_date in self.check_offs:
                if start_date <= check_off_date.date() <= end_date:
                    return True
        return False

    def calculate_current_streak(self) -> int:
        """Calculates the current, unbroken streak ending today or yesterday."""
        if not self.check_offs:
            return 0
        streak_count = 0
        date_to_check = datetime.now()
        if not self.was_completed_in_period(date_to_check):
            date_to_check -= timedelta(days=1)
        while self.was_completed_in_period(date_to_check):
            streak_count += 1
            if self.periodicity == "daily":
                date_to_check -= timedelta(days=1)
            elif self.periodicity == "weekly":
                date_to_check -= timedelta(days=7)
            elif self.periodicity == "3-day":
                date_to_check -= timedelta(days=3)
        
        return streak_count

    def calculate_longest_streak(self) -> int:
        """Calculates the longest streak in the habit's entire history."""
        if len(self.check_offs) < 2:
            return len(self.check_offs)

        sorted_check_offs = sorted(self.check_offs)

        longest_streak = 1
        current_streak = 1
        
        if self.periodicity == 'daily':
            expected_gap = timedelta(days=1)
        elif self.periodicity == 'weekly':
            expected_gap = timedelta(weeks=1)
        elif self.periodicity == '3-day':
            expected_gap = timedelta(days=3)
        else:
            return 1 
        for i in range(1, len(sorted_check_offs)):
            prev_date = sorted_check_offs[i-1]
            current_date = sorted_check_offs[i]

            if expected_gap * 0.9 <= current_date.date() - prev_date.date() <= expected_gap * 1.1:
                current_streak += 1
            else:
                if current_streak > longest_streak:
                    longest_streak = current_streak
                current_streak = 1
        
        if current_streak > longest_streak:
            longest_streak = current_streak

        return longest_streak