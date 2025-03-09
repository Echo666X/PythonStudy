# 3in this tutorial, you’ll learn how to use the PyQt QHBoxLayout to arrange widgets horizontally.

# PyQt layout defines the way to arrage child widgets on a parent widget
# PyQt supports a variety of layout classes, each has a layout strategy that suits a particular situation

# the steps for using a layout  class are as follows:
# First, create a layout object from a layout class.
# Second, assign the layout object to the parent widget’s layout property using the setLayout() method.
# Third, add widgets to the layout using the addWidget() method of the layout object.

# also you can add layouts to a layout using the addLayout() method

# introduction to the PyQt QHBoxLayout
# the QHBoxLayout divides the parent widget into horizonal boxes and places the child widgets sequentially from left to right

# the following program shows how to use the QHBoxLayout
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.setWindowTitle('PyQt QHBoxLayout')
        
        layout = QHBoxLayout()
        self.setayout(layout)
        
        # create buttons and add them to the Layout
        titles = ['Yes', 'No', 'Cancel']
        buttons = [QPushButton(title) for title in titles]
        
        for button in buttons:
            layout.addWidget(button)
            
        self.show()
        
if __name__ =='__main__':
    app = QApplication(sys.argv)
    
    window = MainWindow()
    
    sys.exit(app.exec())