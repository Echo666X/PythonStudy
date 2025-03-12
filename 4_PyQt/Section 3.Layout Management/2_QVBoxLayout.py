# in this tutorial, you’ll learn how to use the PyQt QVBoxLayout to arrange widgets vertically.

# the QVBoxlayout divides the parent wdget into vertial boxes and places the child widgets sequentially from top to buttom
# the following program illustrates how to use the QVBoxLayout class:
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.setWindowTitle('QVBoxLayout')
        self.setGeometry(100,100,320,210)
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        titles = ['Find Next','Find All', 'Close']
        buttons = [QPushButton(title) for title in titles]
        for button in buttons:
            layout.addWidget(button)
            
        self.show()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())