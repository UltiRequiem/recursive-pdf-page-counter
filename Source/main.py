import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
import os
from os import path
from PyPDF2 import PdfFileReader as PdfReader
import csv


def read_pdf(root_folder, sources):
    results = []
    counter_pages = 0

    for source in sources:
        counter = PdfReader(source.get('path')).getNumPages()
        results.append([source.get('path'), source.get('file'), counter])
        counter_pages += counter

    results.append(['Total de paginas: ' + str(counter_pages)])
    write(os.path.join(root_folder, 'results.csv'), results)


def write(csv_location, items):
    with open(csv_location, 'w', newline='') as file:
        writer = csv.writer(file)
        for i in items:
            writer.writerow(i)
    show_dialog('Alerta', 'El proceso a terminado.')


def show_dialog(title, message):
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Information)
    msg_box.setText(message)
    msg_box.setWindowTitle(title)
    msg_box.show()
    msg_box.exec()


def search_files_in_directory(root_path, extension):
    sources = []
    for root, dirs, files in os.walk(root_path):
        for file in files:
            if file.endswith(extension):
                sources.append(
                    {'path': os.path.join(root, file), 'file': file})
    read_pdf(root_path, sources)


class EjemploGUI(QMainWindow):

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
    GUI = EjemploGUI()
    GUI.show()
    sys.exit(app.exec_())
