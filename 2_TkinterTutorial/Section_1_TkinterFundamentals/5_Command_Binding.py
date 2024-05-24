# in this tutorial, you’ll learn about the Tkinter command binding that associates a callback with an event of a widget.
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Command Binding Demo")
root.geometry("600x400+50+50")
# introduction to Tkinter command binding
# to make the application more interative, the widgets need to respond to the events such as: Mouse click or Key presses
# this requires assigning a callback function to a specific event, once the event occurs, the callback will be invoked automatically to handle the event
# in tkinter, some widgets allow you to associate a callback function with an event using the command binding
# it means that you can assign the name of a function to the command option of the widget so that when the event occurs on the widget, the function will be called automatically

# take an example:
def button_clicked():
    """define a function as a callback"""
    print("button clicked")
    
button = ttk.Button(root, text="Click Me!",command=button_clicked) # associate the function with the command option of a button widget
# it should be noted that you pass the callback without parentheses() within the command option, otherwise, the callback would be called as soon as the program runs
button.pack()

# Tkinter button command arguments
# you can use a lambda expression to pass the arguments to a callback function
def output(args):
    print(args)
    
ttk.Button(root,text="Rock",command=lambda :output("Rock")).pack()
ttk.Button(root,text="Paper",command=lambda :output("Paper")).pack()
ttk.Button(root,text="Scissors",command=lambda :output("Scissors")).pack()

# limitations fo command binding
# 1) the command option is not available in all widgets, it is limited to the Button and some other widgets
# 2) the command button binds to the left click and the backspace, but doesn't bind to the Return key,unfortunately, you cannot change the binding of the command function easily
 
root.mainloop()