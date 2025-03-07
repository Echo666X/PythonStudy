import sys
from PyQt6.QtWidgets import QApplication, QWidget

class Mainwindow(QWidget):  # define the MainWindow class that inherits from the Qwiget
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        
    # set the window title
        self.setWindowTitle('Hello World')
    
    # show the window
        self.show()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # create the main window
    window = Mainwindow()
    
    # start the event loop
    sys.exit(app.exec())