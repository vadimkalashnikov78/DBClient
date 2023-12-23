# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EditFormDivisions.ui'
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

class Ui_Form_Divisions(object):
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
        self.label_divisionid = QLabel(Form)
        self.label_divisionid.setObjectName(u"label_divisionid")
        self.label_divisionid.setMinimumSize(QSize(150, 0))

        self.horizontalLayout.addWidget(self.label_divisionid)

        self.lineEdit_divisionid = QLineEdit(Form)
        self.lineEdit_divisionid.setObjectName(u"lineEdit_divisionid")
        self.lineEdit_divisionid.setEnabled(True)
        self.lineEdit_divisionid.setMinimumSize(QSize(200, 0))
        self.lineEdit_divisionid.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lineEdit_divisionid)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_divisionname = QLabel(Form)
        self.label_divisionname.setObjectName(u"label_divisionname")
        self.label_divisionname.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_2.addWidget(self.label_divisionname)

        self.lineEdit_divisionname = QLineEdit(Form)
        self.lineEdit_divisionname.setObjectName(u"lineEdit_divisionname")
        self.lineEdit_divisionname.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_2.addWidget(self.lineEdit_divisionname)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_boss = QLabel(Form)
        self.label_boss.setObjectName(u"label_boss")
        self.label_boss.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_3.addWidget(self.label_boss)

        self.lineEdit_bossname = QLineEdit(Form)
        self.lineEdit_bossname.setObjectName(u"lineEdit_bossname")

        self.horizontalLayout_3.addWidget(self.lineEdit_bossname)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_status = QLabel(Form)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_4.addWidget(self.label_status)

        self.lineEdit_status = QLineEdit(Form)
        self.lineEdit_status.setObjectName(u"lineEdit_status")
        self.lineEdit_status.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_4.addWidget(self.lineEdit_status)


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
        self.label_divisionid.setText(QCoreApplication.translate("Form", u"Division's ID", None))
        self.label_divisionname.setText(QCoreApplication.translate("Form", u"Division's Name", None))
        self.label_boss.setText(QCoreApplication.translate("Form", u"Boss Name", None))
        self.label_status.setText(QCoreApplication.translate("Form", u"Status", None))
        self.pushButton_update.setText(QCoreApplication.translate("Form", u"Update", None))
        self.pushButton_New.setText(QCoreApplication.translate("Form", u"New", None))
        self.pushButton_Delete.setText(QCoreApplication.translate("Form", u"Delete", None))
    # retranslateUi

