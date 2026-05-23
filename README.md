# cross-language-group-project# Cross-Language Group Project: Book Cataloging System

## Group Members

- Umama Azhar - Java Implementation
- Bigyan Devkota - Python Implementation

---

## Project Overview

This project implements a Book Cataloging System in two different programming languages: Java and Python.

Both versions provide the same core functionality while demonstrating language-specific features such as:

- Object-oriented programming
- Data structures
- Exception handling
- GUI development
- Event-driven programming

The application allows users to manage a collection of books by:

- Adding books
- Removing books
- Searching books
- Generating reports by genre or author

---

## Repository Structure

```text
cross-language-group-project/
│
├── README.md                          ← Main project overview
│
├── java-app/                          ← Java implementation
│   ├── src/
│   │   ├── Book.java
│   │   ├── BookManager.java
│   │   ├── MainGUI.java
│   │   └── Main.java
│   └── README.md                      ← Java-specific instructions
│
└── python-app/                        ← Python implementation
    └── src/
        ├── main.py                    ← Python application
        └── README.md                  ← Python-specific instructions
```

---

## How to Compile and Run

# Java Version

### Requirements

- JDK 17 or higher

### Compile

```bash
cd java-app/src
javac *.java
```

### Run

```bash
java Main
```

### Alternative (Using IDE)

Open the `java-app` folder in:

- IntelliJ IDEA
- Eclipse
- Visual Studio Code with Java Extension Pack

Run `Main.java`

---

# Python Version

### Requirements

- Python 3.8 or higher
- Tkinter (included with Python)

### Run

```bash
cd python-app/src
python main.py
```

### Alternative (Using IDE)

Open the `python-app/src` folder in:

- PyCharm
- Visual Studio Code

Run `main.py`

No compilation is required for Python.

---

## Features Implemented (Both Languages)

| Feature | Java | Python |
|---|---|---|
| Add books | ✅ | ✅ |
| Remove books | ✅ | ✅ |
| Search by title | ✅ | ✅ |
| Search by author | ✅ | ✅ |
| Search by genre | ✅ | ✅ |
| Display all books | ✅ | ✅ |
| Report by genre | ✅ | ✅ |
| Report by author | ✅ | ✅ |
| GUI interface | Swing | Tkinter |
| Preloaded sample data | ✅ (3 books) | ✅ (3 books) |

---

## Language-Specific Features Demonstrated

# Java (Umama)

- Object-Oriented Programming
- Classes and encapsulation
- `ArrayList` for data storage
- Event-driven GUI with Swing
- Exception handling using `try-catch`
- `toString()` method override

---

# Python (Bigyan)

- Dynamic typing
- Classes and objects
- Lists for data storage
- `__str__()` method
- GUI development with Tkinter and ttk
- Treeview table display
- Exception handling using `try-except`
- List comprehensions for searching and filtering

---

## How to Use the Application

### Add a Book

1. Fill in:
   - Title
   - Author
   - Genre
   - Publication Year
2. Click **Add Book**

---

### Remove a Book

- Select a book from the table and click **Remove Book**
- OR enter the title and click **Remove Book**

---

### Search for Books

Enter a search term and click:

- Search Title
- Search Author
- Search Genre

---

### View All Books

Click **Display All** to view every book in the catalog.

---

### Generate Reports

Click:

- **Report Genre**
- **Report Author**

A report window will display grouped results.

---

## Sample Books (Preloaded)

| Title | Author | Genre | Year |
|---|---|---|---|
| Harry Potter | J.K. Rowling | Fantasy | 1997 |
| 1984 | George Orwell | Dystopian | 1949 |
| Dune | Frank Herbert | Science Fiction | 1965 |

### Note

Sample books are stored in the application but only appear after clicking **Display All**.

---

## Deliverable Status

| Deliverable | Due Date | Status |
|---|---|---|
| Deliverable 1 (Code + GitHub) | Week 3 | ✅ Submitted |
| Deliverable 2 (Report 2–3 pages) | Week 5 | Pending |
| Deliverable 3 (Video 5–7 min) | Week 7 | Pending |

---

## GitHub Repository

```text
https://github.com/senapi619/cross-language-group-project.git
```

---

## Course Information

**Instructor:** Advanced Programming Languages (MSCS-632-A01)

---

## Notes

- Both implementations provide equivalent functionality using different programming languages.
- The project demonstrates similarities and differences between Java and Python application development.
- GUI frameworks used:
  - Java → Swing
  - Python → Tkinter

---

## Author

Developed as part of a Cross-Language Group Project assignment for an Advanced Programming Languages course.

Languages Used:
- Java
- Python

---