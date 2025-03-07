# Creating a toggle button

# the introduction to toggle button
# the QPushButton class has the checkable property that allows you to use the button as a toggle button
# a toggle button has an on/off state, if the button is on, the checked button is true, otherwise, it is false.
# for a toggle button, the clicked signal sends the status of the button, either on or off

# the following program displays a window that has a toggle button

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.setWindowTitle('PyQt QPushButton Widget')
        self.setGeometry(100,100,320,210)
        
        button = QPushButton('Toggle Me')
        button.setCheckable(True)
        button.clicked.connect(self.on_toggle)
        
        layout = QVBoxLayout()
        layout.addWidget(button)
        self.setLayout(layout)
        
        self.show()
        
    def on_toggle(self,checked):
        print(checked)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = MainWindow()
    
    sys.exit(app.exec())