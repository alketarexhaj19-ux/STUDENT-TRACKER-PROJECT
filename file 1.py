
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
            



 