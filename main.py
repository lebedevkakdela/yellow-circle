import sys
from random import randrange
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor, QPolygon
from PyQt5.QtWidgets import QWidget, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.indicator = None
        self.setMouseTracking(True)
        self.coord = []

    def initUI(self):
        self.setGeometry(300, 300, randrange(100, 300), randrange(100, 300))
        self.setWindowTitle('Супрематизм')

    def mousePressEvent(self, event):
        if (event.button() == Qt.LeftButton):
            self.indicator = 1
        elif (event.button() == Qt.RightButton):
            self.indicator = 2
        self.update()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.indicator = 3
        self.update()

    def mouseMoveEvent(self, event):
        self.coord = [event.x(), event.y()]

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw(qp, self.indicator)
        qp.end()

    def draw(self, qp, indicator):
        a = randrange(5, 40)
        r, g, b = randrange(0, 255), randrange(0, 255), randrange(0, 255)
        qp.setBrush(QColor(r, g, b))
        if indicator == 1:
            qp.drawEllipse(*self.coord, a, a)
        if indicator == 2:
            qp.drawRect(*self.coord, a, a)
        if indicator == 3:
            point = QPolygon([
                QPoint(self.coord[0], self.coord[1] - a),
                QPoint(self.coord[0] - a, self.coord[1] + a),
                QPoint(self.coord[0] + a, self.coord[1] + a)])
            qp.drawPolygon(point)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
