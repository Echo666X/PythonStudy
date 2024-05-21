# in this tutorial, you’ll learn about the Tkinter Button widget and how to use it to create various kinds of buttons.
 # the showinfo function is used to display a simple message box in a Tkinter application
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.geometry("300x200+0+0")
root.resizable(False,False)
root.title("Demo_0")

button = ttk.Button(
    root,
    text="Button Demo",
    )
button.pack()

# introduction to the Tkinter Button:
# Button widgets represent a clickable item in the applications, 
# typically, you use text or an image to display the action that will be performed when clicked

# Button can display text in a single font, the text can span multiple lines, 
# on the top of that, you can make one of the characters uderline to mark a keyboard shortcut

# to invoke a function or a method of a class automatically when the button is clicked, you assign its command option to the function or method
# This is called the command binding in Tkinter

# you can use the ttk.Button constructor to create a button:
# button = ttk.Button(master,**option)
# the typical option is as follows:
# button = ttk.Button(master,text,command)  
# the master is the parent widget on which you place the button, the text is the Label of the button, 
# and the command specifies a callback function that will be called automatically when the button is clicked

# command callback
# you can use a lambda expression to assign a callback to the command option:
# ttk.Button(root,text=,command = lambda_expression)

# button states:
# the default state of a button is normal, in this state the button will respond to the mouse events and keyboard presses by invoking the callback function assigned to its command option
# the button also have the disabled state, it will be greyed out and doesn't respond to the mouse events and keyboard presses
# you can change the state by using the state() method
button.state(['disabled']) # the button will be greyed out
button.state(['!disabled']) # the button becomes normal again

# let's take some example:
# 1) suppose you want to design a program with a single button, once you click it, the program is terminated
example_test_1 = tk.Tk()
example_test_1.geometry("300x200+300+0")
example_test_1.resizable(False,False)
example_test_1.title("Demo_1")

exit_button = ttk.Button(
    example_test_1,
    text="Exit",
    command=root.quit())
exit_button.pack(ipadx=5,ipady=5,expand=True)


# 2）the following example shows how to display an image button
example_test_2 = tk.Tk()
example_test_2.geometry("300x200+600+0")
example_test_2.resizable(False,False)
example_test_2.title('Demo_2')

def download_clicked():
    showinfo(
        title="Information",
        message="Download button clicked!"
    )

download_icon = tk.PhotoImage(file="D:/download.png")
download_button = ttk.Button(
    example_test_2,
    image=download_icon,
    command=download_clicked
)

download_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)



root.mainloop()
example_test_1.mainloop()
example_test_2.mainloop()