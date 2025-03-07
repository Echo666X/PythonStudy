#  in this tutorial, you’ll learn how to use the PyQt QLabel widget to display text or an image.

# to create a label widget,you follow these steps:
# first, import the QLabel widget from PyQt6.QtWidgets module:
from PyQt6.QtWidgets import QLabel

# second, create a new instance of the Qlabel class:
label1 = QLabel('This is Qlabel widget')

# also you can use the setText() method to set a text to the QLabel widget after creating the QLabel widget
label2 = QLabel()
label2.setText('This is Qlabel widget num2')

# to get the text of the QLabel() widget, you call the text() method:
label2.text()

# to clear the text of a QLabel widget, you use the clear() method:
label2.clear()