# importing modules
from tkinter import *

# importing sub-modules
from time import strftime

# variables
__version__ = "v1.0"

# constants
TITLE = "Clock"

# colors
# hexadecimal color code
RED = "#FF0000"
GREEN = "#00FF00"
BLUE = "#0000FF"

BLACK = "#000000"
WHITE = "#FFFFFF"

# creating window
root = Tk()
root.title(f"{TITLE} {__version__}" )
root.resizable(False, False)

# function
def time():
	string = strftime(" 12:34 ")
	label.config(text=string)
	label.after(1000, time)

# will look more attractive
label = Label(root, font=("Digital-7", 80, "bold"), background=BLACK, foreground=RED)

label.pack()
time()

root.mainloop()
