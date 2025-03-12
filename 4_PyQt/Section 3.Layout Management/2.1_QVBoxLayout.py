# The QVBoxLayout stretches each widget type in a specific way. 
# For example, the QVBoxLayout stretches the QPushButton horizontally, not vertically.

# it means that when you increase the width of the parent widget, the widths of all the buttons also increase
# however, when you increase the height of the parent widget, the heights of the buttons doesn't change
# more importantly, the QVBoxLayout allcotes evenly the spaces of the parent widget to each other

# when the parent widget has more space for the child widgets, 
# you can align the child widgets within the parent widget using vertical spacers

import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QHBoxLayout, QWidget

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.setWindowTitle('QVBoxLayout Alighment')
        self.setGeometry(100,100,800,320)
        
        main_layout = QHBoxLayout()
        self.setLayout(main_layout)
        
        # Align bottom
        # to push the buttons to the bottom of the parent widget, you add a vertical spacer at the beginning of the layout
        layout_1 = QVBoxLayout()
    
        layout_1.addStretch()
        
        titles_1 = ['Find Next', 'Find All', 'Close']
        buttons_1 = [QPushButton(title) for title in titles_1]
        
        for button in buttons_1:
            layout_1.addWidget(button)
        
        # Align top
        #Similarly, you can add a vertical spacer as the last item of the layout to push the buttons to the top 
        layout_2 = QVBoxLayout()
        
        titles_2 = ['Find Next', 'Find All', 'Close']
        buttons_2 = [QPushButton(title) for title in titles_2]
        
        for button in  buttons_2:
            layout_2.addWidget(button)
        
        layout_2.addStretch()
        
        # Align center
        # To align the buttons in the center of the parent widget, 
        # you add a vertical spacer at the beginning and one at the end of the layout like this:
        layout_3 = QVBoxLayout()
        
        titles_3 = ['Find Next', 'Find All', 'Close']
        buttons_3 = [QPushButton(title) for title in titles_3]
        
        layout_3.addStretch()
        
        for button in buttons_3:
            layout_3.addWidget(button)
            
        layout_3.addStretch()
        
        # note that you can add a vertical spacer between the widgets in the QVBoxLayout
        # for exmaple, the following adds a vertical spacer between the second and third buttons
        layout_4 = QVBoxLayout()
        
        titles_4 = ['Find Next', 'Find All', 'Close']
        buttons_4 = [QPushButton(title) for title in titles_4]
        
        layout_4.addWidget(buttons_4[0])
        layout_4.addWidget(buttons_4[1])
        
        layout_4.addStretch()
        
        layout_4.addWidget(buttons_4[2])
        
        
        main_layout.addLayout(layout_1)
        main_layout.addLayout(layout_2)
        main_layout.addLayout(layout_3)
        main_layout.addLayout(layout_4)
        
        self.show()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())