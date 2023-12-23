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
from PySide6.QtWidgets import QMessageBox

from ui.ConnectionForm import Ui_Form
from ui.DBClient import Ui_MainWindow
from ui.EditFormEmp import Ui_Form_Emp
from ui.EditFormOrder import Ui_Form_Order
from ui.EditFormPositions import Ui_Form_Position
from ui.EditFormDivisions import Ui_Form_Divisions
from ui.AddStaffingRecord import Ui_Form_Staff


class DBClient(QtWidgets.QMainWindow, Ui_MainWindow):

    # Блок инициации клиента для работы с базой данных
    def __init__(self, parent=None):
        super().__init__(parent)
        # Инициализация настроек
        self.win_message = QMessageBox(self)
        self.settings = QtCore.QSettings("DBClientSettings")

        # Инициализация констант для подключения к таблицам Базы данных
        self.SQL_request_emp = ['Select empid, empname, birthdate, regaddress, contactphone, email from "HR"."Employees" order by empid;', 6,
                                ["Employee's ID", "Employee's Name", "Birth Date", "Registration Address", "Contact Phone", "E-mail"]]
        self.SQL_request_pos = ['Select positionid, positionname, salarymax, salarymin from "HR"."Positions" order by positionid;', 4,
                                ["Position ID", "Position Name", "Salary Maximum", "Salary Minimum"]]
        self.SQL_request_div = [f'Select divisionid, divisionname, bossid, empname, eventtype from "HR"."Divisions" as HD left join "HR"."Employees" as HE'
                                f' on HD.bossid = HE.empid order by divisionid;', 5,
                                ["Division ID", "Division Name", "Boss ID", "Boss Name", "Status"]]
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
        self.win_order = None  # Окно редактирования приказа
        self.win_position = None  # Окно редактирования позиции
        self.win_division = None  # Окно редактирования подразделения
        self.win_staffing = None  # Окно редактирования назначения
        # --- Конец инициации всплывающих окон для редактирования данных

        self.initSignals()
        self.installEventFilter(self)
        # self.Connect()
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
        self.pushButton_Edit.clicked.connect(self.onPushButtonEditClicked)
        self.pushButtonDelete.clicked.connect(self.onPushButtonDeleteClicked)
        self.pushButtonRefresh.clicked.connect(self.refreshView)

        # Сигнал для выполнения SQL запроса на вкладке SQL request
        self.pushButtonRequest.clicked.connect(self.onPushButtonRequestClicked)

        #  Показ текста About DBClient в статус баре
        self.actionAbout_DBClient.triggered.connect(self.onMenuAboutClicked)

        # Переход к редактору SQL запросов
        self.actionSQL_Editor.triggered.connect(lambda: self.tabWidget.setCurrentIndex(0))

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
        if self.activeSQL_request == self.SQL_request_emp:
            self.edit_emp(True)
        if self.activeSQL_request == self.SQL_request_orders:
            self.edit_order(True)
        if self.activeSQL_request == self.SQL_request_pos:
            self.edit_position(True)
        if self.activeSQL_request == self.SQL_request_div:
            self.edit_division(True)
        if self.activeSQL_request == self.SQL_request_staff:
            self.add_staffing()
        pass

    def onPushButtonEditClicked(self) -> None:
        """
        Добавление элемента в список сотрудников
        :return:
        """
        if self.activeSQL_request == self.SQL_request_emp:
            self.edit_emp(False)
        if self.activeSQL_request == self.SQL_request_orders:
            self.edit_order(False)
        if self.activeSQL_request == self.SQL_request_pos:
            self.edit_position(False)
        if self.activeSQL_request == self.SQL_request_div:
            self.edit_division(False)
        if self.activeSQL_request == self.SQL_request_staff:
            self.win_message.setWindowTitle('Предупреждение')
            self.win_message.setText('Нельзя отредактировать запись из реестра назначений!!! \n'
                                     '- только добавить новую!')
            self.win_message.exec()
        pass

    # Функция удаления элемента
    def onPushButtonDeleteClicked(self) -> None:
        current_row = self.tableView.selectionModel().currentIndex().row()
        if current_row == -1:
            self.statusBar().showMessage("Не выбран элемент таблицы")
            return None
        row_data = self.model.takeRow(current_row)
        # Удаление сотрудника
        if self.activeSQL_request == self.SQL_request_emp:
            print(row_data[0].text())
            x_sql = f'DELETE FROM "HR"."Employees" WHERE "empid" = {row_data[0].text()};'
            self.cursor.execute('begin;' + x_sql + 'commit;')
            self.show_view_table(self.activeSQL_request)
        # Удаление подразделения
        if self.activeSQL_request == self.SQL_request_div:
            print(row_data[0].text())
            x_sql = f'DELETE FROM "HR"."Divisions" WHERE "divisionid" = {row_data[0].text()};'
            self.cursor.execute('begin;' + x_sql + 'commit;')
            self.show_view_table(self.activeSQL_request)
        # Удаление позиции
        if self.activeSQL_request == self.SQL_request_pos:
            print(row_data[0].text())
            x_sql = f'DELETE FROM "HR"."Positions" WHERE "positionid" = {row_data[0].text()};'
            self.cursor.execute('begin;' + x_sql + 'commit;')
            self.show_view_table(self.activeSQL_request)
        # Удаление приказа
        if self.activeSQL_request == self.SQL_request_orders:
            print(row_data[0].text())
            x_sql = f'DELETE FROM "Orders"."Orders" WHERE "orderid" = {row_data[0].text()};'
            self.cursor.execute('begin;' + x_sql + 'commit;')
            self.show_view_table(self.activeSQL_request)
        if self.activeSQL_request == self.SQL_request_staff:
            self.statusBar().showMessage('Попытка удаления записи  из таблицы Staffing')
            self.win_message.setWindowTitle('Предупреждение')
            self.win_message.setText('Нельзя удалить запись из реестра назначений')
            self.win_message.exec()
            self.show_view_table(self.activeSQL_request)
        pass

    def onSQL(self, sql='') -> None:
        if sql == '':
            print("Никого не удаляем")
        else:
            self.cursor.execute(sql)
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

