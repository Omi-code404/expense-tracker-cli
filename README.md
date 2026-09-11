# Expense Tracker CLI

A simple command-line application to track daily expenses, built with Python.
Add expenses, view them by category, and keep persistent records using JSON storage.

## Features

- Add new expenses with amount, category, and note
- View all recorded expenses
- Data automatically saved to a local JSON file
- Basic input validation (handles invalid number entries gracefully)

## Tech Stack

- Python 3
- Built-in `json` and `os` modules (no external dependencies)

## How to Run

1. Clone this repository
   ```
   git clone https://github.com/Omi-code404/expense-tracker-cli.git
   cd expense-tracker-cli
   ```

2. Run the program
   ```
   python main.py
   ```

3. Follow the on-screen menu:
   ```
   1. Add Expense
   2. View All
   3. Exit
   ```

## Project Structure

```
expense-tracker-cli/
├── main.py          
├── .gitignore        
 version control
└── README.md
```

## What I Learned

- File handling and persistent storage using JSON
- Writing modular functions (load, save, add, view)
- Handling user input errors with try/except
- Using Git and GitHub for version control

## Future Improvements

- Delete individual expenses
- Filter expenses by date or category
- Export totals to a report

## Author

Amlan — B.Sc Applied Mathematics student