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

from ui.ConnectionForm import Ui_Form
from ui.DBClient import Ui_MainWindow
from ui.EditFormEmp import Ui_Form_Emp


class DBClient(QtWidgets.QMainWindow, Ui_MainWindow):

    # Блок инициации клиента для работы с базой данных
    def __init__(self, parent=None):
        super().__init__(parent)
        # Инициализация настроек
        self.settings = QtCore.QSettings("DBClientSettings")

        # Инициализация констант для подключения к таблицам Базы данных
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
        # Конец инициализации констант подключения к базе данных

        # Инициализация свойств Приложения для работы с данными
        self.connect = None
        self.cursor = None
        self.model = None
        self.host = ""
        self.port = ""
        self.dbname = ""
        self.user = ""
        self.password = ""
        # --- Конец определения объектов для работы с данными

        self.setupUi(self)
        self.setWindowTitle("Клиент для работы с базой данных")

        # Инициализируем параметры подключения к серверу и БД
        if self.settings.value("Server name", "") == "":
            self.first_time = True  # Если внутри settings нет сохраненных настроек ставим параметр в первый раз,
        else:
            self.first_time = False  # Или ставим False когда данные в настройках есть
            # для забора заранее настроенных параметров
        self.initCreds()  # Инициализируем параметры подключения
        self.initDB()  # Инициализируем connect и cursor
        ########################################################

        # Инициализация окон для работы со всплывающими формами редактирования
        self.win_div = None
        self.win_serv = None   # Окно редактирования параметров сервера
        self.win_emp = None    # Окно редактирования сотрудника
        # --- Конец инициации всплывающих окон для редактирования данных

        self.initSignals()
        self.installEventFilter(self)

        self.activeSQL_request = self.SQL_request_emp  # Первыми показываем список сотрудников
        self.show_view_table(self.activeSQL_request)  # Первыми показываем список сотрудников

    # Обработчик событий
    def eventFilter(self, obj, event):
        if event.type() == QtWidgets.QTableView.activated:
            print(event)
        return super().eventFilter(obj, event)
    # --- Конец обработчика событий

    # Функция подключения к базе данных - создает connect и cursor
    def initDB(self) -> None:
        self.connect = psycopg2.connect(host=self.host,
                                        port=self.port,
                                        dbname=self.dbname,
                                        user=self.user,
                                        password=self.password)
        self.cursor = self.connect.cursor()
        pass
    #############################################

    def saveConnectToDB(self) -> None:
        if self.connect.status == 1:
            self.initDB()
            self.cursor = self.connect.cursor()
        self.win_serv.close()
        pass

    def closeDB(self) -> None:
        self.cursor.close()
        self.connect.close()
        pass

    def show_view_table(self, sql_input: list) -> None:
        sql_request1 = sql_input[0]

        self.cursor.execute(sql_request1)

        data = self.cursor.fetchall()
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
        Вызовы слотов для сигналов при работе с главным окном

        :return:
        """
        # Кнопки для операций на вкладке Table
        self.pushButtonAdd.clicked.connect(self.onPushButtonAddClicked)
        self.pushButton_Edit.clicked.connect(self.edit_emp)
        self.pushButtonDelete.clicked.connect(self.onPushButtonDeleteClicked)
        self.pushButtonRefresh.clicked.connect(self.refreshView)

        # Сигнал для выполнения SQL запроса на вкладке SQL request
        self.pushButtonRequest.clicked.connect(self.onPushButtonRequestClicked)

        #  Показ текста About DBClient в статус баре
        self.actionAbout_DBClient.triggered.connect(self.onMenuAboutClicked)

        # Переход к редактору SQL запросов
        self.actionSQL_Editor.triggered.connect(lambda: self.tabWidget.setCurrentIndex(1))

        # Переход к другим представлениям в разделе Меню OpenView
        self.actionDivisions.triggered.connect(self.onDivisions)
        self.actionPositions.triggered.connect(self.onPositions)
        self.actionOrders.triggered.connect(self.onOrders)
        self.actionStaffing.triggered.connect(self.onStaffing)
        self.actionEmployees.triggered.connect(self.onEmployees)

        # Изменение подключения к серверу по разделу Menu Connect to Server
        self.actionConnect_to_Server.triggered.connect(self.Connect)

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
        pass

    def onPushButtonDeleteClicked(self):
        pass

    # Функция выполнения произвольного SQL запроса
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

    # Функции обновления представлений в OpenView
    def onEmployees(self):
        """

        :return:
        """
        self.activeSQL_request = self.SQL_request_emp
        self.refreshView()
        pass

    def onDivisions(self):
        """

        :return:
        """
        self.activeSQL_request = self.SQL_request_div
        self.refreshView()
        pass

    def onPositions(self):
        """

        :return:
        """
        self.activeSQL_request = self.SQL_request_pos
        self.refreshView()
        pass

    def onOrders(self):
        """

        :return:
        """
        self.activeSQL_request = self.SQL_request_orders
        self.refreshView()
        pass

    def onStaffing(self):
        """

        :return:
        """
        self.activeSQL_request = self.SQL_request_staff
        self.refreshView()
        pass

    # Функция обновления текущего окна
    def refreshView(self):
        """
        Обновление TableView
        :return:
        """
        self.initDB()
        self.show_view_table(self.activeSQL_request)
        pass
    # ---------------

    def edit_emp(self):
        if self.win_emp is None:
            self.win_emp = EditEmp()
            xz = self.tableView.selectionModel().currentIndex().row()
            data_emp = self.model.takeRow(xz)
# Заполнение формы для редактирования данными текущего элемента
            self.win_emp.lineEdit_empid.setText(data_emp[0].text())
            self.win_emp.lineEdit_empname.setText(data_emp[1].text())
            self.win_emp.dateEdit_emp_birthdate.setDate(datetime.date.fromisoformat(data_emp[2].text()))
            self.win_emp.lineEdit_regaddress.setText(data_emp[3].text())
            self.win_emp.lineEdit_emp_phone.setText(data_emp[4].text())
            self.win_emp.lineEdit_emp_mail.setText(data_emp[5].text())
            self.win_emp.current_id = data_emp[0].text()
            self.win_emp.show()
        else:
            self.win_emp.close()
            self.win_emp = None

    # Инициализация параметров подключения к серверу
    def initCreds(self) -> None:
        if self.first_time:
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
            self.first_time = False
        return None

    def Connect(self) -> None:
        if self.win_serv is None:
            self.win_serv = ServerConnection()
            self.win_serv.lineEdit_servername.setText(self.host)
            self.win_serv.lineEdit_serverport.setText(self.port)
            self.win_serv.lineEdit_dbname.setText(self.dbname)
            self.win_serv.lineEdit_user.setText(self.user)
            self.win_serv.lineEdit_password.setText(self.password)
            self.win_serv.show()
            self.win_serv.pushButton_Cancel.clicked.connect(lambda: self.win_serv.close())
            self.win_serv.pushButton_check_connection.clicked.connect(lambda: self.checkConnection())
            self.win_serv.pushButton_OK.clicked.connect(lambda: self.saveConnectToDB())

        else:
            self.win_serv.close()
            self.win_serv = None

    # Метод проверки статус соединения к СУБД печатает статус в форме, ошибки выводятся в консоль
    def checkConnection(self) -> None:
        self.closeDB()
        self.host = self.win_serv.lineEdit_servername.text()
        self.port = self.win_serv.lineEdit_serverport.text()
        self.dbname = self.win_serv.lineEdit_dbname.text()
        self.user = self.win_serv.lineEdit_user.text()
        self.password = self.win_serv.lineEdit_password.text()
        self.initDB()
        if self.connect.status == 1:
            self.win_serv.label_Check_Connect.setText("Connection is OK!")
        else:
            self.win_serv.label_Check_Connect.setText("Connection is broken!!!")
        pass

    # Метод сохраняет настройки подключения к СУБД при закрытии Главного окна приложения
    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.settings.setValue("Server name", self.host)
        self.settings.setValue("DB name", self.dbname)
        self.settings.setValue("Port number", self.port)
        self.settings.setValue("User name", self.user)
        self.settings.setValue("Password", self.password)


# Класс запускающий окно для изменения подключения к серверу
class ServerConnection(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

# Классы для CRUD операций с базой данных


# Класс запускающий редактирование сотрудника
class EditEmp(QtWidgets.QWidget, Ui_Form_Emp):
    updated = QtCore.Signal(str)
    deleted = QtCore.Signal(str)
    new = QtCore.Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.initSignal()
        self.current_id = ""

    def initSignal(self):
        self.pushButton_update.clicked.connect(self.emp_update)
        self.pushButton_New.clicked.connect(self.emp_new)
        self.pushButton_Delete.clicked.connect(self.emp_delete)

    def emp_update(self) -> None:
        sql_updated = (f'UPDATE INTO "HR"."Employees" (empname, birthdate, regaddress, contactphone, email) '
                   f'VALUES ({self.lineEdit_empname.text()}, {self.dateEdit_emp_birthdate.date()}, {self.lineEdit_regaddress.text()},'
                   f' {self.lineEdit_emp_phone}, {self.lineEdit_emp_mail});')
        self.updated.emit(sql_updated)
        pass

    def emp_new(self) -> None:
        sql_new = (f'INSERT INTO "HR"."Employees" (empname, birthdate, regaddress, contactphone, email) '
                   f'VALUES ({self.lineEdit_empname.text()}, {self.dateEdit_emp_birthdate.date()}, {self.lineEdit_regaddress.text()},'
                   f' {self.lineEdit_emp_phone}, {self.lineEdit_emp_mail});')
        self.new.emit(sql_new)
        pass

    def emp_delete(self) -> None:
        sql_delete = f'DELETE FROM "HR"."Employees" WHERE "empid" = {self.current_id};'
        self.deleted.emit(sql_delete)
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    win = DBClient()
    win.show()
    app.exec()
