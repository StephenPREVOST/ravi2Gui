from PyQt5.QtWidgets import QMainWindow, QAction, QTabWidget, QWidget, QVBoxLayout, QPushButton


class OpenButton():
    pass


class MyTableWidget(QWidget):
    pass


class Gui(QMainWindow):

    def __init__(self, parent):
        super().__init__()
        self.initUI()
        self.title = 'RAVI 2'
        self.statusBar().showMessage('Ready')
        self.setWindowTitle(self.title)

        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)

        self.show()

        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()

        self.tabs.addTab(self.tab1, "Onglet 1")
        self.tabs.addTab(self.tab2, "Onglet 2")

        # Create first tab
        self.tab1.layout = QVBoxLayout(self)
        openButton = QPushButton("Nom ?")
        openButton.clicked.connect(self.openclick)

        self.tab1.layout.addWidget(openButton)
        self.tab1.setLayout(self.tab1.layout)
        self.tab1.setStyleSheet(("background-image: url(./flooop.png); background-attachment: fixed;"))

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)


    def initUI(self):
        menubar = self.menuBar()
        fichierMenu = menubar.addMenu("Fichier")

        openAct = QAction("ouvrir", self)
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

        self.setWindowTitle('RAVI 2')

        self.show()

    def open(self):
        print("open")

    def rec(self):
        print("rec")

    def quit(self):
        print("quit")
