# Student Progress Tracker (Tkinter GUI Project)
## Identifying Information
- **Name:** Alketa Rexhaj
- **P-Number:** P513974
- **Course Code:** IY499

## Declaration of Own Work
I confirm that this assignment is my own work.   
Where I have referred to online sources, I have provided comments detailing the reference and included a link to the source.

## Program Description
The **Smart Student Progress Tracker** is an advanced Python desktop application designed for comprehensive student academic management. It combines traditional grade tracking with intelligent analytics to provide deep insights into student performance, trends, and areas for improvement.

##  Project Description
This project is a Python-based Student Progress Tracker using Tkinter.  
It allows users to add students, store marks, calculate averages, search, sort, save, and load data using a JSON file.
It allows users to manage student records through a simple graphical interface.

The system can:
- Add students
- Add marks
- Automatically calculate averages
- Search and delete students
- Sort students by performance
- Save data to a file (JSON)
- Load saved data back into the program
- Display all data in a table (GUI Treeview)
  
## How the System Works

The program uses a Python dictionary called `students` to store all data in memory.

### Example Structure:
```python
students = {
    "Ali": {
        "marks": [80, 90],
        "average": 85
    }
}
 Program Flow:
User adds a student → stored in dictionary
User adds marks → stored in list
Average is automatically calculated
GUI table updates instantly
Data can be saved to JSON file
Data can be loaded again later
 Features & Functions

1. load_data()

Loads student data from students.json.
 If file exists → data is loaded
 If file does not exist → empty system starts

2. save_data()

Saves all student data into a file.
 Prevents data loss
 Allows data reuse later

3. add_student()

Adds a new student to the system.
 Uses input dialog
 Creates empty marks list
 Initializes average as 0

4. add_mark()

Adds a mark to a student.
 Stores marks in a list
 Calculates average using statistics
 Updates table instantly

5. delete_student()

Removes a student completely.
 Deletes all stored data for that student

6. search_student()

Searches for a student and displays their details.
 Shows marks and average in a popup

7. update_table()

Updates the GUI table (Treeview)
 Clears old data
 Displays updated student list

8. sort_students()

Sorts students by average (highest first).
Uses Python sorted() function
 Updates table in sorted order

9. load_and_refresh()

Loads data from file and refreshes GUI.
 Combines loading + table update
 Graphical User Interface (GUI)
The project uses Tkinter GUI library.

It includes:

Buttons for all actions
Table (Treeview) to display students
Frame layout for organization

Each button is linked to a function:

Add Student → add_student()
Add Mark → add_mark()
Save → save_data()
Load → load_and_refresh()


 How to Run the Project
python student.py

Project Structure
Student Tracker Project/
│
├── student.py.py

└── README.md


 Concepts Used
Python Dictionaries
File Handling (JSON)
Tkinter GUI
Functions
Lists
Sorting
Exception Handling


 REFERENCES
Python Software Foundation (2023). json — JSON encoder and decoder — Python 3.8.3rc1 documentation. [online] docs.python.org. Available at: https://docs.python.org/3/library/json.html.

‌
Python.org. (2019). statistics — Mathematical statistics functions — Python 3.7.2 documentation. [online] Available at: https://docs.python.org/3/library/statistics.html.

Python documentation. (n.d.). Built-in Functions. [online] Available at: https://docs.python.org/3/library/functions.html#sorted.

Python Software Foundation (2019). tkinter — Python interface to Tcl/Tk — Python 3.7.2 documentation. [online] python.org. Available at: https://docs.python.org/3/library/tkinter.html.

Bansal, R. (2017). Python GUI - tkinter - GeeksforGeeks. [online] GeeksforGeeks. Available at: https://www.geeksforgeeks.org/python-gui-tkinter/.

bansal, ayushmaan (2018). Python Dictionary. [online] GeeksforGeeks. Available at: https://www.geeksforgeeks.org/python-dictionary/.

Pythonexamples.org. (2024). Tkinter simpledialog - Prompt for User Input. [online] Available at: https://pythonexamples.org/python-tkinter-simpledialog-prompt-for-user-input/?utm_source=chatgpt.com [Accesed 5 Apr.2026]

Bing.com. (2026). tkinter treeview insert data - Search Videos. [online] Available at: https://www.bing.com/videos/riverview/relatedvideo?q=tkinter+treeview+insert+data&mid=C85CB516112FD01C0514C85CB516112FD01C0514&FORM=VIRE 

Python, R. (n.d.). Lists and Tuples in Python – Real Python. [online] realpython.com. Available at: https://realpython.com/python-lists-tuples/.

W3schools (2018). Python Dictionaries. [online] W3schools.com. Available at: https://www.w3schools.com/python/python_dictionaries.asp.







