from PyQt5 import QtWidgets

from design2 import Ui_PDFtoCSV  # importing our generated file



import sys

class Ui_PDFtoCSV(QtWidgets.QMainWindow):

    def __init__(self):

        super(PDFtoCSV, self).__init__()

        self.ui = Ui_MainWindow()
    
        self.ui.setupUi(self)

app = QtWidgets.QApplication([])

application = Ui_PDFtoCSV()

application.show()

sys.exit(app.exec())