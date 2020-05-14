import sys
from PyQt5.QtWidgets import QMainWindow, QApplication


class Gui(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('Ready')

        self.setGeometry(300, 300, 1280, 720)
        self.setWindowTitle('RAVI_2')
        self.show()


