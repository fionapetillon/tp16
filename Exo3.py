from PySide2.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("IHM")
        self.setMinimumSize(400,200)

        self.layout = QVBoxLayout()
        self.clic =0


        self.button = QPushButton("Changer mon texte !")
        self.text = QTextEdit("Le nombre de clics va être affiché ici")

        self.layout.addWidget(self.button)
        self.layout.addWidget(self.text)
        self.button.clicked.connect(self.buttonClicked)



        self.setLayout(self.layout)

    def buttonClicked(self):

        self.clic += 1
        self.button.setText("Clic" + " " + str(self.clic))
        self.text.setText("Clic" + " " + str(self.clic))


if __name__ == "__main__":
    app = QApplication([])
    w = Window()
    w.show()
    app.exec_()


