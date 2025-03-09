# Setting spaces between widgets

# by default,  the QHBoxLayout sets a default space between the child widgets, to change the spaces between them,
# you use the setSpacing() method of the QHBoxLayout object

import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QHBoxLayout, QWidget

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.setWindowTitle('QHBoxlayout')
        self.setGeometry(100,100,320,210)
        
        layout = QHBoxLayout()
        self.setLayout(layout)
        
        titles = ['Yes', 'No', 'Cancel']
        buttons = [QPushButton(title) for title in titles]
        
        for button in buttons:
            layout.addWidget(button)
        
        # set the spaces between buttons to 50px:
        layout.setSpacing(50)
        
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())