#student.py

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
 # 4. delete_student
# : GeeksforGeeks Python dictionary tutorial

def delete_student():
    name = simpledialog.askstring("Input", "Enter student name to delete:")
    if name in students:
        del students[name]
        update_table()
    else:
        messagebox.showerror("Error", "Student not found")
        #5. search_student
        # StackOverflow Tkinter simpledialog example
        def search_student():
            name = simpledialog.askstring("Search", "Enter student name;")
            if name in students:
                data = students[name]
                messagebox.showinfo("Result", f"{name}\nMarks: {data['marks']}\nAverage: {data['average']}")
            else:
                messagebox.showerror("Error", "Student not found")
                #6. update_table
                # StackOverflow Treeview example
                def update_table():
                    for row in tree.get_children():
                        tree.delete(row)
                        for name, data in students.items():
                            tree.insert("","end", values=(name, str(data["marks"]), data["average"]))

  #7. sort_students
  # Python sorted() documentation
def sort_students():
    sorted_data = sorted(students.items(), key=lambda x: x[1]["average"], reverse=True)
    for row in tree.get_children():
        tree.delete(row)
    for name, data in sorted_data:
        tree.insert("","end", values=(name, str(data["marks"]), data["average"]))

        #8. load_and_refresh
        #Concept: Refresh GUI table after loading JSON data
        #Python JSON documentation + Treeview handling
def load_and_refresh():
    try:
        load_data()
        update_table()
        messagebox.showinfo("Success", "Data loaded sucessfully!")
    except:
        messagebox.showerror("Error", "Failed to load data")
      

   
  
    




              
                


               