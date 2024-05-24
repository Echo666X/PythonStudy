# in this tutorial, you’ll learn how to set options for a Tk themed widget using the widget constructor, a dictionary index, and config() method.

# when working with themed widgets, you often need to set their attributes such as text and image
# tkinter allows you to set the options of a widget using one of the following ways:
# 1) use the widget constructor during the widget's creation
# 2) set a property value using a dictionary index after creating widget
# 3) call the config() method with keyword arguments
import tkinter as tk
from tkinter import ttk

# 1) using the widget constructor when creating the widget
# the following illustrates how to use the widget constructor to set the text option for the Label widget:
root = tk.Tk()
ttk.Label(root, text="Hello World!").pack()

# 2) using a dictionary index after widget creation
# the following program shows the same Label but uses a dictionary index to set the text option for the Label widget
label = ttk.Label(root)
label['text'] = 'Hello World!!!'
label.pack()

# 3) using the config() method with keyword arguments]
# the following program illustrates how to use the config() method with a keyword argument to set the text option for the label:
label = ttk.Label(root)
label.config(text = "Hello world!!!!")
label.pack()
root.mainloop()