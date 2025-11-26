import tkinter as tk
from tkinter import messagebox, scrolledtext

# list where we keep all the students
students_list = []

def load_students():
    global students_list
    
    # try to load from the file
    try:
        file = open("studentMarks.txt", "r")
        lines = file.readlines()
        file.close()
        
        # first line is how many students
        num_students = int(lines[0])
        
        # read each student line
        for i in range(1, num_students + 1):
            line = lines[i].strip()
            parts = line.split(',')
            
            # make a dictionary for this student
            student = {}
            student['number'] = parts[0]
            student['name'] = parts[1]
            student['coursework1'] = int(parts[2])
            student['coursework2'] = int(parts[3])
            student['coursework3'] = int(parts[4])
            student['exam'] = int(parts[5])
            
            students_list.append(student)
    
    except:
        # if no file just use fake students
        students_list = [
            {'number': '8439', 'name': 'Jake Hobbs', 'coursework1': 10, 'coursework2': 11, 'coursework3': 10, 'exam': 43},
            {'number': '7821', 'name': 'Sarah Smith', 'coursework1': 18, 'coursework2': 19, 'coursework3': 17, 'exam': 85},
            {'number': '9102', 'name': 'Tom Jones', 'coursework1': 15, 'coursework2': 14, 'coursework3': 16, 'exam': 72},
            {'number': '6543', 'name': 'Emma Brown', 'coursework1': 12, 'coursework2': 13, 'coursework3': 11, 'exam': 58}
        ]

def calculate_student_info(student):
    # add up the coursework marks
    total_coursework = student['coursework1'] + student['coursework2'] + student['coursework3']
    
    # add coursework and exam together
    overall_total = total_coursework + student['exam']
    
    # work out percentage out of 160
    percentage = (overall_total / 160) * 100
    
    # figure out the grade
    if percentage >= 70:
        grade = 'A'
    elif percentage >= 60:
        grade = 'B'
    elif percentage >= 50:
        grade = 'C'
    elif percentage >= 40:
        grade = 'D'
    else:
        grade = 'F'
    
    return total_coursework, overall_total, percentage, grade

def format_student_display(student):
    # get all the calculated stuff
    coursework_total, overall_total, percentage, grade = calculate_student_info(student)
    
    # make it look nice
    text = "\n"
    text = text + "Student Name: " + student['name'] + "\n"
    text = text + "Student Number: " + student['number'] + "\n"
    text = text + "Total Coursework Mark: " + str(coursework_total) + "/60\n"
    text = text + "Exam Mark: " + str(student['exam']) + "/100\n"
    text = text + "Overall Percentage: " + str(round(percentage, 1)) + "%\n"
    text = text + "Grade: " + grade + "\n"
    text = text + "--------------------------------------------------\n"
    
    return text

def show_menu():
    # clear the window
    for widget in window.winfo_children():
        widget.destroy()
    
    # title
    title = tk.Label(window, text="STUDENT MANAGER", font=("Arial", 20, "bold"))
    title.pack(pady=30)
    
    # all the menu buttons
    btn1 = tk.Button(window, text="1. View all student records", command=view_all_students, width=35, height=2)
    btn1.pack(pady=5)
    
    btn2 = tk.Button(window, text="2. View individual student record", command=select_student, width=35, height=2)
    btn2.pack(pady=5)
    
    btn3 = tk.Button(window, text="3. Show student with highest total score", command=show_highest, width=35, height=2)
    btn3.pack(pady=5)
    
    btn4 = tk.Button(window, text="4. Show student with lowest total score", command=show_lowest, width=35, height=2)
    btn4.pack(pady=5)
    
    quit_btn = tk.Button(window, text="Quit", command=window.quit, width=35, height=2)
    quit_btn.pack(pady=20)

