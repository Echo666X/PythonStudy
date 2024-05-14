# in this tutorial, you’ll learn how to manipulate various attributes of a Tkinter window.
# if you create a simple program that consists of a window, you can see the root window has a title that defaults to tk.
# it also has three system buttons including Minimize, Maxmize and close

import tkinter as tk
root  = tk.Tk()

# to change the windows title, you can use the title() method
# the basic syntax of the title() method is as follows:
# window.title(new_title)
root.title('Tkinter Window Demo')
# to get the current title of a window, you can use the title() method with no argument:
title = root.title()
print(title)

# in Tkinter, the position and the size of a window on the screen is determined by it geometry
# the following shows the geometry specification:
# width×height±x±y
# the width represents the window's width in pixels
# the height represents the window's height in pixels
# the x represents the window's horizontal position, for example, +50(-50) signifies the left(right) edge of the window should be positioned 50 pixels from the left(right) edge of the screen
# the y represents the window's vertical position, for example, +50(-50) signifies the top(bottom) edge of the window should be positioned 50 pixels below the top (bottom)of the screen

# to change the size and the position of a window, you use the geometry() method:
# window.geometry(new_geometry)
# the following example changes the size of the window to 600×400 and the position of the window to 50 pixels from the top and left of the screen
# # root.geometry('600x400+50+50')
# # root.mainloop()

# sometimes, you want to center the window on the screen, the following program illustrates how to do it:

windows_width = 600
windows_height = 400 # setting window parameters

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight() # get the screen width and height using the winfo_screenwidth() and winfo_screenheight() methods

center_x = int((screen_width-windows_width)/2)
center_y = int((screen_height-windows_height)/2)

root.geometry(f'{windows_width}x{windows_height}+{center_x}+{center_y}')
# if you want to get the current geometry of a window, you can use the geometry() method without providing any argument
geometry_output = root.geometry()
print(geometry_output)

# by default, you can resize the width and height of a window, to prevent the window from resizing, you can use the resizable() method
# the basic syntax of the resizable() method is as follows:
# window.resizable(width,height)
# the resizable() method has two parameters that specify whether the width and the height of the window can be resizable
# the following statement will make the window's width cannot be change but the height can be change
root.resizable(False,True)
# when you create a window that is resizable, you can specify the minimum and maximum sizes using minsize() and maxsize() methods:
# window.minsize(min_width,min_height)
# window.maxsize(max_width,max_height)

# Tkinter allows you to specify the transparency of a window by setting its alpha channel ranging from 0.0(fully transparent) to 1.0(fully opaque)
# the basic syntax of setting the transparency is as follows:
# window.attributes('-alpha',0.5)
root.attributes('-alpha', 0.5)

# window stacking order
# the window stack order refers to the windows placed on the screen from bottom to top.
# to ensure that a window is always at the top of the stacking order, you can use the -topmost attribute like this:
# window.attributes('-topmost',1)
# to move a window up or down of the stack, you can use the lift() and lower() methods:
# window.lift()
# window.lift(another_window)
# window.lower()
# window.lower(another_window)
# the following example places the root window on top of all other windows:
root.attributes('-topmost',1)
root.mainloop()

# tkinter window displays a default icon, to change this icon, you follow these steps:
# 1.prepare an image in the .ico format
# 2.place the icon in a folder that can be accessible from the program
# 3.call the iconbitmap() method of the window object
# the basic syntax of the iconbitmap() is as follows:
# window.iconbitmap('./assets/pythontutorial.ico')