# in this tutorial, you’ll learn how to use the PyQt QLineEdit widget to create a single-line text-entry widget.

# The PyQt QLineEdit allows you to create a single-line text-entry widget
# Typically, you’ll use the QLineEdit in a data-entry form.

# to creat a QLineEdit widget, you follow these steps:
# first, import QLineEdit from PyQt6
from PyQt6.QtWidgets import QLineEdit

# second, create a new QLineEdit object that uses:
   # no arguments; with only a parent widget; or with a a default string value as the first argument
   
# 1)simple PyQt QLineEdit exameple
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        
        self.setWindowTitle('QLineEdit Widget')
        self.setGeometry(100,100,320,210)
        
        search_box = QLineEdit(
            self,
            placeholderText = "Enter a keyword to search",
            clearButtonEnabled = True
        )
        
        layout = QVBoxLayout()
        layout.addWidget(search_box)
        self.setLayout(layout)
        
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())