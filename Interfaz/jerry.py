import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import os
from os import path

class ejemplo_GUI(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.comenzar.clicked.connect(self.read_directory)
       

    def read_directory(self):       
        user_path = self.folder.toPlainText()

        if path.exists(user_path):
            for root, dirs, files in os.walk(user_path):
                for file in files:
                    if file.endswith(".pdf"):
                        print(os.path.join(root, file))

        else:
            print('El Directorio no Existe')

                

        #C:\\Users\eliaz\Desktop\Repositorios\gg\mydir




if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = ejemplo_GUI()
    GUI.show()
    sys.exit(app.exec_())