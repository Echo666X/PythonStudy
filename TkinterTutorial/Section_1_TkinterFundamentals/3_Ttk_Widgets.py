# in this tutorial, you’ll learn about Tk themed widgets by using the Tkinter.ttk module.

# introduction to Tk themed widgets
# tkinter has two generations of widgets:
# the old classic tk widegets, tkinter introduced them in 1991
# the newer themed ttk widgets added in 2007 with Tk 8.5, the newer Tk themed widgets replace many(but not all) classic widgets
# note that ttk stands for k themed, therefore, Tk themed widgets are the same as ttk widgets

# the tkinter.ttk module contains all the new ttk widgets, it's a good practice to always use themed widgets whenever they're available

# the following statements import the classic and the new Tk themed widgets:
import tkinter as tk
from tkinter import ttk

# the following program illustrates how to create classic and themed labels:
root = tk.Tk()
tk.Label(root,text="Classic Label").pack()
ttk.Label(root,text="Themed Label").pack()
# they look similar, however, their appearences depend on the platform on which the program runs
root.mainloop()

# by using the Tk themed widgets, you gain the following advantages:
# separating the widget's behavior and appearance through the styling system.
# the ttk widgets have the native look and feel of the platform on which the program runs
# simplify the state-specific widget behaviors---the ttk widgets simplify and generalize the state-specific widget behavior

# the following ttk widgets replace the Tkinter widgets with the same names:
# Button
# Checkbutton
# Entry
# Frame
# Label
# LabelFrame
# Menubutton
# PanedWindow
# Radiobutton
# Scale
# Scrollbar
# Spinbox
# and the following widgets are new and specific to ttk:
# Combobox
# Notebook
# Progressbar
# Separator
# Sizegrip
# Treeview