# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConnectionForm.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(369, 360)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_server_name = QLabel(Form)
        self.label_server_name.setObjectName(u"label_server_name")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_server_name.sizePolicy().hasHeightForWidth())
        self.label_server_name.setSizePolicy(sizePolicy)
        self.label_server_name.setMinimumSize(QSize(100, 0))

        self.horizontalLayout.addWidget(self.label_server_name)

        self.lineEdit_servername = QLineEdit(Form)
        self.lineEdit_servername.setObjectName(u"lineEdit_servername")
        self.lineEdit_servername.setMinimumSize(QSize(200, 0))

        self.horizontalLayout.addWidget(self.lineEdit_servername)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_server_port = QLabel(Form)
        self.label_server_port.setObjectName(u"label_server_port")
        sizePolicy.setHeightForWidth(self.label_server_port.sizePolicy().hasHeightForWidth())
        self.label_server_port.setSizePolicy(sizePolicy)
        self.label_server_port.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_2.addWidget(self.label_server_port)

        self.lineEdit_serverport = QLineEdit(Form)
        self.lineEdit_serverport.setObjectName(u"lineEdit_serverport")
        self.lineEdit_serverport.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_2.addWidget(self.lineEdit_serverport)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_db_name = QLabel(Form)
        self.label_db_name.setObjectName(u"label_db_name")
        sizePolicy.setHeightForWidth(self.label_db_name.sizePolicy().hasHeightForWidth())
        self.label_db_name.setSizePolicy(sizePolicy)
        self.label_db_name.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_3.addWidget(self.label_db_name)

        self.lineEdit_dbname = QLineEdit(Form)
        self.lineEdit_dbname.setObjectName(u"lineEdit_dbname")
        self.lineEdit_dbname.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_3.addWidget(self.lineEdit_dbname)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_user_name = QLabel(Form)
        self.label_user_name.setObjectName(u"label_user_name")
        self.label_user_name.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_4.addWidget(self.label_user_name)

        self.lineEdit_user = QLineEdit(Form)
        self.lineEdit_user.setObjectName(u"lineEdit_user")
        self.lineEdit_user.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_4.addWidget(self.lineEdit_user)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_password = QLabel(Form)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_5.addWidget(self.label_password)

        self.lineEdit_password = QLineEdit(Form)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setMinimumSize(QSize(200, 0))
        self.lineEdit_password.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_5.addWidget(self.lineEdit_password)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_check_connection = QPushButton(Form)
        self.pushButton_check_connection.setObjectName(u"pushButton_check_connection")
        self.pushButton_check_connection.setMinimumSize(QSize(200, 0))

        self.verticalLayout_2.addWidget(self.pushButton_check_connection)

        self.label_Check_Connect = QLabel(Form)
        self.label_Check_Connect.setObjectName(u"label_Check_Connect")
        self.label_Check_Connect.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_Check_Connect)


        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 2)

        self.pushButton_OK = QPushButton(Form)
        self.pushButton_OK.setObjectName(u"pushButton_OK")

        self.gridLayout.addWidget(self.pushButton_OK, 2, 0, 1, 1)

        self.pushButton_Cancel = QPushButton(Form)
        self.pushButton_Cancel.setObjectName(u"pushButton_Cancel")

        self.gridLayout.addWidget(self.pushButton_Cancel, 2, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_server_name.setText(QCoreApplication.translate("Form", u"Server name", None))
        self.lineEdit_servername.setText("")
        self.lineEdit_servername.setPlaceholderText(QCoreApplication.translate("Form", u"Enter Server name", None))
        self.label_server_port.setText(QCoreApplication.translate("Form", u"Server port", None))
        self.lineEdit_serverport.setText("")
        self.lineEdit_serverport.setPlaceholderText(QCoreApplication.translate("Form", u"Enter Port", None))
        self.label_db_name.setText(QCoreApplication.translate("Form", u"Database name", None))
        self.lineEdit_dbname.setText("")
        self.lineEdit_dbname.setPlaceholderText(QCoreApplication.translate("Form", u"Enter Database name", None))
        self.label_user_name.setText(QCoreApplication.translate("Form", u"User", None))
        self.lineEdit_user.setText("")
        self.lineEdit_user.setPlaceholderText(QCoreApplication.translate("Form", u"Enter User", None))
        self.label_password.setText(QCoreApplication.translate("Form", u"Password", None))
        self.lineEdit_password.setText("")
        self.lineEdit_password.setPlaceholderText(QCoreApplication.translate("Form", u"Enter Password", None))
        self.pushButton_check_connection.setText(QCoreApplication.translate("Form", u"Check Connection", None))
        self.label_Check_Connect.setText(QCoreApplication.translate("Form", u"Check?", None))
        self.pushButton_OK.setText(QCoreApplication.translate("Form", u"OK", None))
        self.pushButton_Cancel.setText(QCoreApplication.translate("Form", u"Cancel", None))
    # retranslateUi

