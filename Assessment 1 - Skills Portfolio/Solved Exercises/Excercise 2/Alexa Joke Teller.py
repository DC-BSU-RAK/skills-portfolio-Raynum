import tkinter as tk
from tkinter import messagebox
import random

# list to hold all the jokes
all_jokes = []
current_setup = ""
current_punchline = ""

def load_jokes():
    global all_jokes
    
    # try to open the file
    try:
        file = open("randomJokes.txt", "r")
        lines = file.readlines()
        file.close()
        
        # go through each line and split it
        for line in lines:
            if '?' in line:
                parts = line.split('?')
                setup = parts[0] + '?'
                punchline = parts[1].strip()
                # add it to our list
                joke = {'setup': setup, 'punchline': punchline}
                all_jokes.append(joke)
    
    except:
        # if theres no file just use these jokes
        all_jokes = [
            {'setup': 'Why did the chicken cross the road?', 'punchline': 'To get to the other side.'},
            {'setup': 'What happens if you boil a clown?', 'punchline': 'You get a laughing stock.'},
            {'setup': 'Why dont scientists trust atoms?', 'punchline': 'Because they make up everything!'},
            {'setup': 'What do you call a bear with no teeth?', 'punchline': 'A gummy bear!'},
            {'setup': 'Why did the scarecrow win an award?', 'punchline': 'He was outstanding in his field!'}
        ]

def tell_joke():
    global current_setup, current_punchline
    
    # just pick any random joke
    joke = random.choice(all_jokes)
    current_setup = joke['setup']
    current_punchline = joke['punchline']
    
    # show the setup part
    setup_label.config(text=current_setup)
    punchline_label.config(text="")
    
    # change which buttons work
    punchline_btn.config(state="normal")
    next_btn.config(state="disabled")
    joke_btn.config(state="disabled")

def show_punchline():
    # show the funny part
    punchline_label.config(text=current_punchline)
    
    # change buttons again
    punchline_btn.config(state="disabled")
    next_btn.config(state="normal")

def next_joke():
    # clear everything
    setup_label.config(text="")
    punchline_label.config(text="")
    
    # reset buttons
    joke_btn.config(state="normal")
    punchline_btn.config(state="disabled")
    next_btn.config(state="disabled")

# make the window
window = tk.Tk()
window.title("Alexa Joke Teller")
window.geometry("550x400")

# load all the jokes first
load_jokes()

# title at top
title_label = tk.Label(window, text="🎤 Alexa Joke Assistant", font=("Arial", 22, "bold"))
title_label.pack(pady=30)

# this shows the joke question
setup_label = tk.Label(window, text="", font=("Arial", 14), wraplength=500, fg="blue")
setup_label.pack(pady=20)

# this shows the answer
punchline_label = tk.Label(window, text="", font=("Arial", 13), wraplength=500, fg="green")
punchline_label.pack(pady=10)

# button to get a joke
joke_btn = tk.Button(window, text="Alexa tell me a Joke", command=tell_joke, width=25, height=2, bg="lightblue", font=("Arial", 11))
joke_btn.pack(pady=10)

# button to see the punchline
punchline_btn = tk.Button(window, text="Show Punchline", command=show_punchline, width=25, height=2, state="disabled")
punchline_btn.pack(pady=5)

# button to go to next joke
next_btn = tk.Button(window, text="Next Joke", command=next_joke, width=25, height=2, state="disabled")
next_btn.pack(pady=5)

# quit button
quit_btn = tk.Button(window, text="Quit", command=window.quit, width=25, height=2)
quit_btn.pack(pady=10)

# start the program
window.mainloop()