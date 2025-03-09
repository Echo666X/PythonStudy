# Setting layout stretch factors
# by default, a child widget takes its default size, to set the space that the child wifget can stretch
# you call the setStretchFactor() method of the QHBoxlayout object

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        
        self.setWindowTitle('QHBoxLayout')
        self.setGeometry(100,100,320,210)
        
        layout = QHBoxLayout()
        self.setLayout(layout)
        
        titles = ['Yes','No','Cancel']
        buttons = [QPushButton(title) for title in titles]
        
        for button in buttons:
            layout.addWidget(button)
            
        layout.setStretchFactor(buttons[0],2)
        layout.setStretchFactor(buttons[1],2)
        layout.setStretchFactor(buttons[2],1)
        
        self.show()
        
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    sys.exit(app.exec())