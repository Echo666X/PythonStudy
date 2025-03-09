# alignments
# to keep the child widgets at their default sizes and align them horizontally, you use a horizonal spacer

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout,QVBoxLayout

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        
        self.setWindowTitle('QHBoxLayout')
        self.setGeometry(100,200,320,210)
        
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        
        
        
       # align left 
        layout_1 = QHBoxLayout()
        self.setLayout(layout_1)
        
        titles1 = ['Yes','No','Left']
        buttons1 = [QPushButton(title) for title in titles1]
        for button in buttons1:
            layout_1.addWidget(button)
        # to add a horizontal spacer to the end of the layout, you call the addStretch() method after adding all buttons to the layout
        layout_1.addStretch()
        #添加到主布局
        main_layout.addLayout(layout_1) 
        
        
        
        #align right
        layout_2 = QHBoxLayout()
        self.setLayout(layout_2)
        
        # similarly, you can add a spacer at the beginning of the layout to push the buttons to the right
        layout_2.addStretch()
        titles2 = ['Yes','No','Right']
        buttons2 = [QPushButton(title) for title in titles2]
        for button in buttons2:
            layout_2.addWidget(button)
        main_layout.addLayout(layout_2)   
        
        
        
        #align center
        layout_3 = QHBoxLayout()
        self.setLayout(layout_3)
        
        #To align buttons to the center, you add one horizontal spacer at the beginning and the other at the end of the layout:
        layout_3.addStretch()
        titiles_3 = ['Yes','No','Center']
        buttons3 = [QPushButton(title) for title in titiles_3]
        for button in buttons3:
            layout_3.addWidget(button)
        layout_3.addStretch()
        main_layout.addLayout(layout_3)
        
        
        self.show()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())