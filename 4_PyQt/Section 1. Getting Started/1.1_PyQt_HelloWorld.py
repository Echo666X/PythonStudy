# A PyQt program may accept one or more command line arguments.
# To enable this, you need to pass the argv from the sys module to the QApplication like this

import sys
from PyQt6.QtWidgets import QApplication, QWidget


# create the QApplication
app = QApplication(sys.argv)

# create the main window
window = QWidget(windowTitle='Hello World')
window.show()

# start the event loop
sys.exit(app.exec())