from PyQt5.QtWidgets import QMainWindow, QAction


class Gui(QMainWindow):

    def __init__(self):
        super().__init__()

    def initUI(self):
        self.statusBar().showMessage('Ready')

        menubar = self.menuBar()
        fichierMenu = menubar.add("Fichier")

        openAct = QAction("ouvrir",self)
        openAct.triggered.connect(self.open)
        openAct.detShortcut("O")
        openAct.setStatusTip("Ouvrir un fichier")

        recAct = QAction("Enregistrer", self)
        recAct.triggered.connect(self.rec)
        recAct.detShortcut("S")
        recAct.setStatusTip("Sauvegarder")

        quitAct = QAction("Quitter", self)
        quitAct.triggered.connect(self.quit)
        quitAct.detShortcut("C")
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
        self.quit



