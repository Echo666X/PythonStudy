# in this tutorial, you’ll learn how to use the PyQt QPushButton widget to create a push button.

# the PyqtButton class allow you to create a button widget, which can be a push button or a toggle button
# to create a push button, you follow these steps:

# first, import QPushButton from PuQt.QWidgets
# from PyQt6.QtWidgets import QPushButton

# second, call the QPushButton() with a text that appears on the button:
# button = QPushButton('Click Me')

# Third,connet the clicked signal to a callable:
# button.clicked.connect(self.on_clicked) #the on_clicked is a method that executes

# the following shows the complete program that displays a button on a window:
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class mainwindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.setWindowTitle('PyQt QPushButton Widget')
        self.setGeometry(100,100,320,210)
        
        button = QPushButton('click me')
    
        layout = QVBoxLayout()
        layout.addWidget(button)
        self.setLayout(layout)
    
        self.show()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    window = mainwindow()
    
    sys.exit(app.exec())