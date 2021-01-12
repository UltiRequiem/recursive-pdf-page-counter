from ventana_ui import *
class MainWindow(QtWidgets.QMainWindow):
    pass
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()