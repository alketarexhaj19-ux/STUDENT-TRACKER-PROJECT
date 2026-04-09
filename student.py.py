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

