import sys

from PySide6 import QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.do_something()  # sanity check
        self.cw = ChildWidget(self)
        self.setCentralWidget(self.cw)
        self.show()

    @staticmethod
    def do_something():
        print('doing something!')


class ChildWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(ChildWidget, self).__init__(parent)
        self.button1 = QtWidgets.QPushButton()
        self.button1.clicked.connect(self.do_something_else)
        self.button2 = QtWidgets.QPushButton()
        self.button2.clicked.connect(self.parent().do_something)
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.setLayout(self.layout)
        self.show()

    @staticmethod
    def do_something_else():
        print('doing something else!')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    app.exec()
