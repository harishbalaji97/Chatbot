import os
import aiml

BRAIN_FILE="brain.dump"

k = aiml.Kernel()

# To increase the startup speed of the bot it is
# possible to save the parsed aiml files as a
# dump. This code checks if a dump exists and
# otherwise loads the aiml from the xml files
# and saves the brain dump.
if os.path.exists(BRAIN_FILE):
    print("Loading from brain file: " + BRAIN_FILE)
    k.loadBrain(BRAIN_FILE)
else:
    print("Parsing aiml files")
    k.bootstrap(learnFiles="std-startup.aiml", commands="load aiml b")
    print("Saving brain file: " + BRAIN_FILE)
    k.saveBrain(BRAIN_FILE)
from tkinter import *
from tkinter.messagebox import *

def show_answer():
    Ans = str(num1.get())
    response = k.respond(Ans)
    blank.insert(0, response)


main = Tk()
Label(main, text="SIMPLE CHAT BOT",font=("times new roman",20),fg="white",bg="maroon",height=2).grid(row=0,rowspan=2,columnspan=8,sticky=N+E+W+S,padx=5,pady=5)
Label(main, text = "ENTER THE INPUT :").grid(row=3)
Label(main, text = "REPLY").grid(row=4)


num1 = Entry(main)
blank = Entry(main)


num1.grid(row=3, column=1)
blank.grid(row=4, column=1)


Button(main, text='Quit', command=main.destroy).grid(row=5, column=0, sticky=W, pady=4)
Button(main, text='Click for response', command=show_answer).grid(row=5, column=1, sticky=W, pady=4)

mainloop()