# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DBClient.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QMainWindow,
    QMenu, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QStatusBar, QTabWidget, QTableView,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionConnect_to_Server = QAction(MainWindow)
        self.actionConnect_to_Server.setObjectName(u"actionConnect_to_Server")
        self.actionClose_Connecttion = QAction(MainWindow)
        self.actionClose_Connecttion.setObjectName(u"actionClose_Connecttion")
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionCreate_Table = QAction(MainWindow)
        self.actionCreate_Table.setObjectName(u"actionCreate_Table")
        self.actionSQL_Editor = QAction(MainWindow)
        self.actionSQL_Editor.setObjectName(u"actionSQL_Editor")
        self.actionAbout_DBClient = QAction(MainWindow)
        self.actionAbout_DBClient.setObjectName(u"actionAbout_DBClient")
        self.actionDivisions = QAction(MainWindow)
        self.actionDivisions.setObjectName(u"actionDivisions")
        self.actionPositions = QAction(MainWindow)
        self.actionPositions.setObjectName(u"actionPositions")
        self.actionOrders = QAction(MainWindow)
        self.actionOrders.setObjectName(u"actionOrders")
        self.actionStaffing = QAction(MainWindow)
        self.actionStaffing.setObjectName(u"actionStaffing")
        self.actionEmployees = QAction(MainWindow)
        self.actionEmployees.setObjectName(u"actionEmployees")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(6, -1, 791, 561))
        self.tabWidget.setMinimumSize(QSize(791, 561))
        self.tabWidget.setMaximumSize(QSize(791, 561))
        self.SQL = QWidget()
        self.SQL.setObjectName(u"SQL")
        self.pushButtonRequest = QPushButton(self.SQL)
        self.pushButtonRequest.setObjectName(u"pushButtonRequest")
        self.pushButtonRequest.setGeometry(QRect(1, 199, 75, 24))
        self.plainTextEdit = QPlainTextEdit(self.SQL)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(1, 229, 781, 192))
        self.plainTextEdit.setMinimumSize(QSize(0, 192))
        self.plainTextEdit.setMaximumSize(QSize(781, 192))
        self.plainTextEdit.setReadOnly(True)
        self.textEdit = QTextEdit(self.SQL)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(1, 1, 781, 192))
        self.textEdit.setMinimumSize(QSize(104, 71))
        self.tabWidget.addTab(self.SQL, "")
        self.Database = QWidget()
        self.Database.setObjectName(u"Database")
        self.tableView = QTableView(self.Database)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(0, 40, 791, 491))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setMinimumSize(QSize(600, 400))
        self.tableView.setMaximumSize(QSize(791, 491))
        self.layoutWidget = QWidget(self.Database)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 320, 26))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButtonAdd = QPushButton(self.layoutWidget)
        self.pushButtonAdd.setObjectName(u"pushButtonAdd")

        self.horizontalLayout.addWidget(self.pushButtonAdd)

        self.pushButton_Edit = QPushButton(self.layoutWidget)
        self.pushButton_Edit.setObjectName(u"pushButton_Edit")

        self.horizontalLayout.addWidget(self.pushButton_Edit)

        self.pushButtonDelete = QPushButton(self.layoutWidget)
        self.pushButtonDelete.setObjectName(u"pushButtonDelete")

        self.horizontalLayout.addWidget(self.pushButtonDelete)

        self.pushButtonRefresh = QPushButton(self.layoutWidget)
        self.pushButtonRefresh.setObjectName(u"pushButtonRefresh")

        self.horizontalLayout.addWidget(self.pushButtonRefresh)

        self.tabWidget.addTab(self.Database, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        self.menuOpenView = QMenu(self.menuTools)
        self.menuOpenView.setObjectName(u"menuOpenView")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuFile.addAction(self.actionConnect_to_Server)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuTools.addAction(self.menuOpenView.menuAction())
        self.menuTools.addAction(self.actionSQL_Editor)
        self.menuOpenView.addAction(self.actionDivisions)
        self.menuOpenView.addAction(self.actionPositions)
        self.menuOpenView.addAction(self.actionOrders)
        self.menuOpenView.addAction(self.actionStaffing)
        self.menuOpenView.addAction(self.actionEmployees)
        self.menuAbout.addAction(self.actionAbout_DBClient)

        self.retranslateUi(MainWindow)
        self.actionSQL_Editor.triggered.connect(self.tabWidget.setFocus)
        self.actionClose.triggered.connect(MainWindow.close)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionConnect_to_Server.setText(QCoreApplication.translate("MainWindow", u"Connect to Server", None))
        self.actionClose_Connecttion.setText(QCoreApplication.translate("MainWindow", u"Close Connecttion", None))
        self.actionSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionCreate_Table.setText(QCoreApplication.translate("MainWindow", u"Create Table", None))
        self.actionSQL_Editor.setText(QCoreApplication.translate("MainWindow", u"SQL Editor", None))
        self.actionAbout_DBClient.setText(QCoreApplication.translate("MainWindow", u"About DBClient", None))
        self.actionDivisions.setText(QCoreApplication.translate("MainWindow", u"Divisions", None))
        self.actionPositions.setText(QCoreApplication.translate("MainWindow", u"Positions", None))
        self.actionOrders.setText(QCoreApplication.translate("MainWindow", u"Orders", None))
        self.actionStaffing.setText(QCoreApplication.translate("MainWindow", u"Staffing", None))
        self.actionEmployees.setText(QCoreApplication.translate("MainWindow", u"Employees", None))
        self.pushButtonRequest.setText(QCoreApplication.translate("MainWindow", u"Request", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please type arbitrary SQL query", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SQL), QCoreApplication.translate("MainWindow", u"SQL Request", None))
        self.pushButtonAdd.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButton_Edit.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.pushButtonDelete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.pushButtonRefresh.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Database), QCoreApplication.translate("MainWindow", u"Table", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"Database", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.menuOpenView.setTitle(QCoreApplication.translate("MainWindow", u"OpenView", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

