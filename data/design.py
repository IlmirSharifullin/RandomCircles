import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QMenuBar, QMenu, QStatusBar, QApplication

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class Design(QMainWindow):
    def setupUI(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(500, 500)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btn = QPushButton(self.centralwidget)
        self.btn.setGeometry(QtCore.QRect(220, 450, 75, 23))
        self.btn.setObjectName(_fromUtf8("pushButton"))
        self.btn.setText('Нажми меня')

        QtCore.QMetaObject.connectSlotsByName(MainWindow)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = Design()
    main_win.show()
    app.exec()