# Функция вызова формы редактирования пользователя
    def edit_emp(self, new=False) -> None:
        if self.win_emp is None:
            if self.tableView.selectionModel().currentIndex().row() == -1:
                self.statusBar().showMessage("Не выбран элемент")
                return None
            else:
                current_row = self.tableView.selectionModel().currentIndex().row()
                data_emp = self.model.takeRow(current_row)
    # Задание параметров текущего пользователя
            user = dict({"empid": f'{data_emp[0].text()}',
                    "name": data_emp[1].text(),
                    "birthday": datetime.date.fromisoformat(data_emp[2].text()),
                    "address": data_emp[3].text(),
                    "phone": data_emp[4].text(),
                    "email": data_emp[5].text()})
            self.win_emp = EditEmp(self, user, new)
            self.refreshView()
    #  --- Конец Заполнения и активации формы для редактирования данными текущего пользователя
        else:
            self.win_emp = None
            self.refreshView()

    # --- Конец функции вызова формы редактирования пользователя

        # Функция вызова формы редактирования приказа
    def edit_order(self, new=False) -> None:
        if self.win_order is None:
            if self.tableView.selectionModel().currentIndex().row() == -1:
                self.statusBar().showMessage("Не выбран элемент")
                return None
            else:
                current_row = self.tableView.selectionModel().currentIndex().row()
                data_order = self.model.takeRow(current_row)
                # Задание параметров текущего пользователя
            order = dict({"orderid": f'{data_order[0].text()}',
                        "signedby": data_order[1].text(),
                        "orderdate": datetime.date.fromisoformat(data_order[2].text()),
                        "ordernumber": data_order[3].text()})
            self.win_order = EditOrder(self, order, new)
            self.refreshView()
            #  --- Конец Заполнения и активации формы для редактирования данными текущего пользователя
        else:
            self.win_emp = None
            self.refreshView()

        # --- Конец функции вызова формы редактирования приказа

        # Функция вызова формы редактирования позиции
    def edit_position(self, new=False) -> None:
        if self.win_position is None:
            if self.tableView.selectionModel().currentIndex().row() == -1:
                self.statusBar().showMessage("Не выбран элемент")
                return None
            else:
                current_row = self.tableView.selectionModel().currentIndex().row()
                data_pos = self.model.takeRow(current_row)
                # Задание параметров текущего пользователя
            position = dict({"positionid": f'{data_pos[0].text()}',
                        "positionname": data_pos[1].text(),
                        "salarymin": data_pos[2].text(),
                        "salarymax": data_pos[3].text()})
            self.win_position = EditPosition(self, position, new)
            self.refreshView()
            #  --- Конец Заполнения и активации формы для редактирования данными текущего пользователя
        else:
            self.win_position = None
            self.refreshView()

        # --- Конец функции вызова формы редактирования позиции

        # Функция вызова формы редактирования подразделения
    def edit_division(self, new=False) -> None:
        if self.win_division is None:
            if self.tableView.selectionModel().currentIndex().row() == -1:
                self.statusBar().showMessage("Не выбран элемент")
                return None
            else:
                current_row = self.tableView.selectionModel().currentIndex().row()
                data_div = self.model.takeRow(current_row)
                # Задание параметров текущего подразделения
            division = dict({"divisionid": f'{data_div[0].text()}',
                        "divisionname": data_div[1].text(),
                        "bossname": data_div[3].text(),
                        "status": data_div[4].text()})
            self.win_division = EditDivision(self, division, new)
            self.refreshView()
            #  --- Конец Заполнения и активации формы для редактирования данными текущего подразделения
        else:
            self.win_division = None
            self.refreshView()

        # --- Конец функции вызова формы редактирования позиции

        # Функция вызова формы редактирования назначения
    def add_staffing(self) -> None:
        if self.win_staffing is None:
            emp_sql = f'select empid, empname from "HR"."Employees";'
            self.cursor.execute(emp_sql)
            data_emp = self.cursor.fetchall()
            pos_sql = f'select positionid, positionname from "HR"."Positions";'
            self.cursor.execute(pos_sql)
            data_pos = self.cursor.fetchall()
            div_sql = f'select divisionid, divisionname from "HR"."Divisions";'
            self.cursor.execute(div_sql)
            data_div = self.cursor.fetchall()
            #  Задание параметров для формы
            staffing = dict({"employees": dict(data_emp), "positions": dict(data_pos), "divisions": dict(data_div)})
            print(staffing)
            self.win_staffing = AddStaff(self, staffing)
            self.activeSQL_request = self.SQL_request_staff
            self.refreshView()
            #  --- Конец Заполнения и активации формы для редактирования данными текущего подразделения
        else:
            self.win_staffing = None
            self.refreshView()

        # --- Конец функции вызова формы редактирования назначения

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
    def __init__(self, parent1=None, user=None, new=False):
        super(EditEmp, self).__init__()
        self.parent = parent1
        self.user = user
        self.setupUi(self)
        self.initSignals()
        self.lineEdit_empid.setText(self.user["empid"])
        self.lineEdit_empid.setStyleSheet("background-color: grey")
        self.lineEdit_empname.setText(self.user["name"])
        self.dateEdit_emp_birthdate.setDate(self.user["birthday"])
        self.lineEdit_regaddress.setText(self.user["address"])
        self.lineEdit_emp_phone.setText(self.user["phone"])
        self.lineEdit_emp_mail.setText(self.user["email"])
        self.show()
        if new:
            self.emp_new()

    def initSignals(self):
        self.pushButton_update.clicked.connect(self.emp_update)
        self.pushButton_New.clicked.connect(self.emp_new)
        self.pushButton_Delete.clicked.connect(self.emp_delete)

    def emp_new(self) -> None:
        self.pushButton_New.hide()
        self.pushButton_update.setText("Save")
        self.pushButton_Delete.setText("Close")
        self.lineEdit_empid.setText("")
        self.lineEdit_empname.setText("")
        self.lineEdit_regaddress.setText("")
        self.lineEdit_emp_mail.setText("")
        self.lineEdit_emp_phone.setText("")
        self.dateEdit_emp_birthdate.setDate(datetime.date.today())
        pass

    def emp_update(self) -> None:
        if self.pushButton_update.text() == "Save":
            print("OK, вставляю новое значение")
            # year = self.dateEdit_emp_birthdate.date().year()
            # month = self.dateEdit_emp_birthdate.date().month()
            # day = self.dateEdit_emp_birthdate.date().day()
            # birthday_text = "'" + str(f'{year}-{month}-{day}') + "'"
            sql_update = f'begin;' + (f'INSERT INTO "HR"."Employees" (empname, birthdate, regaddress, contactphone, email)'
                                      f' VALUES (\'{self.lineEdit_empname.text()}\', current_date, \'{self.lineEdit_regaddress.text()}\','
                                      f' \'{self.lineEdit_emp_phone.text()}\', \'{self.lineEdit_emp_mail.text()}\');') + f'commit;'

            print(sql_update)
            self.parent.onSQL(sql_update)
            self.close()

        else:
            sql_update = f'begin;' + (f' UPDATE "HR"."Employees" SET '
                                      f'"empname" = \'{self.lineEdit_empname.text()}\','
                                      f'"regaddress" = \'{self.lineEdit_regaddress.text()}\','
                                      f' "contactphone" = \'{self.lineEdit_emp_phone.text()}\','
                                      f' "email" = \'{self.lineEdit_emp_mail.text()}\''
                                      f' WHERE "empid" = {self.user["empid"]};') + f'commit;'
            print(sql_update)
            self.parent.onSQL(sql_update)
            self.close()
        pass

    def emp_delete(self) -> None:
        if self.pushButton_Delete.text() == "Close":
            self.close()
        else:
            sql_delete = f'begin;' + f'DELETE FROM "HR"."Employees" WHERE "empid" = {self.user["empid"]};' + f'commit;'
            print(sql_delete)
            self.parent.onSQL(sql_delete)
            self.close()

        pass
