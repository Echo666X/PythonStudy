# in this tutorial, you’ll learn step-by-step how to develop the Tkinter “Hello, World!” program.


# the following program shows how to display a window on the screen:
import tkinter as tk

root = tk.Tk() # create an instance of tk.Tk class that will create the application window
# root.mainloop() # this line is commented out so that it does not affect the running of subsequent programs
#
# by convention, the main window in Tkinter is called root, but you can use any other name like main
# the mainloop() method ensures the main window remains wisible on the screen, if you don't call it, the main window will display and disappear almost instantly
# the mainloop() method ensures the main window continues to dispaly and run until you close it
# typically, in a Tkinter program, you place the call to the mainloop() method as the last statement after creating the widgets


# displaying a label
# in tkinter, the components are referred to as widgets
message = tk.Label(root, text = 'Hello World!')
message.pack()
#root.mainloop() # this line is commented out so that it does not affect the running of subsequent programs
# to create a widget that belongs to a container, you ues the following syntax:
#    widget = WidgetName(master, **options)
# the master is the parent window or frame where you want to place the widget
# the options is one or more keyword arguments that specify the configurations of the widget
# in the sample program, "message =..." creates a Label widget placed on the root window
# then the "massage.pack()" positions the Label on the main windowM, if you haven't called it, Tkinter still creates the widget, however, the widget will not be visible


# fixing the blur UI on windows
# if you find the text and UI are blurry on windows, you can use the ctypes python library to fix it
try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
finally:
    root.mainloop()
# the try...finally statement ensures that the application can run across platforms such as Windows, macOS and Linux
# on windows, the code in try block will work properly, the code in the finally lock will always execute that displays the main window 