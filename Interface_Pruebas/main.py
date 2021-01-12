from PyQt5 import QtWidgets, uic

import sys

app = QtWidgets.QApplication([])

win = uic.loadUi("main.ui") #specify the location of your .ui file

win.show()

print(win.folder)
sys.exit(app.exec())