# in this tutorial, you will learn how to use PyQt QgridLayout to arrange widgets

# introduction to the PyQt QgridLayout
# The QGridLayout allows you to place widgets in uniform rows and columns of a grid. 
# rows and colomns are zero-based indexing.
# the intersection between a row and a column is called a cell. a cellis a space where you can place a widget
# rows and columns can span.

# If a widget takes less space than the containing cell, you can align it within the cell using the  alignment options in the 3_QgridLayout.m

# you use the addWidget() method to plce the child widgets on the gridlayout:
# layout.addWidget(widget, row, column, rowSpan, columnSpan, alignment)
# widget is a child widget that you want to place on the grid
# row and column is a index that starts from 0
# span is the number that you want to span
# alignment specifies the alignmet of the widget within the cell

# to get the alignment value, you import Qt from PyQt6.Qtcore
# and use one of the values of the Qt.AlignmentFlag enum, for example:
# Qt.AlignmentFlag.AlignRight

# the following example shows how to create a login form using the QGridLayout
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QGridLayout
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        self.setWindowTitle('Login Form')
        self.setGeometry(100,100,320,210)
        
        layout = QGridLayout()
        self.setLayout(layout)
        
        layout.addWidget(QLabel('Username:'),0,0)
        layout.addWidget(QLineEdit(),0,1)
        
        layout.addWidget(QLabel('Password:'),1,0)
        layout.addWidget(QLineEdit(echoMode = QLineEdit.EchoMode.Password),1,1)
        
        layout.addWidget(QPushButton('Login:'), 2, 0, 
                         alignment= Qt.AlignmentFlag.AlignRight)
        
        layout.addWidget(QPushButton('Close:'), 2, 1,
                         alignment= Qt.AlignmentFlag.AlignRight)
        
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())