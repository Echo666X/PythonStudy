# in this tutorial, you’ll learn how to create a PyQt application that displays the Hello World message.

from PyQt6.QtWidgets import QApplication, QWidget

# create the Qapplication
app = QApplication([]) # each PyQt application needs one and only one QApplication object

# create the main window
window = QWidget(windowTitle = 'Hello World')
window.show()  #call the show() method to display the window

# start the event loop
app.exec()  # call the exec() method to start the event loop

# note that each PyQt application has one and only one event loop