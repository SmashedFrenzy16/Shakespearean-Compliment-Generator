from tkinter import *
import random


root = Tk()
root.title("Shakespearean Compliment Generator By @SmashedFrenzy16")
root.geometry("800x600")

column1raw = """rare
    sweet
    fruitful
    brave
    sugared
    flowering precious
    gallant
    delicate
    celestial"""


column2raw = """honey-tongued
well-wishing
fair-faced
best-tempered
tender-hearted
tiger-booted
smooth-faced
thunder-darting
sweet-suggesting
young-eyed"""

column3raw = """smilet
toast
cukoo-bud
nose-herb
wafer-cake
pigeon-egg
welsh cheese
song
true-penny
valentine"""

column1 = column1raw.split()
column2 = column2raw.split()
column3 = column3raw.split()

title = Label(root, text = "Welcome To This Shakespearean Compliment Generator!", font = "Arial 24 bold italic", foreground = "red")
title.pack()

def comp_command():

    emptylabel = Label(root, text = "")
    emptylabel.pack()

    comp = Label(root, text = "Thou " + random.choice(column1) + " " + random.choice(column2) + " " + random.choice(column3))
    comp.pack()

emptylabel2 = Label(root, text = "")
emptylabel2.pack()

generate_button = Button(root, text = "Generate Shakespearean Compliment!", command = comp_command)
generate_button.pack()


root.mainloop()