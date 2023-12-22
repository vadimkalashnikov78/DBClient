# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EditFormOrder.ui'
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

class Ui_Form_Order(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(378, 177)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_order_id = QLabel(Form)
        self.label_order_id.setObjectName(u"label_order_id")
        self.label_order_id.setMinimumSize(QSize(150, 0))

        self.horizontalLayout.addWidget(self.label_order_id)

        self.lineEdit_orderid = QLineEdit(Form)
        self.lineEdit_orderid.setObjectName(u"lineEdit_orderid")
        self.lineEdit_orderid.setEnabled(True)
        self.lineEdit_orderid.setMinimumSize(QSize(200, 0))
        self.lineEdit_orderid.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lineEdit_orderid)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_order_signedby = QLabel(Form)
        self.label_order_signedby.setObjectName(u"label_order_signedby")
        self.label_order_signedby.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_2.addWidget(self.label_order_signedby)

        self.lineEdit_signedby = QLineEdit(Form)
        self.lineEdit_signedby.setObjectName(u"lineEdit_signedby")
        self.lineEdit_signedby.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_2.addWidget(self.lineEdit_signedby)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_order_date = QLabel(Form)
        self.label_order_date.setObjectName(u"label_order_date")
        self.label_order_date.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_3.addWidget(self.label_order_date)

        self.dateEdit_orderdate = QDateEdit(Form)
        self.dateEdit_orderdate.setObjectName(u"dateEdit_orderdate")
        self.dateEdit_orderdate.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_3.addWidget(self.dateEdit_orderdate)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_order_number = QLabel(Form)
        self.label_order_number.setObjectName(u"label_order_number")
        self.label_order_number.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_4.addWidget(self.label_order_number)

        self.lineEdit_order_number = QLineEdit(Form)
        self.lineEdit_order_number.setObjectName(u"lineEdit_order_number")
        self.lineEdit_order_number.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_4.addWidget(self.lineEdit_order_number)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


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
        self.label_order_id.setText(QCoreApplication.translate("Form", u"Order's ID", None))
        self.label_order_signedby.setText(QCoreApplication.translate("Form", u"Signed By", None))
        self.label_order_date.setText(QCoreApplication.translate("Form", u"Order Date", None))
        self.label_order_number.setText(QCoreApplication.translate("Form", u"Order Number", None))
        self.pushButton_update.setText(QCoreApplication.translate("Form", u"Update", None))
        self.pushButton_New.setText(QCoreApplication.translate("Form", u"New", None))
        self.pushButton_Delete.setText(QCoreApplication.translate("Form", u"Delete", None))
    # retranslateUi

