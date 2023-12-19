# ### Задача.
#
# Разработать клиент для работы с базой данных, разработка которой велась на курсе DevDB.
#
# Обязательные функции в приложении:
#
# * Должна присутствовать авторизация в БД
# * Функционал должен обеспечивать полный набор CRUD операции с БД.
# * Обеспечить возможность работы с клиентом (отображение данных в графических элементах).

import psycopg2
import datetime
from PySide6 import QtGui, QtWidgets, QtCore

from DB_Forms import NewEmpForm
from ui.ConnectionForm import Ui_Form
from ui.DBClient import Ui_MainWindow
from ui.EditForm import Ui_Form_Edit


class DBClient(QtWidgets.QMainWindow, Ui_MainWindow):

    # Блок инициации клиента для работы с базой данных
    def __init__(self, parent=None):
        super().__init__(parent)
        self.first_time = True
        self.settings = QtCore.QSettings("DBClientSettings")
        self.initConsts()
        self.setupUi(self)
        self.setWindowTitle("Клиент для работы с базой данных")
        self.initCreds()
        self.win = None
        self.win2 = None
        self.win3 = None
        # self.initThreads()
        self.initDB()
        self.initSignals()
        self.installEventFilter(self)

        if self.connect.status == 1:
            self.show_view_table(self.SQL_request_emp)  # Первыми показываем список сотрудников

# Обработчик событий
    def eventFilter(self, obj, event):
        if event.type() == QtWidgets.QTableView.activated:
            print(event)
        return super().eventFilter(obj, event)

    # def initThreads(self) -> None:
        # self.thread_new = WorkerNew()

    # Функции подключения к базе данных и вывода основного списка работников
    def initDB(self) -> None:
        self.connect = psycopg2.connect(host=self.host,
                                        port=self.port,
                                        dbname=self.dbname,
                                        user=self.user,
                                        password=self.password)
        self.cursor = self.connect.cursor()
        pass

    def saveConnectToDB(self) -> None:
        if self.connect.status == 1:
            self.initDB()
            self.cursor = self.connect.cursor()
        self.win2.close()
        pass

    def closeDB(self) -> None:
        self.cursor.close()
        self.connect.close()
        pass

    def show_view_table(self, sql_input: list) -> None:
        sql_request1 = sql_input[0]

        self.cursor.execute(sql_request1)

        data = self.cursor.fetchall()
    # print(data_emp)
        self.model = QtGui.QStandardItemModel()
        self.model.setHorizontalHeaderLabels(sql_input[2])

        for elem in data:
            list_items = []
            for i in range(sql_input[1]):
                list_items.append(QtGui.QStandardItem(str(elem[i])))
            self.model.appendRow(list_items)

        self.tableView.setModel(self.model)
        pass

# Сигналы для работы основного окна приложения
    def initSignals(self):
        """

        :return:
        """
        # Добавление элемента в список сотрудников
        self.pushButtonAdd.clicked.connect(self.onPushButtonAddClicked)
        #
        self.pushButtonDelete.clicked.connect(self.onPushButtonDeleteClicked)
        # Сигнал для выполнения SQL запроса
        self.pushButtonRequest.clicked.connect(self.onPushButtonRequestClicked)
        #
        self.pushButton_Edit.clicked.connect(self.onPushButtonEditClicked)

        #  Возврат к списку сотрудников в главном окне
        self.pushButtonRefresh.clicked.connect(lambda: self.show_view_table(self.SQL_request_emp))
        #
        self.actionAbout_DBClient.triggered.connect(self.onMenuAboutClicked)

        self.actionSQL_Editor.triggered.connect(lambda: self.tabWidget.setCurrentIndex(1))

        #  Сигналы переключения к другим представлениям в главном окне
        self.actionDivisions.triggered.connect(lambda: self.show_view_table(self.SQL_request_div))
        self.actionPositions.triggered.connect(lambda: self.show_view_table(self.SQL_request_pos))
        self.actionOrders.triggered.connect(lambda: self.show_view_table(self.SQL_request_orders))
        self.actionStaffing.triggered.connect(lambda: self.show_view_table(self.SQL_request_staff))
        self.actionConnect_to_Server.triggered.connect(self.Connect)
        self.pushButton_Edit.clicked.connect(self.edit_emp)

        # Сигналы на редактирование в главном окне


    # Слоты для описания действий на кнопки
    def onMenuAboutClicked(self) -> None:
        """
        В статус бар выводится информация о программе
        :return:
        """
        text_about = "Это программа подключения и работы с учебной базой DevDB2023 на сервере gpngw.avalon.ru"
        self.statusBar().showMessage(text_about)
        pass

    def onPushButtonAddClicked(self) -> None:
        """
        Добавление элемента в список сотрудников
        :return:
        """
        self.show_new_emp_window()

        pass

    def onPushButtonDeleteClicked(self):
        pass

    def onPushButtonRequestClicked(self) -> None:
        """
        Процедура выполнения SQL запроса на вкладке SQL Request
        :return:
        """
        sql_request2 = self.textEdit.toPlainText()
        self.cursor.execute(sql_request2)
        data = self.cursor.fetchall()
        self.plainTextEdit.setPlainText(str(data))
        pass

    def onPushButtonRefreshClicked(self):
        pass

    def onPushButtonEditClicked(self):
        pass

    def show_new_emp_window(self):
        if self.win is None:
            self.win = NewEmpForm()
            self.win.show()
            self.win.pushbutton_ok.clicked.connect(self.insert_new_emp(self.win.newUserSQL))

        else:
            self.win.close()
            self.win = None

    def insert_new_emp(self, new_usr: str):
        print(new_usr)
        pass

    def edit_emp(self):
        if self.win3 is None:
            self.win3 = EditEmp()
            xz = self.tableView.selectionModel().currentIndex().row()
            data_emp = self.model.takeRow(xz)
