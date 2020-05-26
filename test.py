from PySide2.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Calculator")
        self.setMinimumSize(600,300)
        self.layout = QGridLayout()