# --- Конец описания класса редактирования пользователя


# Класс запускающий редактирование приказа
class EditOrder(QtWidgets.QWidget, Ui_Form_Order):
    def __init__(self, parent1=None, order=None, new=False):
        super(EditOrder, self).__init__()
        self.parent = parent1
        self.order = order
        self.setupUi(self)
        self.initSignals()
        self.lineEdit_orderid.setText(self.order["orderid"])
        self.lineEdit_orderid.setStyleSheet("background-color: grey")
        self.lineEdit_signedby.setText(self.order["signedby"])
        self.dateEdit_orderdate.setDate(self.order["orderdate"])
        self.lineEdit_order_number.setText(self.order["ordernumber"])
        self.show()
        if new:
            self.order_new()

    def initSignals(self):
        self.pushButton_update.clicked.connect(self.order_update)
        self.pushButton_New.clicked.connect(self.order_new)
        self.pushButton_Delete.clicked.connect(self.order_delete)

    def order_new(self) -> None:
        self.pushButton_New.hide()
        self.pushButton_update.setText("Save")
        self.pushButton_Delete.setText("Close")
        self.lineEdit_orderid.setText("")
        self.lineEdit_signedby.setText("")
        self.lineEdit_order_number.setText("")
        self.dateEdit_orderdate.setDate(datetime.date.today())
        pass

    def order_update(self) -> None:
        if self.pushButton_update.text() == "Save":
            print("OK, вставляю новое значение")
            sql_update = f'begin;' + (f'INSERT INTO "Orders"."Orders" (signedby, orderdate, ordernumber) VALUES (\'{self.lineEdit_signedby.text()}\','
                                      f' current_date, \'{self.lineEdit_order_number.text()}\');') + f'commit;'

            print(sql_update)
            self.parent.onSQL(sql_update)
            self.close()

        else:
            sql_update = f'begin;' + (f' UPDATE "Orders"."Orders" SET '
                                      f'"signedby" = \'{self.lineEdit_signedby.text()}\','
                                      f'"ordernumber" = \'{self.lineEdit_order_number.text()}\''
                                      f' WHERE "orderid" = {self.order["orderid"]};') + f'commit;'
            print(sql_update)
            self.parent.onSQL(sql_update)
            self.close()
        pass

    def order_delete(self) -> None:
        if self.pushButton_Delete.text() == "Close":
            self.close()
        else:
            sql_delete = f'begin;' + f'DELETE FROM "Orders"."Orders" WHERE "orderid" = {self.order["orderid"]};' + f'commit;'
            print(sql_delete)
            self.parent.onSQL(sql_delete)
            self.close()
        pass
