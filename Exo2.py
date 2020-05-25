from PySide2.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("IHM")
        self.setMinimumSize(400,200)

        self.layout = QHBoxLayout()

        self.slider = QSlider()
        self.bar = QProgressBar()

        self.slider.valueChanged.connect(self.signaux)

        self.layout.addWidget(self.bar)
        self.layout.addWidget(self.slider)

        self.setLayout(self.layout)


    def signaux(self):
        self.bar.setValue(self.slider.value())






if __name__ == "__main__":
    app = QApplication([])
    w= Window()
    w.show()
    app.exec_()


