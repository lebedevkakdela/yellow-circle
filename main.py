import sys
from random import randrange
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.indicator = 0
        self.coord = [380, 230]
        self.pushButton.clicked.connect(self.pluser)

    def pluser(self):
        self.indicator = 1
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        if self.indicator == 1:
            self.draw(qp, 1)
        qp.end()

    def draw(self, qp, indicator):
        a = randrange(5, 40)
        qp.setBrush(QColor(255, 255, 0))
        if indicator == 1:
            qp.drawEllipse(*self.coord, a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