# --- Конец описания класса редактирования приказов


# Класс запускающий редактирование должностей
class EditPosition(QtWidgets.QWidget, Ui_Form_Position):
    def __init__(self, parent1=None, position=None, new=False):
        super(EditPosition, self).__init__()
        self.parent = parent1
        self.position = position
        self.setupUi(self)
        self.initSignals()
        self.lineEdit_positionid.setText(self.position["positionid"])
        self.lineEdit_positionid.setStyleSheet("background-color: grey")
        self.lineEdit_positionname.setText(self.position["positionname"])
        self.lineEdit_salarymin.setText(self.position["salarymin"])
        self.lineEdit_salarymax.setText(self.position["salarymax"])
        self.show()
        if new:
            self.position_new()

    def initSignals(self):
        self.pushButton_update.clicked.connect(self.position_update)
        self.pushButton_New.clicked.connect(self.position_new)
        self.pushButton_Delete.clicked.connect(self.position_delete)

    def position_new(self) -> None:
        self.pushButton_New.hide()
        self.pushButton_update.setText("Save")
        self.pushButton_Delete.setText("Close")
        self.lineEdit_positionid.setText("")
        self.lineEdit_positionname.setText("")
        self.lineEdit_salarymin.setText("")
        self.lineEdit_salarymax.setText("")
        pass

    def position_update(self) -> None:
        if self.pushButton_update.text() == "Save":
            print("OK, вставляю новое значение")
            sql_update = f'begin;' + (f'INSERT INTO "HR"."Positions" (positionname, salarymin, salarymax) VALUES (\'{self.lineEdit_positionname.text()}\','
                                      f' \'{self.lineEdit_salarymin.text()}\', \'{self.lineEdit_salarymax.text()}\');') + f'commit;'

            print(sql_update)
            self.parent.onSQL(sql_update)
            self.close()

        else:
            sql_update = f'begin;' + (f' UPDATE "HR"."Positions" SET '
                                      f'"positionname" = \'{self.lineEdit_positionname.text()}\','
                                      f'"salarymin" = \'{self.lineEdit_salarymin.text()}\','
                                      f'"salarymax" = \'{self.lineEdit_salarymax.text()}\''
                                      f' WHERE "positionid" = {self.position["positionid"]};') + f'commit;'
            print(sql_update)
            self.parent.onSQL(sql_update)
            self.close()
        pass

    def position_delete(self) -> None:
        if self.pushButton_Delete.text() == "Close":
            self.close()
        else:
            sql_delete = f'begin;' + f'DELETE FROM "HR"."Positions" WHERE "positionid" = {self.position["positionid"]};' + f'commit;'
            print(sql_delete)
            self.parent.onSQL(sql_delete)
            self.close()
        pass
