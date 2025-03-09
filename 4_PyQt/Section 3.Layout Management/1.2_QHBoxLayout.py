# placing a horizonal spacer between widgets
# it is possible to place the horizontal spacer between widgets to push them to the left and right of the layout

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.setWindowTitle('QHBoxlayout')
        self.setGeometry(100,100,320,210)
        layout = QHBoxLayout()
        self.setLayout(layout)
        
        titles = ['Yes','No','Cancel']
        buttons = [QPushButton(title) for title in titles]
        
        layout.addWidget(buttons[0])
        layout.addWidget(buttons[1])
        
        layout.addStretch()
        
        layout.addWidget(buttons[2])
        
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())