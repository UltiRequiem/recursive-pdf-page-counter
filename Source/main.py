import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QMessageBox
import os
from os import path
from PyPDF2 import PdfFileReader as pdf_reader
import pandas as pd
import csv

sources = []
results = []


def read_pdf(root_folder):

    counter_pages = 0

    for source in sources:
        counter = pdf_reader(source.get('path')).getNumPages()
        results.append([source.get('path'), source.get('file'), counter])
        counter_pages += counter

    results.append(['Total de paginas: ' + str(counter_pages)])
    write(os.path.join(root_folder, 'results.csv'))


def write(csv_location):
    with open(csv_location, 'w', newline='') as file:
        writer = csv.writer(file)
        for i in results:
            writer.writerow(i)
    show_dialog('Alerta', 'El proceso a terminado.')


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
                sources.append(
                    {'path': os.path.join(root, file), 'file': file})
    read_pdf(path)


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
