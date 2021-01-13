import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QMessageBox
import os
from os import path
from PyPDF2 import PdfFileReader as pdf_reader
import pandas as pd

sources = []

def read_pdf(path, pdf):
    page_counter = pdf_reader(path).getNumPages()
    write(page_counter, path, pdf)

def write(page_counter, path, pdf):
    df = pd.DataFrame(page_counter, colums=['Paginas'])
    print(df)

def show_dialog(title, message):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText(message)
    msgBox.setWindowTitle(title)
    msgBox.show()
    returnValue = msgBox.exec()

def search_files_in_directory(path, extension):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extension):
                sources.append(os.path.join(root, file), file)
                #read_pdf(os.path.join(root, file), file)


class ejemplo_GUI(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.comenzar.clicked.connect(self.start)

    def start(self):              
        
        user_path = self.folder.toPlainText()

        if path.exists(user_path):
            search_files_in_directory(user_path, '.pdf')
        else:
            show_dialog('Alerta', 'El directorio no existe')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = ejemplo_GUI()
    GUI.show()
    sys.exit(app.exec_())