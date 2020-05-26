from PySide2.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Calculator")
        self.setMinimumSize(400,400)
        self.layout = QGridLayout()

        self.linedit = QLineEdit()
        self.buttonC = QPushButton("C")
        self.buttonCE = QPushButton("CE")
        self.button7 = QPushButton("7")
        self.button8 = QPushButton("8")
        self.button9 = QPushButton("9")
        self.button10 = QPushButton("/")
        self.button4 = QPushButton("4")
        self.button5 = QPushButton("5")
        self.button6 = QPushButton("6")
        self.button11 = QPushButton("*")
        self.button1 = QPushButton("1")
        self.button2 = QPushButton("2")
        self.button3 = QPushButton("3")
        self.button12 = QPushButton("-")
        self.button0 = QPushButton("0")
        self.button13 = QPushButton(".")
        self.button14 = QPushButton("=")
        self.button15 = QPushButton("+")






        self.layout.addWidget(self.linedit,0,0,1,4)
        self.layout.addWidget(self.buttonC,1,0,1,2)
        self.layout.addWidget(self.buttonCE,1,2,1,2)
        self.layout.addWidget(self.button7,2,0)
        self.layout.addWidget(self.button8,2,1)
        self.layout.addWidget(self.button9,2,2)
        self.layout.addWidget(self.button10,2,3)
        self.layout.addWidget(self.button4,3,0)
        self.layout.addWidget(self.button5,3,1)
        self.layout.addWidget(self.button6,3,2)
        self.layout.addWidget(self.button11,3,3)
        self.layout.addWidget(self.button1,4,0)
        self.layout.addWidget(self.button2,4,1)
        self.layout.addWidget(self.button3,4,2)
        self.layout.addWidget(self.button12,4,3)
        self.layout.addWidget(self.button0,5,0)
        self.layout.addWidget(self.button13,5,1)
        self.layout.addWidget(self.button14,5,2)
        self.layout.addWidget(self.button15,5,3)

        self.button1.clicked.connect(self.button1)




        








        self.setLayout(self.layout)





if __name__ == "__main__":
    app = QApplication([])
    win = Window()
    win.show()
    app.exec_()
