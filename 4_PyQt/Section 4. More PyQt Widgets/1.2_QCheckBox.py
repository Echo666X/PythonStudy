# Setting checked or unchecked of PyQt QCheckBox programmatically
# the Qcheckbox class has the setchecked() method that allows you to check or uncheck a check box programmatically

# if you ass True to the setChecked() method, the checkbox will be checked
# however, if you pass False to the setcheck() method, the checkbox will be unchecked

# also, you can use the setcheckstate() method of the Qcheckbox class to set the state of the checkbox
# the setcheckstate method accepts one of three state values of the Qt.CheckState enum

# the following program illustrates how to use the setchecked() method to check and uncheck a checkbox:
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QPushButton, QGridLayout
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        self.setWindowTitle('QCheckBox')
        self.setGeometry(100,100,320,210)
        
        layout = QGridLayout()
        self.setLayout(layout)
        
        self.checkbox = QCheckBox('I agree', self)
        
        check_button = QPushButton('Check')
        check_button.clicked.connect(self.check)
        
        uncheck_button = QPushButton('Uncheck')
        uncheck_button.clicked.connect(self.uncheck)
        
        layout.addWidget(self.checkbox, 0, 0, 0, 2,
                         Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(check_button, 1, 0)
        layout.addWidget(uncheck_button, 1, 1)
        
        self.show()
        
    def check(self):
        self.checkbox.setChecked(True)
        
    def uncheck(self):
        self.checkbox.setChecked(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())