# --- Конец описания класса редактирования должностей


# Класс запускающий редактирование подразделений
class EditDivision(QtWidgets.QWidget, Ui_Form_Divisions):
    def __init__(self, parent1=None, division=None, new=False):
        super(EditDivision, self).__init__()
        self.parent = parent1
        self.division = division
        self.setupUi(self)
        self.initSignals()
        self.lineEdit_divisionid.setText(self.division["divisionid"])
        self.lineEdit_divisionid.setStyleSheet("background-color: grey")
        self.lineEdit_divisionname.setText(self.division["divisionname"])
        self.lineEdit_bossname.setText(self.division["bossname"])
        self.lineEdit_bossname.setStyleSheet("background-color: blue")
        self.lineEdit_status.setText(self.division["status"])
        self.show()
        if new:
            self.division_new()

    def initSignals(self):
        self.pushButton_update.clicked.connect(self.division_update)
        self.pushButton_New.clicked.connect(self.division_new)
        self.pushButton_Delete.clicked.connect(self.division_delete)

    def division_new(self) -> None:
        self.pushButton_New.hide()
        self.pushButton_update.setText("Save")
        self.pushButton_Delete.setText("Close")
        self.lineEdit_divisionid.setText("")
        self.lineEdit_divisionname.setText("")
        self.lineEdit_bossname.setText("")
        self.lineEdit_status.setText("")
        pass

    def division_update(self) -> None:
        if self.pushButton_update.text() == "Save":
            print("OK, вставляю новое значение")
            sql_update = f'begin;' + (f'INSERT INTO "HR"."Divisions" (divisionname, bossid, eventdate, eventtype)'
                                      f' VALUES (\'{self.lineEdit_divisionname.text()}\', \'22\', current_date, \'Open\');' + f'commit;')

            print(sql_update)
            self.parent.onSQL(sql_update)
            self.close()

        else:
            sql_update = f'begin;' + (f' UPDATE "HR"."Divisions" SET '
                                      f'"divisionname" = \'{self.lineEdit_divisionname.text()}\','
                                      f'"eventdate" = current_date,'
                                      f'"eventtype" = \'{self.lineEdit_status.text()}\''
                                      f' WHERE "divisionid" = {self.division["divisionid"]};') + f'commit;'
            print(sql_update)
            self.parent.onSQL(sql_update)
            self.close()
        pass

    def division_delete(self) -> None:
        if self.pushButton_Delete.text() == "Close":
            self.close()
        else:
            sql_delete = f'begin;' + f'DELETE FROM "HR"."Divisions" WHERE "divisionid" = {self.division["divisionid"]};' + f'commit;'
            print(sql_delete)
            self.parent.onSQL(sql_delete)
            self.close()
        pass
