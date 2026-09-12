# Expense Tracker CLI

A simple command-line application to track daily expenses, built with Python.
Add expenses, view them by category, and keep persistent records using JSON storage.

## Features

- Add new expenses with amount, category, and note
- View all recorded expenses
- Delete an expense by its list number
- View category-wise totals (category names are normalized, so "food" and "Food" are treated the same)
- Data automatically saved to a local JSON file
- Basic input validation (handles invalid number entries gracefully)

## Tech Stack

- Python 3
- Built-in json and os modules (no external dependencies)

## How to Run

1. Clone this repository
  
   git clone https://github.com/Omi-code404/expense-tracker-cli.git
   cd expense-tracker-cli
   
2. Run the program
  
   python main.py
   
3. Follow the on-screen menu:
  
   1. Add Expense
   2. View All
   3. Delete Expense
   4. Show Total
   5. Exit
   
## Example Usage

Choose: 1
Enter the amount: 200
Enter the category: Food
Enter a note (optional): Lunch
Expense added successfully.

Choose: 4
Food: 200.0
## Project Structure

expense-tracker-cli/
├── main.py          # Main application logic
├── .gitignore        # Excludes personal data from version control
└── README.md
## What I Learned

- File handling and persistent storage using JSON
- Writing modular functions (load, save, add, view, delete, totals)
- Handling user input errors with try/except
- Rebuilding a list in place using slice assignment (expenses[:] = new_expenses)
- Aggregating values with a dictionary using .get(key, default)
- Normalizing text input (.strip().title()) to avoid case-sensitivity bugs
- Using Git and GitHub for version control

## Future Improvements

- Edit an existing expense
- Filter expenses by date or category
- Export totals to a report

## Author

Amlan — B.Sc Applied Mathematics student