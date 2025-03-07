# A signal may carry data that provides the state of the object when the event occurs. 
# For example, the textChanged signal of the QLineEdit has the text entered in the widget.

import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QVBoxLayout
)


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Qt Signals & Slots')

        # create widgets
        label = QLabel()
        line_edit = QLineEdit()
        line_edit.textChanged.connect(label.setText)

        # place the widgets
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(line_edit)
        self.setLayout(layout)

        # show the window
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())