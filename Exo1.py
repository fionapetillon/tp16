from PySide2.QtWidgets import *
import random

class Window(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("Cycles de l'ISEN Yncréa Ouest")
        self.setMinimumSize(500,300)
        self.layout = QVBoxLayout()

        self.button = QPushButton("Changer de cycle")
        self.liste=["CSI","CIR","BIOST","BIAST","CENT","EST"]

        self.label = QLabel(random.choice(self.liste))



        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.connexion)

        self.setLayout(self.layout)

    def connexion(self):
        self.label.setText(random.choice(self.liste))


if __name__ == "__main__":
    app = QApplication([])
    w=Window()
    w.show()
    app.exec_()




