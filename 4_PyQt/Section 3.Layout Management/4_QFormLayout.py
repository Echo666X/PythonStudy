# in this tutorial, you’ll learn how to use PyQt QFormLayout to arrange widgets in a form.

# introdution to the PyQt QFormLayout
# when creating a data-entry form ,you often need to place fields in rows, and on each row, you place a label next to an input widget
# PyQt provides you with a convenient two-column form that arranges the widgets on a form. 
# The left column has a label and the right column has an input widget.

# the following example shows how to create a sign up form using the QFormLayout:
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit,  QFormLayout

class MainWindow(QWidget):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.setWindowTitle('Sign Up Form')
        self.setGeometry(100,100,320,210)
        
        layout = QFormLayout()
        self.setLayout(layout)
        
        # The addRow() method takes a string and a widget and automatically creates the QLabel widget for the string
    
        layout.addRow('Name:',QLineEdit(self))
        layout.addRow('Email:',QLineEdit(self))
        layout.addRow('Password:',QLineEdit(self, echoMode = QLineEdit.EchoMode.Password))
        layout.addRow('Confirm Password:',QLineEdit(self, echoMode = QLineEdit.EchoMode.Password))
        layout.addRow('Phone:', QLineEdit(self))
        
        # if you pass a single widget such as a Qlabel, the widget will automatically span both columns.
        # in practice, you can use this feature for creating headings or section labels
        layout.addRow(QPushButton('Sign Up'))
        
        self.show()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    
    sys.exit(app.exec())