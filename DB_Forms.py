from PySide6 import QtWidgets


class NewEmpForm(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.newUserSQL = ''

        self.setWindowTitle("New Employee")
        self.setMaximumSize(500, 600)

        label1 = QtWidgets.QLabel()
        label1.setText("Enter your Employee Name")
        self.lineEdit1 = QtWidgets.QLineEdit()
        layout1 = QtWidgets.QHBoxLayout()
        layout1.addWidget(label1)
        layout1.addWidget(self.lineEdit1)

        label2 = QtWidgets.QLabel()
        label2.setText("Enter your Employee Birthdate")
        self.lineEdit2 = QtWidgets.QLineEdit()
        layout2 = QtWidgets.QHBoxLayout()
        layout2.addWidget(label2)
        layout2.addWidget(self.lineEdit2)

        self.pushbutton_ok = QtWidgets.QPushButton()
        self.pushbutton_ok.setText("OK")

        self.pushbutton_cancel = QtWidgets.QPushButton()
        self.pushbutton_cancel.setText("Cancel")

        layout3 = QtWidgets.QHBoxLayout()
        layout3.addWidget(self.pushbutton_ok)
        layout3.addWidget(self.pushbutton_cancel)

        # Создание главного layout
        layout_main = QtWidgets.QVBoxLayout()
        layout_main.addLayout(layout1)
        layout_main.addLayout(layout2)
        layout_main.addLayout(layout3)

        self.setLayout(layout_main)
        self.initButtons()

    def initButtons(self) -> None:
        self.pushbutton_ok.clicked.connect(self.onPushButtonOKClicked)
        self.pushbutton_cancel.clicked.connect(self.onPushButtonCancelClicked)

    def onPushButtonCancelClicked(self) -> None:
        self.close()

    def onPushButtonOKClicked(self) -> None:
        self.newUserSQL = f'{self.lineEdit1.text()}, {self.lineEdit2.text()}'
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    new_form = NewEmpForm()
    new_form.show()

    app.exec()
