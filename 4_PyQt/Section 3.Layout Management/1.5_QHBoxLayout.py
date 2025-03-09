# Setting content margins
# By default, the QHBoxLayout sets specific left, top, right, and bottom margins for child widgets. 

# To change the margins, you use the setContentsMargins() method:
# setContentsMargins(self, left: int, top: int, right: int, bottom: int) -> None

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        
        self.setWindowTitle('QHBoxLayout')
        self.setGeometry(100,100,320,210)
        
        layout = QHBoxLayout()
        self.setLayout(layout)
        
        titles = ['YES','NO','CANCEL']
        buttons = [QPushButton(title) for title in titles]
        
        for button in buttons:
            layout.addWidget(button)
            
        layout.setContentsMargins(50,50,50,50)
        
        self.show()

if __name__ =='__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())