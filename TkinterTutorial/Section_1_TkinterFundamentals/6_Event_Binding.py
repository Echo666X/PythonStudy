# in this tutorial, you’ll learn about the Tkinter event binding mechanism.
# assigning a funtion to an event of a widget is known as event binding, the assigned function is invoked automatically when the event occurs
# in the previous tutorial, it noted that not all widgets support the command option
# therefore, Tkinter provides you with an alternative way for event binding via the bind() method

# the basic syntax of the bind() method is as follows:
# widget.bind(event,handler,add=None)  
#once the event occurs, the handler will be invoked automatically
# if you want to register an additional handler, you can pass the "+" to the add argument, this allows you to have mutiple event handlers responding to the same event

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Event Binding Demo")
root.geometry("800x400+100+100")

# the following program illustrates how to bind the return_pressed function to the Return key pressed event of the 'Save' button
def return_pressed(_):
    print("Return key pressed.")
    
button = ttk.Button(root,text="Save")
button.bind("<Return>",return_pressed) # this statement calls the bind() method on the button widget to bind the Return key pressed event
button.focus()
button.pack(expand=True)


# also you can use the bind() method to register multiple handlers for the same event
def log(event):
    print(event)
    
button.bind("<Return>",log,add="+") # the third argument add='+' registered additional handler, which is the log() function
# if you don't use the add, the bind() method will replace the existing handler by the new one
button.focus()
button.pack(expand=True)


# Event patterns
# tkinter uses event patterns to map event names with handlers, for example, <Return> denotes the Return key pressed
# the basic syntax of an event pattern is as follows:
# <modifier-type-detail>
# an event is surrounded by angle brackets<>, inside the angle brackets, there are zero or more modifiers, an event type, and detailed information about the event
# you can see more details of the event patterns in 6_Event_Binding.md


# the levels of binding
# binding an event to a particular instance of a widget is called an instance-level binding
# however, you can also bind an event to all the instances of a widget.
# you can bind the event to all the textboxes in a program like:
root.bind_class("Entrty","<Control-V>",log)

# sometimes, you may want to undo the effect of an earlier binding, to do it, you can use the unbind() method
# widget.unbind(event)
# the following example unbinds the event from the button :
button.unbind('<Return>')
root.mainloop()
