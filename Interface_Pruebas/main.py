from PyQt5 import *

from main5 import *
import sys
from os import *

#----------------------------------------------------------------------------------------------------------------------------------------------------------   
class mywindow(QtWidgets.QMainWindow):

    def mela2(self):
            mai = self.folder
            print(mai)

    def __init__(self):

        super(mywindow, self).__init__()

        self.ui = Ui_MainWindow()
    
        self.ui.setupUi(self)

        #print(self.folder.values)
    
    


app = QtWidgets.QApplication([])

application = mywindow()
application.mela2()
application.show()

sys.exit(app.exec())



#----------------------------------------------------------------------------------------------------------------------------------------------------------