# Заполнение формы для редактирования данными текущего элемента
            self.win3.lineEdit_empid.setText(data_emp[0].text())
            self.win3.lineEdit_empname.setText(data_emp[1].text())
            self.win3.dateEdit_emp_birthdate.setDate(datetime.date.fromisoformat(data_emp[2].text()))
            self.win3.lineEdit_regaddress.setText(data_emp[3].text())
            self.win3.lineEdit_emp_phone.setText(data_emp[4].text())
            self.win3.lineEdit_emp_mail.setText(data_emp[5].text())
            self.win3.current_id = data_emp[0].text()
            self.win3.show()
        else:
            self.win3.close()
            self.win3 = None

    def initCreds(self) -> None:
        if self.first_time == True:
            self.host = "vpngw.avalon.ru"
            self.port = "5432"
            self.dbname = "DevDB2023_vadkal"
            self.user = "pguser"
            self.password = "Pa$$w0rd"
        else:
            self.host = self.settings.value("Server name", "")
            self.port = self.settings.value("Port number", "")
            self.dbname = self.settings.value("DB name", "")
            self.user = self.settings.value("User name", "")
            self.password = self.settings.value("Password", "")
        return None

    def Connect(self) -> None:
        if self.win2 is None:
            self.win2 = ServerConnection()
            self.win2.lineEdit_servername.setText(self.host)
            self.win2.lineEdit_serverport.setText(self.port)
            self.win2.lineEdit_dbname.setText(self.dbname)
            self.win2.lineEdit_user.setText(self.user)
            self.win2.lineEdit_password.setText(self.password)
            self.win2.show()
            self.win2.pushButton_Cancel.clicked.connect(lambda: self.win2.close())
            self.win2.pushButton_check_connection.clicked.connect(lambda: self.checkConnection())
            self.win2.pushButton_OK.clicked.connect(lambda: self.saveConnectToDB())

        else:
            self.win2.close()
            self.win2 = None

    def checkConnection(self) -> None:
        self.closeDB()
        self.host = self.win2.lineEdit_servername.text()
        self.port = self.win2.lineEdit_serverport.text()
        self.dbname = self.win2.lineEdit_dbname.text()
        self.user = self.win2.lineEdit_user.text()
        self.password = self.win2.lineEdit_password.text()
        self.initDB()
        if self.connect.status == 1:
            self.win2.label_Check_Connect.setText("Connection is OK!")
        else:
            self.win2.label_Check_Connect.setText("Connection is broken!!!")
        pass

    def initConsts(self) -> None:
        self.SQL_request_emp = ['Select empid, empname, birthdate, regaddress, contactphone, email from "HR"."Employees" order by empid;', 6,
                                ["Employee's ID", "Employee's Name", "Birth Date", "Registration Address", "Contact Phone", "E-mail"]]
        self.SQL_request_pos = ['Select positionid, positionname, salarymax, salarymin from "HR"."Positions" order by positionid;', 4,
                                ["Position ID", "Position Name", "Salary Maximum", "Salary Minimum"]]
        self.SQL_request_div = ['Select divisionid, divisionname, parentid, bossid, eventdate, eventtype, orderid from "HR"."Divisions" order by divisionid;', 7,
                                ["Division ID", "Division Name", "Parent ID", "Boss ID", "Event Date", "Event Type", "Order ID"]]
        self.SQL_request_orders = ['Select orderid, signedby, orderdate, ordernumber from "Orders"."Orders" order by orderid;', 4,
                                ["Order ID", "Signed By", "Order Date", "Order Number"]]
        self.SQL_request_staff = ['Select empid, positionid, divisionid, fte, salary, eventdate, eventtype, orderid from "Staff"."Staffing" order by empid;', 8,
                                ["Employee's ID", "Position ID", "Division ID", "FTE", "Salary", "Event Date", "Event Type", "Order ID"]]

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.settings.setValue("Server name", self.host)
        self.settings.setValue("DB name", self.dbname)
        self.settings.setValue("Port number", self.port)
        self.settings.setValue("User name", self.user)
        self.settings.setValue("Password", self.password)


# Форма для создания подключения к серверу

# Класс запускающий окно для изменения подключения к серверу
class ServerConnection(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


# Класс запускающий редактирование сотрудника
class EditEmp(QtWidgets.QWidget, Ui_Form_Edit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.initSignal()
        self.current_id = None


    def initSignal(self):
        self.pushButton_update.clicked.connect(self.emp_update)
        self.pushButton_Close.clicked.connect(self.form_close)
        self.pushButton_Delete.clicked.connect(self.emp_delete)


    def emp_update(self) -> None:
        pass

    def form_close(self) -> None:
        self.close()
        pass

    def emp_delete(self) -> None:
        pass

# TODO Реализация CRUD операций для базы данных


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = DBClient()

    win.show()

    app.exec()
