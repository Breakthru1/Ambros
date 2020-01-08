# -*- coding:cp1252 -*-

import sys
import time
import random
import tkinter as tk
from tkinter import messagebox


lista = ("Could be possible", "Chances are low", "Chances are high", "Go and ask someone else",
         "Not a chance", "The 8 ball vibrates", "It must be so", "No", "Yes...", "Hmm...Other question maybe?",
         "I do not know", "Ask again later", "Only you know it", "Yes, it is so", "Maybe", "Should i know",
         "It may be", "Think of the trees", "Dunno", "Yes it is"
         )

def ExitApplication():
    MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit',icon = 'warning')
    if MsgBox == 'yes':
        root.destroy()
    else:
        tk.messagebox.showinfo("Return","You will return to the application screen")

    root= tk.Tk() 
    canvas1 = tk.Canvas(root, width = 300, height = 300)
    canvas1.pack()
    button1 = tk.Button (root, text="Exit Application",command=ExitApplication)
    canvas1.create_window(150, 150, window=button1)
    
    root.mainloop() 

def userinput():
        
        question = ("What is your question?")
        print(question)
        stuff = input("> ")
         
        print("\nThinking\n")
        time.sleep(1)
        print(random.choice(lista))

        final()

def final():
    print("Would you like to ask another question?(yes/no)")
    user_reply = input("> ")
    while(input):
            if user_reply == "yes":
                    userinput()
            else:
                ExitApplication()
                   

print("Welcome to the Magic 8 Ball game!")
userinput()

