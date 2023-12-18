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
from PySide6 import QtGui, QtWidgets

from DB_Forms import NewEmpForm
from ui.ConnectionForm import Ui_Form
from ui.DBClient import Ui_MainWindow


class DB_client(QtWidgets.QMainWindow, Ui_MainWindow):

    # Блок инициации клиента для работы с базой данных
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initConsts()
        self.host = ""
        self.port = ""
        self.dbname = ""
        self.user = ""
        self.password = ""
        self.setupUi(self)
        self.setWindowTitle("Клиент для работы с базой данных")
        self.initCreds()

        self.win = None
        self.win2 = None
        # self.initThreads()
        self.initDB()
        self.initSignals()
        self.installEventFilter(self)

        if self.connect.status == 1:
            self.show_view_table(self.SQL_request_emp) # Первыми показываем список сотрудников

# Обработчик событий
    def eventFilter(self, obj, event):
        if event.type() == QtWidgets.QTableView.entered:
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

            SQL_request1 = sql_input[0]

            self.cursor.execute(SQL_request1)

            data_emp = self.cursor.fetchall()
            # print(data_emp)


            model = QtGui.QStandardItemModel()
            model.setHorizontalHeaderLabels(sql_input[2])


            for elem in data_emp:
                list_items = []
                for i in range(sql_input[1]):
                    list_items.append(QtGui.QStandardItem(str(elem[i])))
                model.appendRow(list_items)

            self.tableView.setModel(model)
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

        # Сигналы на редактирование в главном окне



# Слоты для описания действий на кнопки
    def onMenuAboutClicked(self) -> None:
        """
        В статус бар выводится информация о программе
        :return:
        """
        text_about = "Это программа подключения и работы с учебной базой DevDB2023 на сервере gpngw.avalon.ru. Все права защищены"
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
        SQL_request2 = self.textEdit.toPlainText()
        self.cursor.execute(SQL_request2)
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



    def initCreds(self) -> None:
        self.host = "vpngw.avalon.ru"
        self.port = "5432"
        self.dbname = "DevDB2023_vadkal"
        self.user = "pguser"
        self.password = "Pa$$w0rd"

    def Connect(self) -> None:
        if self.win2 is None:
            self.win2 = ServerConnection()
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

# Форма для создания подключения к серверу
class ServerConnection(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)



if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = DB_client()

    win.show()

    app.exec()
