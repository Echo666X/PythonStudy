# in this tutorial, you’ll learn about the Tkinter Label widget and how to use it to display a text or image on the screen.
# Tkinter Label widget is used to display a text or image on the screen, to use a Label widget, you use the following general syntax:
# label = ttk.Label(master,**options)
# the Label widget has many options that allow you to customize its appearance, you can see more details in the 7.1 markdown.

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x800")
root.resizable(False,True)
root.title("Label Widget Demo")

# the following program shows how to display a regular label on the root window
label = ttk.Label(root, text="This is a Label") # create a new instance of the Label Widget, set its container to the root window, and assign a literal string to its text property
label.pack()


# setting a specific font for the Label
# you can pass the font keyword argument to the Label constructor, 
# the basic syntax of the keyword argument is as follows:
# font = ('font name', font_size)
# the following program illustrates an example:
label_font_demo = ttk.Label(
    root,
    text="A label with the Helvetica font",
    font=("Helvetica",14)
)
label_font_demo.pack(ipadx=10, ipady=10) 
# the ipadx and ipady parameters are used to set the internal padding of the Label componet.The specific functions is used to set the horizontal internal padding of the Label component


# displaying an image
# you can create a Photoimage widget by passing the path of the photo to the PhotoImage constructor:
# photo = tk.PhotoImage(file = "path")
# the following program illustrates how to use a Label widget to display an image:
photo = tk.PhotoImage(file='C:/Users/ROG/Pictures/Screenshots/屏幕截图 2024-05-16 171606.png')
label_image_demo = ttk.Label(root,image=photo)
label_image_demo.pack()
# to display both text and image, you'll use the text attribute and compound option
# the compound option specifies the position of the image relative to the text, you can find more details in the 7.2 markdown
# the following program shows how to diaplay both text and image on a label:
label_textimage_demo = ttk.Label(
    root,
    image=photo,
    text="Life is short,\nI choose Python",
    font=("Helvetica",14),
    compound="top"
    )
label_textimage_demo.pack()


root.mainloop()