# in this tutorial, you’ll learn about PyQt signals & slots and how they work in PyQt applications.

# Typically, a Python script runs from the top to the bottom as follows:
  # Get inputs.
  # Process the inputs to produce outputs.
  # Write the outputs to the screen or a file.
# this is called procedure programming

# when you create a GUI program, you use event-driven programming instead.
# in the event-driven programming paradigm, a program has the following flow:
  # Create widgets like labels, line edits, and buttons.
  # Start an event loop that waits for events.
  # Respond to events when they occur by executing callables.
  
# to connect events with callables of the program,PyQt uses the signals and slots mechanism

# Signals
# A signal is a special property of an object that is emitted when an event occurs. 
# An event may be a user action, a timeout, or the completion of an asynchronous operation.

# Slots
# A slot is a callable that can receive a signal and respond to it.

# example:
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QPushButton,
    QVBoxLayout
)


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # set the window title
        self.setWindowTitle('Qt Signals & Slots')

        # create a button widget and connect its clicked signal
        # to a method
        button = QPushButton('Click me')
        button.clicked.connect(self.button_clicked)

        # place the buton on window using a vertical box layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(button)

        # show the window
        self.show()

    def button_clicked(self):
        print('clicked')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create the main window and display it
    window = MainWindow()

    # start the event loop
    sys.exit(app.exec())