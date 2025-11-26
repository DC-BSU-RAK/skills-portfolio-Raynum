import tkinter as tk
from tkinter import messagebox
import random

# stuff to keep track of the game
score = 0
question_count = 0
tries = 0
correct_answer = 0
difficulty_level = 0

def displayMenu():
    # just clear everything first
    for widget in window.winfo_children():
        widget.destroy()
    
    # make the difficulty menu
    title = tk.Label(window, text="DIFFICULTY LEVEL", font=("Arial", 16, "bold"))
    title.pack(pady=30)
    
    # three buttons for difficulty
    easy_btn = tk.Button(window, text="1. Easy", command=lambda: start_quiz(1), width=20, height=2)
    easy_btn.pack(pady=5)
    
    moderate_btn = tk.Button(window, text="2. Moderate", command=lambda: start_quiz(2), width=20, height=2)
    moderate_btn.pack(pady=5)
    
    advanced_btn = tk.Button(window, text="3. Advanced", command=lambda: start_quiz(3), width=20, height=2)
    advanced_btn.pack(pady=5)

def start_quiz(level):
    global score, question_count, difficulty_level
    # reset everything
    score = 0
    question_count = 0
    difficulty_level = level
    show_next_question()

def randomInt():
    # make random numbers based on what level they picked
    if difficulty_level == 1:
        # easy is just 1-9
        return random.randint(1, 9)
    elif difficulty_level == 2:
        # moderate is 10-99
        return random.randint(10, 99)
    else:
        # advanced is big numbers
        return random.randint(1000, 9999)

def decideOperation():
    # just pick plus or minus randomly
    if random.randint(0, 1) == 0:
        return '+'
    else:
        return '-'

def show_next_question():
    global question_count, tries, correct_answer
    
    # check if we did 10 questions already
    if question_count >= 10:
        displayResults()
        return
    
    # clear the screen
    for widget in window.winfo_children():
        widget.destroy()
    
    # start fresh for this question
    tries = 0
    
    # make up a math problem
    num1 = randomInt()
    num2 = randomInt()
    operation = decideOperation()
    
    # figure out what the answer should be
    if operation == '+':
        correct_answer = num1 + num2
    else:
        correct_answer = num1 - num2
    
    # show the question on screen
    question_label = tk.Label(window, text="Question " + str(question_count + 1) + " of 10", font=("Arial", 12))
    question_label.pack(pady=10)
    
    score_label = tk.Label(window, text="Current Score: " + str(score), font=("Arial", 10))
    score_label.pack()
    
    problem_label = tk.Label(window, text=str(num1) + " " + operation + " " + str(num2) + " = ", font=("Arial", 24, "bold"))
    problem_label.pack(pady=30)
    
    # box for them to type answer
    global answer_box
    answer_box = tk.Entry(window, font=("Arial", 16), width=15)
    answer_box.pack(pady=10)
    answer_box.focus()
    
    # button to submit
    submit_btn = tk.Button(window, text="Submit Answer", command=isCorrect, width=15, height=2)
    submit_btn.pack(pady=10)

def isCorrect():
    global score, question_count, tries
    
    # try to get their answer
    try:
        user_answer = int(answer_box.get())
        
        # check if they got it right
        if user_answer == correct_answer:
            # yay they got it
            if tries == 0:
                # first try gets 10 points
                score = score + 10
                messagebox.showinfo("Correct!", "Well done! You got 10 points!")
            else:
                # second try gets 5 points
                score = score + 5
                messagebox.showinfo("Correct!", "Good job! You got 5 points!")
            
            # move to next question
            question_count = question_count + 1
            show_next_question()
        
        else:
            # wrong answer
            tries = tries + 1
            
            if tries >= 2:
                # they already tried twice so move on
                messagebox.showerror("Wrong", "Sorry, the correct answer was " + str(correct_answer))
                question_count = question_count + 1
                show_next_question()
            else:
                # let them try again
                messagebox.showwarning("Try Again", "Wrong! Try again for 5 points")
                answer_box.delete(0, tk.END)
    
    except:
        # they didnt type a number
        messagebox.showerror("Error", "Please enter a valid number!")

def displayResults():
    # clear screen
    for widget in window.winfo_children():
        widget.destroy()
    
    # figure out what grade they got
    if score >= 90:
        grade = "A+"
    elif score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "F"
    
    # show them how they did
    title = tk.Label(window, text="Quiz Finished!", font=("Arial", 20, "bold"))
    title.pack(pady=30)
    
    score_label = tk.Label(window, text="Your Score: " + str(score) + " out of 100", font=("Arial", 14))
    score_label.pack(pady=10)
    
    grade_label = tk.Label(window, text="Your Grade: " + grade, font=("Arial", 14))
    grade_label.pack(pady=10)
    
    # buttons to play again or quit
    play_again_btn = tk.Button(window, text="Play Again", command=displayMenu, width=15, height=2)
    play_again_btn.pack(pady=10)
    
    quit_btn = tk.Button(window, text="Quit", command=window.quit, width=15, height=2)
    quit_btn.pack(pady=5)

# make the window
window = tk.Tk()
window.title("Maths Quiz")
window.geometry("500x400")

# start the game
displayMenu()

window.mainloop()