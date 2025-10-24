# Sea of Habits

## Description
Sea of Habits is a command-line habit tracking application built with Python. It supports users in sticking to their habits by providing a space to create and track them. Additionally, it offers the option to choose from predefined habits. Users can access their current streak, as well as their longest streak.

The application turns boring habit tracking into a game by creating the illusion of swimming through the ocean. Along the way, it provides fun facts about different sea animals when a milestone is reached, turning habit building into an exciting adventure.

## Features
*   View a list of all current habits.
*   Add new habits, either by choosing from a predefined list or creating a custom one.
*   Check off completed habits to track progress.
*   Analyze habits through a statistics menu, including:
    *   Finding the longest streak overall.
    *   Finding the longest streak for a specific habit.
    *   Filtering habits by their periodicity.
*   Gamification system with unlockable achievements.

## Technologies Used
*   Python 3.13
*   Pytest for unit testing

## Setup and Installation
1.  **Clone the repository:**
    ```bash
    git clone <https://github.com/upendi007/Sea_Of_Habits>
    cd Sea-of-Habits
    ```
    (Alternatively, download the project as a ZIP file and unzip it.)

2.  **Create and activate a virtual environment:**
    ```bash
    # Create the environment
    python -m venv venv

    # Activate it (Windows PowerShell)
    .\venv\Scripts\Activate.ps1
    ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage
To run the application, execute the `main.py` script from the root directory of the project. Make sure your virtual environment is activated first.

```bash
python main.py 
```

## Creating Predefined Data

The project includes a script to generate a sample `habits.json` file. This file contains 5 sample habits with a simulated 4-week tracking history, which is required by the project brief for testing and demonstration purposes.

If the `habits.json` file is missing, or if you want to reset the application to its initial sample state, run the following command from the project's root directory:

```bash
python seed_data.py 
```

## Running the Tests

This project uses `pytest` for unit testing. The tests cover the critical logic of the `Habit` class (streak calculation) and the gamification module to ensure their correctness.

To run the full test suite, execute the following command from the project's root directory:

```bash
pytest
```
