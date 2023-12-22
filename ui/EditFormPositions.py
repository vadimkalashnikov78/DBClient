# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EditFormPositions.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form_Position(object):
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
        self.label_positionid = QLabel(Form)
        self.label_positionid.setObjectName(u"label_positionid")
        self.label_positionid.setMinimumSize(QSize(150, 0))

        self.horizontalLayout.addWidget(self.label_positionid)

        self.lineEdit_positionid = QLineEdit(Form)
        self.lineEdit_positionid.setObjectName(u"lineEdit_positionid")
        self.lineEdit_positionid.setEnabled(True)
        self.lineEdit_positionid.setMinimumSize(QSize(200, 0))
        self.lineEdit_positionid.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lineEdit_positionid)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_positionname = QLabel(Form)
        self.label_positionname.setObjectName(u"label_positionname")
        self.label_positionname.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_2.addWidget(self.label_positionname)

        self.lineEdit_positionname = QLineEdit(Form)
        self.lineEdit_positionname.setObjectName(u"lineEdit_positionname")
        self.lineEdit_positionname.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_2.addWidget(self.lineEdit_positionname)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_salarymin = QLabel(Form)
        self.label_salarymin.setObjectName(u"label_salarymin")
        self.label_salarymin.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_3.addWidget(self.label_salarymin)

        self.lineEdit_salarymin = QLineEdit(Form)
        self.lineEdit_salarymin.setObjectName(u"lineEdit_salarymin")

        self.horizontalLayout_3.addWidget(self.lineEdit_salarymin)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_salarymax = QLabel(Form)
        self.label_salarymax.setObjectName(u"label_salarymax")
        self.label_salarymax.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_4.addWidget(self.label_salarymax)

        self.lineEdit_salarymax = QLineEdit(Form)
        self.lineEdit_salarymax.setObjectName(u"lineEdit_salarymax")
        self.lineEdit_salarymax.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_4.addWidget(self.lineEdit_salarymax)


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
        self.label_positionid.setText(QCoreApplication.translate("Form", u"Position's ID", None))
        self.label_positionname.setText(QCoreApplication.translate("Form", u"Positions Name", None))
        self.label_salarymin.setText(QCoreApplication.translate("Form", u"Salary Min", None))
        self.label_salarymax.setText(QCoreApplication.translate("Form", u"Salary Max", None))
        self.pushButton_update.setText(QCoreApplication.translate("Form", u"Update", None))
        self.pushButton_New.setText(QCoreApplication.translate("Form", u"New", None))
        self.pushButton_Delete.setText(QCoreApplication.translate("Form", u"Delete", None))
    # retranslateUi

