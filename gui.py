from PyQt5.QtWidgets import QMainWindow, QAction, QWidget, QTabWidget, QVBoxLayout, QPushButton


class MyTableWidget(QWidget):
        pass



class Gui(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.title = 'RAVI 2'
        self.statusBar().showMessage('Ready')

        self.show()



    def initUI(self):

        menubar = self.menuBar()
        fichierMenu = menubar.addMenu("Fichier")

        openAct = QAction("ouvrir",self)
        openAct.triggered.connect(self.open)
        openAct.setShortcut("O")
        openAct.setStatusTip("Ouvrir un fichier")

        recAct = QAction("Enregistrer", self)
        recAct.triggered.connect(self.rec)
        recAct.setShortcut("S")
        recAct.setStatusTip("Sauvegarder")

        quitAct = QAction("Quitter", self)
        quitAct.triggered.connect(self.quit)
        quitAct.setShortcut("C")
        quitAct.setStatusTip("Fermer la fenêtre")

        fichierMenu.addAction(openAct)
        fichierMenu.addAction(recAct)
        fichierMenu.addAction(quitAct)

        self.setGeometry(300, 300, 1280, 720)

        self.setWindowTitle('RAVI_2')


        self.show()

    def open(self):
        print("open")

    def rec(self):
        print("rec")

    def quit(self):
        print("quit")