# --- Конец описания класса редактирования подразделений


# Класс добавления в журнал назначений
class AddStaff(QtWidgets.QWidget, Ui_Form_Staff):
    def __init__(self, parent1=None, staffing=None):
        super(AddStaff, self).__init__()
        self.parent = parent1
        self.staffing = staffing
        self.combo_div = self.staffing["divisions"]
        self.combo_pos = self.staffing["positions"]
        self.combo_emp = self.staffing["employees"]
        self.setupUi(self)
        self.initSignals()
        self.dateEdit.setDate(datetime.date.today())
        self.dateEdit.setStyleSheet("background-color: grey")
        self.emp_id = ""
        self.position_id = ""
        self.division_id = ""
        self.update_form()
        self.show()
        print(self.staffing["employees"])

    def initSignals(self) -> None:
        self.pushButton_Save.clicked.connect(self.addStaffing)
        self.pushButton_Cancel.clicked.connect(lambda: self.close())

    def update_form(self) -> None:
        for key, value in self.combo_emp.items():
            self.comboBox_emp.addItem(value)
        for key, value in self.combo_pos.items():
            self.comboBox_pos.addItem(value)
        for key, value in self.combo_div.items():
            self.comboBox_div.addItem(value)
        pass

    def addStaffing(self) -> None:
        for key, value in self.combo_emp.items():
            if self.comboBox_emp.currentText() == value:
                self.emp_id = key

        for key, value in self.combo_pos.items():
            if self.comboBox_pos.currentText() == value:
                self.position_id = key

        for key, value in self.combo_div.items():
            if self.comboBox_div.currentText() == value:
                self.division_id = key

        print("OK, вставляю новое значение")
        sql_update = f'begin;' + (f'INSERT INTO "Staff"."Staffing" (empid, positionid, divisionid, fte, salary, eventdate, eventtype, orderid)'
                                  f' VALUES (\'{self.emp_id}\', \'{self.position_id}\','
                                  f' \'{self.division_id}\', \'{self.lineEdit_fte.text()}\','
                                  f' \'{self.lineEdit_salary.text()}\', current_date, \'{self.comboBox_event.currentText()}\','
                                  f' \'{self.lineEdit_order.text()}\');' + f'commit;')

        print(sql_update)
        self.parent.onSQL(sql_update)
        self.close()
        pass
# --- Конец описания класса добавления в журнал назначений


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    win = DBClient()
    win.show()
    app.exec()
