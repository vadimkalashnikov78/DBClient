from PySide6 import QtWidgets


class NewEmpForm(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

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

        pushbutton_ok = QtWidgets.QPushButton()
        pushbutton_ok.setText("OK")

        pushbutton_cancel = QtWidgets.QPushButton()
        pushbutton_cancel.setText("Cancel")

        layout3 = QtWidgets.QHBoxLayout()
        layout3.addWidget(pushbutton_ok)
        layout3.addWidget(pushbutton_cancel)

        # Создание главного layout
        layout_main = QtWidgets.QVBoxLayout()
        layout_main.addLayout(layout1)
        layout_main.addLayout(layout2)
        layout_main.addLayout(layout3)

        self.setLayout(layout_main)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    new_form = NewEmpForm()
    new_form.show()

    app.exec()
