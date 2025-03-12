# setting layout stretch factors
# the following program displays three QLabel widgets with different backgroud colors red, green,and blue using the QVBoxLayout

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        
        self.setWindowTitle('QVBoxLayout')
        self.setGeometry(100,100,500,400)
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        label_1 = QLabel('')
        label_1.setStyleSheet('QLabel{background-color:red}')
        label_2 = QLabel('')
        label_2.setStyleSheet('QLabel{background-color:green}')
        label_3 = QLabel('')
        label_3.setStyleSheet('QLabel{background-color:blue}')
        
        # label_list = [label_1,label_2,label_3]
        
        # for label in label_list:
        #     label.setFixedSize(100,50)
        #     label.setMinimumHeight(50)
        
        label_1.setText('red:')
        label_2.setText("green:")
        label_3.setText('blue:')
        
        layout.addWidget(label_1)
        layout.addWidget(label_2)
        layout.addWidget(label_3)
        
        # to allocate spaces for each QLabel widget proportionally,
        # you use the setStretch() method with the following syntax:
        # setStretchFactor(widget,factor)
        
        layout.setStretchFactor(label_1,1)
        layout.setStretchFactor(label_2,2)
        layout.setStretchFactor(label_3,3)
        
        # by default, the QVBoxLayout sets a default space between widgets
        # to change the spaces between widgets, you use the setSpacing() method
        # the following example uses the setSpacing() method to set the spaces between QLabel widgets to zero
        
        layout.setSpacing(0)
        
        # bydefault, the QVBoxLayout sets specific left, top, right, and bottom margins for a widget.
        # To change the margins, you use the setContentMargins() method:
        # setContentsMargins(self, left: int, top: int, right: int, bottom: int) -> None
        
        layout.setContentsMargins(10,10,10,10)
        
        self.show()
        
if __name__ =="__main__":
    app = QApplication(sys.argv)
    
    window = MainWindow()
    
    sys.exit(app.exec())