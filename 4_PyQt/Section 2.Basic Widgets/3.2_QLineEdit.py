# 3) Using the PyQt QLineEdit with the auto-complete feature

# you follow these steps to create an entry with the auto-complete feature
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QCompleter
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.setWindowTitle('PyQt QLineEdit Widget')
        self.setGeometry(100,100,320,210)
        
        common_fruits = QCompleter([
            'Apple',
            'Apricot',
            'Banana',
            'Carambola',
            'Olive',
            'Oranges',
            'Papaya',
            'Peach',
            'Pineapple',
            'Pomegranate',
            'Rambutan',
            'Ramphal',
            'Raspberries',
            'Rose apple',
            'Starfruit',
            'Strawberries',
            'Water apple',
        ])
        
        common_fruits.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        fruit = QLineEdit(self)
        fruit.setCompleter(common_fruits)
        
        
        layout = QVBoxLayout()
        layout.addWidget(fruit)
        self.setLayout(layout)
        
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())