# Expense Tracker System

## Overview

The Expense Tracker System is a GUI-based desktop application developed in Python using Tkinter.  
It allows users to manage personal expenses by adding, deleting, filtering by category, and viewing expense summaries with total calculations by category.

This project demonstrates Python's dynamic typing, dictionary-based data storage, and event-driven GUI design.

---

## Features

- Add expenses with:
  - Date
  - Amount
  - Category
  - Description

- Delete selected expenses from the list

- Filter expenses by category:
  - Food
  - Transport
  - Entertainment
  - Bills
  - Shopping
  - Other

- View all expenses in a sortable table

- Display total expenses and breakdown by category

- Data persistence using JSON storage

- Error handling for:
  - Invalid amounts
  - Empty fields
  - Incorrect input formats

---

## Project Structure

```text
python-app/
└── src/
    ├── main.py          # Main application with ExpenseTracker class and GUI
    ├── expenses.json    # Auto-generated file for data persistence
    └── README.md        # Project documentation
```

---

## Requirements

To run this project, the following is required:

- Python 3.8 or higher
- Tkinter (included with standard Python installation)

Recommended IDEs:
- Visual Studio Code
- PyCharm

No additional libraries or installations are required.

---

## Running the Application

1. Open the project folder in your IDE or terminal.
2. Navigate to the `python-app/src` directory.
3. Run the application using:

```bash
python main.py
```

Once executed, the Expense Tracker graphical interface will open.

---

## How to Use

### Add an Expense

1. Enter the expense date  
   - Or leave the auto-filled current date
2. Enter the amount
3. Select a category from the dropdown
4. Enter a description
5. Click **Add Expense**

---

### Delete an Expense

1. Select an expense from the table
2. Click **Delete Selected**

---

### Filter Expenses

1. Select a category from the **Filter by Category** dropdown
2. Click **Apply Filter**

---

### Show All Expenses

Click **Show All** to clear filters and display every expense.

---

### View Totals

The bottom section of the application automatically displays:

- Total expenses
- Expense totals grouped by category

---

## Python Concepts Used

This project demonstrates several core Python concepts:

- Dynamic typing
- Dictionaries for storing expense records
- Lists for managing collections of data
- JSON module for data persistence
- `datetime` module for handling dates
- Exception handling using `try/except`
- Event-driven programming
- GUI development with Tkinter and ttk widgets

---

## Data Persistence

- Expense data is automatically saved to `expenses.json`
- Data is saved after every:
  - Add operation
  - Delete operation

If `expenses.json` does not exist, the program starts with an empty expense list.

---

## Error Handling

The application validates user input and displays warning messages for:

- Non-numeric amounts
- Empty fields
- Invalid input values

This helps maintain accurate and reliable expense records.

---

## Notes

- All Python files should remain in the same directory for proper execution.
- The application automatically creates `expenses.json` when needed.
- Tkinter is included with Python and does not require separate installation.

---

## Technologies Used

- Python
- Tkinter
- ttk Widgets
- JSON

---

## Author

Developed as part of a Programming Languages course assignment.

**Language:** Python  
*(Paired with Java version by a team member)*

---