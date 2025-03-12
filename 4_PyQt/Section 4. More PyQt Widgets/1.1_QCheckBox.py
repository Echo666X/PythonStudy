# the stateChanged signal

# if you want to do something when the checkbox is checked or unchecked, you can connnect a slot to the statechanged signal
# for example:
# checkbox = QCheckBox('I agree', self)
# checkbox.stateChanged.connect(self.on_checkbox_changed)

# The stateChanged signal sends a value that indicates whether the button is checked or unchecked. 
# To check the state of a QCheckBox, you create a Qt.CheckState instance:

# state = Qt.CheckState(value)

# and compare it with one of three values:
# Checked, Unchecked, Partially checked

# also, you can use the ischecked() method to check if a checkbox is checked

# the following shows a complete program that diaplays a message in the console when a ckeckbox is checked or unchecked

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QCheckBox
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.setWindowTitle('CheckBox')
        self.setGeometry(100,100,320,210)
        
        layout = QGridLayout()
        self.setLayout(layout)
        
        checkbox = QCheckBox('I agree', self)
        checkbox.stateChanged.connect(self.on_check_changed)
        
        layout.addWidget(checkbox, 0, 0, Qt.AlignmentFlag.AlignCenter)
        
        self.show()
        
    def on_check_changed(self,value):
        state = Qt.CheckState(value)
        if state == Qt.CheckState.Checked:
            print('Ckecked')
            
        elif state == Qt.CheckState.Unchecked:
            print('Unchecked')
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())    