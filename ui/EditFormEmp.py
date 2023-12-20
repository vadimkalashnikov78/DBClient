# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EditFormEmp.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form_Emp(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(378, 224)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_emp_id = QLabel(Form)
        self.label_emp_id.setObjectName(u"label_emp_id")
        self.label_emp_id.setMinimumSize(QSize(150, 0))

        self.horizontalLayout.addWidget(self.label_emp_id)

        self.lineEdit_empid = QLineEdit(Form)
        self.lineEdit_empid.setObjectName(u"lineEdit_empid")
        self.lineEdit_empid.setEnabled(True)
        self.lineEdit_empid.setMinimumSize(QSize(200, 0))
        self.lineEdit_empid.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lineEdit_empid)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_emp_name = QLabel(Form)
        self.label_emp_name.setObjectName(u"label_emp_name")
        self.label_emp_name.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_2.addWidget(self.label_emp_name)

        self.lineEdit_empname = QLineEdit(Form)
        self.lineEdit_empname.setObjectName(u"lineEdit_empname")
        self.lineEdit_empname.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_2.addWidget(self.lineEdit_empname)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_birth_date = QLabel(Form)
        self.label_birth_date.setObjectName(u"label_birth_date")
        self.label_birth_date.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_3.addWidget(self.label_birth_date)

        self.dateEdit_emp_birthdate = QDateEdit(Form)
        self.dateEdit_emp_birthdate.setObjectName(u"dateEdit_emp_birthdate")
        self.dateEdit_emp_birthdate.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_3.addWidget(self.dateEdit_emp_birthdate)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_regaddress = QLabel(Form)
        self.label_regaddress.setObjectName(u"label_regaddress")
        self.label_regaddress.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_4.addWidget(self.label_regaddress)

        self.lineEdit_regaddress = QLineEdit(Form)
        self.lineEdit_regaddress.setObjectName(u"lineEdit_regaddress")
        self.lineEdit_regaddress.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_4.addWidget(self.lineEdit_regaddress)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_emp_phone = QLabel(Form)
        self.label_emp_phone.setObjectName(u"label_emp_phone")
        self.label_emp_phone.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_5.addWidget(self.label_emp_phone)

        self.lineEdit_emp_phone = QLineEdit(Form)
        self.lineEdit_emp_phone.setObjectName(u"lineEdit_emp_phone")
        self.lineEdit_emp_phone.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_5.addWidget(self.lineEdit_emp_phone)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_emp_mail = QLabel(Form)
        self.label_emp_mail.setObjectName(u"label_emp_mail")
        self.label_emp_mail.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_6.addWidget(self.label_emp_mail)

        self.lineEdit_emp_mail = QLineEdit(Form)
        self.lineEdit_emp_mail.setObjectName(u"lineEdit_emp_mail")
        self.lineEdit_emp_mail.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_6.addWidget(self.lineEdit_emp_mail)


        self.verticalLayout.addLayout(self.horizontalLayout_6)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_update = QPushButton(Form)
        self.pushButton_update.setObjectName(u"pushButton_update")

        self.horizontalLayout_7.addWidget(self.pushButton_update)

        self.pushButton_New = QPushButton(Form)
        self.pushButton_New.setObjectName(u"pushButton_New")

        self.horizontalLayout_7.addWidget(self.pushButton_New)

        self.pushButton_Delete = QPushButton(Form)
        self.pushButton_Delete.setObjectName(u"pushButton_Delete")

        self.horizontalLayout_7.addWidget(self.pushButton_Delete)


        self.gridLayout.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_emp_id.setText(QCoreApplication.translate("Form", u"Employee's ID", None))
        self.label_emp_name.setText(QCoreApplication.translate("Form", u"Employee's Name", None))
        self.label_birth_date.setText(QCoreApplication.translate("Form", u"Birth Date", None))
        self.label_regaddress.setText(QCoreApplication.translate("Form", u"Registration Address", None))
        self.label_emp_phone.setText(QCoreApplication.translate("Form", u"Contact Phone", None))
        self.label_emp_mail.setText(QCoreApplication.translate("Form", u"E-mail", None))
        self.pushButton_update.setText(QCoreApplication.translate("Form", u"Update", None))
        self.pushButton_New.setText(QCoreApplication.translate("Form", u"New", None))
        self.pushButton_Delete.setText(QCoreApplication.translate("Form", u"Delete", None))
    # retranslateUi

