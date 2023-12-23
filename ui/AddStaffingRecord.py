# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddStaffingRecord.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form_Staff(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(332, 289)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(11, 11, 310, 268))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_emp = QLabel(self.widget)
        self.label_emp.setObjectName(u"label_emp")
        self.label_emp.setMinimumSize(QSize(100, 0))
        font = QFont()
        font.setBold(True)
        self.label_emp.setFont(font)

        self.horizontalLayout.addWidget(self.label_emp)

        self.comboBox_emp = QComboBox(self.widget)
        self.comboBox_emp.setObjectName(u"comboBox_emp")
        self.comboBox_emp.setMinimumSize(QSize(200, 0))

        self.horizontalLayout.addWidget(self.comboBox_emp)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_pos = QLabel(self.widget)
        self.label_pos.setObjectName(u"label_pos")
        self.label_pos.setMinimumSize(QSize(100, 0))
        self.label_pos.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_pos)

        self.comboBox_pos = QComboBox(self.widget)
        self.comboBox_pos.setObjectName(u"comboBox_pos")
        self.comboBox_pos.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_2.addWidget(self.comboBox_pos)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_div = QLabel(self.widget)
        self.label_div.setObjectName(u"label_div")
        self.label_div.setMinimumSize(QSize(100, 0))
        self.label_div.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_div)

        self.comboBox_div = QComboBox(self.widget)
        self.comboBox_div.setObjectName(u"comboBox_div")
        self.comboBox_div.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_3.addWidget(self.comboBox_div)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_fte = QLabel(self.widget)
        self.label_fte.setObjectName(u"label_fte")
        self.label_fte.setMinimumSize(QSize(100, 0))
        self.label_fte.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_fte)

        self.lineEdit_fte = QLineEdit(self.widget)
        self.lineEdit_fte.setObjectName(u"lineEdit_fte")
        self.lineEdit_fte.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_4.addWidget(self.lineEdit_fte)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_salary = QLabel(self.widget)
        self.label_salary.setObjectName(u"label_salary")
        self.label_salary.setMinimumSize(QSize(100, 0))
        self.label_salary.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_salary)

        self.lineEdit_salary = QLineEdit(self.widget)
        self.lineEdit_salary.setObjectName(u"lineEdit_salary")
        self.lineEdit_salary.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_5.addWidget(self.lineEdit_salary)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_date = QLabel(self.widget)
        self.label_date.setObjectName(u"label_date")
        self.label_date.setMinimumSize(QSize(100, 0))
        self.label_date.setFont(font)

        self.horizontalLayout_6.addWidget(self.label_date)

        self.dateEdit = QDateEdit(self.widget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setEnabled(True)
        font1 = QFont()
        font1.setBold(False)
        self.dateEdit.setFont(font1)
        self.dateEdit.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.dateEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_div_2 = QLabel(self.widget)
        self.label_div_2.setObjectName(u"label_div_2")
        self.label_div_2.setMinimumSize(QSize(100, 0))
        self.label_div_2.setFont(font)

        self.horizontalLayout_7.addWidget(self.label_div_2)

        self.comboBox_event = QComboBox(self.widget)
        self.comboBox_event.addItem("")
        self.comboBox_event.addItem("")
        self.comboBox_event.setObjectName(u"comboBox_event")

        self.horizontalLayout_7.addWidget(self.comboBox_event)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_div_3 = QLabel(self.widget)
        self.label_div_3.setObjectName(u"label_div_3")
        self.label_div_3.setMinimumSize(QSize(100, 0))
        self.label_div_3.setFont(font)

        self.horizontalLayout_8.addWidget(self.label_div_3)

        self.lineEdit_order = QLineEdit(self.widget)
        self.lineEdit_order.setObjectName(u"lineEdit_order")
        self.lineEdit_order.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_8.addWidget(self.lineEdit_order)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pushButton_Save = QPushButton(self.widget)
        self.pushButton_Save.setObjectName(u"pushButton_Save")

        self.horizontalLayout_9.addWidget(self.pushButton_Save)

        self.pushButton_Cancel = QPushButton(self.widget)
        self.pushButton_Cancel.setObjectName(u"pushButton_Cancel")

        self.horizontalLayout_9.addWidget(self.pushButton_Cancel)


        self.verticalLayout.addLayout(self.horizontalLayout_9)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_emp.setText(QCoreApplication.translate("Form", u"Employee", None))
        self.label_pos.setText(QCoreApplication.translate("Form", u"Position", None))
        self.label_div.setText(QCoreApplication.translate("Form", u"Division", None))
        self.label_fte.setText(QCoreApplication.translate("Form", u"FTE = ", None))
        self.label_salary.setText(QCoreApplication.translate("Form", u"Salary", None))
        self.label_date.setText(QCoreApplication.translate("Form", u"CurrentDate", None))
        self.label_div_2.setText(QCoreApplication.translate("Form", u"Event type", None))
        self.comboBox_event.setItemText(0, QCoreApplication.translate("Form", u"Hired", None))
        self.comboBox_event.setItemText(1, QCoreApplication.translate("Form", u"Fired", None))

        self.label_div_3.setText(QCoreApplication.translate("Form", u"OrderId", None))
        self.pushButton_Save.setText(QCoreApplication.translate("Form", u"Save", None))
        self.pushButton_Cancel.setText(QCoreApplication.translate("Form", u"Cancel", None))
    # retranslateUi

