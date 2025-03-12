# Creating a tristate checkbox

# besides checked and unchecked, a QcheckBox supports the third state that indicates 'no change', in this case, a checkbox has three states
# checked; unchecked, partially checked

# in practice, you use a tristate checkbox to give the user the option of neither checking nor unchecking the checkbox
# to creaate a tristae checkbox, you use the setTristate() tO True

# the following program shows a tristate checkbos:
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QGridLayout
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        self.setWindowTitle('A Tristate Checkbox')
        self.setGeometry(100,100,320,210)
        
        layout = QGridLayout()
        self.setLayout(layout)
        
        
        self.checkbox = QCheckBox('A Tristate Box', self)
        self.checkbox.setTristate(True)
        
        layout.addWidget(self.checkbox,0,0,Qt.AlignmentFlag.AlignCenter)
        
        self.show()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())