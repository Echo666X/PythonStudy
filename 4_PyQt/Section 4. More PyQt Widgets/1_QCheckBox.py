# in this tutorial, you’ll learn how to use the PyQt QCheckBox class to create a checkbox widget.

# the QCheckBox class allows you to create a check wdget, which can be switched on or off.
# the following exaaple shows how to create a checkbox using the QCheckBox class

import sys
from PyQt6.QtWidgets import QCheckBox, QApplication, QWidget, QGridLayout
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.setWindowTitle('CheckBox')
        self.setGeometry(100,100,320,210)
        
        layout = QGridLayout()
        self.setLayout(layout)
        
        checkbox = QCheckBox('I agree', self)
        
        layout.addWidget(checkbox, 0, 0, Qt.AlignmentFlag.AlignCenter)
        
        self.show()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())