def view_all_students():
    # clear window
    for widget in window.winfo_children():
        widget.destroy()
    
    # title
    title = tk.Label(window, text="ALL STUDENT RECORDS", font=("Arial", 16, "bold"))
    title.pack(pady=10)
    
    # big text box with scroll bar
    text_box = scrolledtext.ScrolledText(window, width=70, height=20, font=("Courier", 10))
    text_box.pack(pady=10)
    
    # show every student
    for student in students_list:
        student_info = format_student_display(student)
        text_box.insert(tk.END, student_info)
    
    # calculate class average
    total_percentage = 0
    for student in students_list:
        coursework_total, overall_total, percentage, grade = calculate_student_info(student)
        total_percentage = total_percentage + percentage
    
    average = total_percentage / len(students_list)
    
    # add summary at bottom
    text_box.insert(tk.END, "\n==================================================\n")
    text_box.insert(tk.END, "Total number of students: " + str(len(students_list)) + "\n")
    text_box.insert(tk.END, "Class average percentage: " + str(round(average, 1)) + "%\n")
    
    text_box.config(state="disabled")
    
    # back button
    back_btn = tk.Button(window, text="Back to Menu", command=show_menu, width=20, height=2)
    back_btn.pack(pady=10)

def select_student():
    # clear window
    for widget in window.winfo_children():
        widget.destroy()
    
    # title
    title = tk.Label(window, text="SELECT A STUDENT", font=("Arial", 16, "bold"))
    title.pack(pady=20)
    
    # make a button for each student
    for student in students_list:
        btn_text = student['number'] + " - " + student['name']
        btn = tk.Button(window, text=btn_text, command=lambda s=student: view_single_student(s), width=40, height=2)
        btn.pack(pady=3)
    
    # back button
    back_btn = tk.Button(window, text="Back to Menu", command=show_menu, width=40, height=2)
    back_btn.pack(pady=20)

def view_single_student(student):
    # clear window
    for widget in window.winfo_children():
        widget.destroy()
    
    # title
    title = tk.Label(window, text="STUDENT RECORD", font=("Arial", 16, "bold"))
    title.pack(pady=10)
    
    # text box
    text_box = tk.Text(window, width=60, height=15, font=("Courier", 11))
    text_box.pack(pady=10)
    
    # show the student info
    student_info = format_student_display(student)
    text_box.insert(tk.END, student_info)
    text_box.config(state="disabled")
    
    # back button
    back_btn = tk.Button(window, text="Back to Menu", command=show_menu, width=20, height=2)
    back_btn.pack(pady=10)

def show_highest():
    # find who has the best score
    highest_student = students_list[0]
    highest_total = 0
    
    for student in students_list:
        coursework_total, overall_total, percentage, grade = calculate_student_info(student)
        if overall_total > highest_total:
            highest_total = overall_total
            highest_student = student
    
    # clear window
    for widget in window.winfo_children():
        widget.destroy()
    
    # title
    title = tk.Label(window, text="HIGHEST SCORING STUDENT", font=("Arial", 16, "bold"))
    title.pack(pady=10)
    
    # text box
    text_box = tk.Text(window, width=60, height=15, font=("Courier", 11))
    text_box.pack(pady=10)
    
    # show their info
    student_info = format_student_display(highest_student)
    text_box.insert(tk.END, student_info)
    text_box.config(state="disabled")
    
    # back button
    back_btn = tk.Button(window, text="Back to Menu", command=show_menu, width=20, height=2)
    back_btn.pack(pady=10)

def show_lowest():
    # find who has the worst score
    lowest_student = students_list[0]
    lowest_total = 999999
    
    for student in students_list:
        coursework_total, overall_total, percentage, grade = calculate_student_info(student)
        if overall_total < lowest_total:
            lowest_total = overall_total
            lowest_student = student
    
    # clear window
    for widget in window.winfo_children():
        widget.destroy()
    
    # title
    title = tk.Label(window, text="LOWEST SCORING STUDENT", font=("Arial", 16, "bold"))
    title.pack(pady=10)
    
    # text box
    text_box = tk.Text(window, width=60, height=15, font=("Courier", 11))
    text_box.pack(pady=10)
    
    # show their info
    student_info = format_student_display(lowest_student)
    text_box.insert(tk.END, student_info)
    text_box.config(state="disabled")
    
    # back button
    back_btn = tk.Button(window, text="Back to Menu", command=show_menu, width=20, height=2)
    back_btn.pack(pady=10)

# make the main window
window = tk.Tk()
window.title("Student Manager")
window.geometry("750x550")

# load the students
load_students()

# show the menu
show_menu()

# run the program
window.mainloop()