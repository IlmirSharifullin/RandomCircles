import random
import sys

from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget
from data.design import Design


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Design()
        self.ui.setupUI(self)
        self.ui.btn.clicked.connect(self.paint)
        self.painting = False

    def paint(self):
        self.painting = True
        self.repaint()

    def paintEvent(self, event):
        if self.painting:
            qp = QPainter()
            qp.begin(self)
            self.draw_circles(qp)
            qp.end()
            self.painting = False

    def draw_circles(self, qpainter: QPainter):
        color = [random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256)]
        qpainter.setBrush(QColor(*color))
        r = random.randrange(10, 200)
        x = random.randrange(r, 500 - 200)
        y = random.randrange(r, 500 - 200)
        qpainter.drawEllipse(QPoint(x, y), r, r)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
