#student.pu

import json
import statistics
import tkinter as tk
from tkinter import messagebox,simpledialog
from tkinter import ttk

student = {} # Dictionary to store student data


#0. Load_data
#Python JSON module documentation
def load_data():
    global students
    try:
        with open("students.json", "r") as file:
            students = json.load(file)
    except:
        students = {}
        #2. add_student
        # GeeksforGeeks Tkinter tutorial
        def add_student():
            name = simpledialog.askstring("Input", "Enter student name:")
            if not name:
                return
            if name in students:
                messagebox.showerror("Error", "Student already exists")
                return
            students[name] = { "marks": [], "average": 0 }
            update_table()
            #3. add_marks
            #1) GeeksforGeeks Tkinter simpledialog tutorial
            #2) Python statistics.mean() documentation
            def add_marks():
                name = simpledialog.askstring("Input", "Enter student name:")
                if name not in students:
                    messagebox.showerror("Error","Student not found")
                    return
                try:
                    mark = float(simpledialog.askstring("Input", "Enter mark (0-100):"))
                    if mark < 0 or mark >100:
                        raise ValueError
                    students[name]["marks"].append(mark)
                    students[name]["average"] = round(statistics.mean(students[name]["marks"]), 2)
                    update_table()
                except:
                    messagebox.showerror("Error", "Invalid input")
            

