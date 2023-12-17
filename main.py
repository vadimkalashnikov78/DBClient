import psycopg2
from PySide6 import QtCore, QtGui, QtWidgets
import db_ui
from DB_Forms import NewEmpForm

class DB_client(QtWidgets.QMainWindow, db_ui.Ui_MainWindow):

    # Блок инициации клиента для работы с базой данных
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Клиент для работы с базой данных")
        self.initSignals()
        self.initDB()
        self.installEventFilter(self)


        self.take_EmployeesList()

# Обработчик событий
    def eventFilter(self, obj, event):
        # if event.type() == QtWidgets.QMenu.keyPressEvent(self) and obj == self.menuAbout:
        #     # self.onMenuAboutClicked()
        # print(event)

        return super().eventFilter(obj, event)




    # Функция подключения к базе данных и вывода основного списка работников
    def initDB(self) -> None:
        self.connect = psycopg2.connect(host="vpngw.avalon.ru",
                                        port="5432",
                                        dbname="DevDB2023_vadkal",
                                        user="pguser",
                                        password="Pa$$w0rd")
        self.cursor = self.connect.cursor()
        pass


    def take_EmployeesList(self) -> None:

        SQL_request1 = 'Select empid, empname, birthdate, email from "HR"."Employees" order by empid;'

        self.cursor.execute(SQL_request1)

        data_emp = self.cursor.fetchall()


        model = QtGui.QStandardItemModel()
        model.setHorizontalHeaderLabels(["Employee's id", "Name", "Birthdate", "E-mail"])


        for elem in data_emp:
            item1 = QtGui.QStandardItem(str(elem[0]))
            item2 = QtGui.QStandardItem(str(elem[1]))
            item3 = QtGui.QStandardItem(str(elem[2]))
            item4 = QtGui.QStandardItem(str(elem[3]))
            model.appendRow([item1, item2, item3, item4])

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
        #
        self.pushButtonRequest.clicked.connect(self.onPushButtonRequestClicked)
        #
        self.pushButton_Edit.clicked.connect(self.onPushButtonEditClicked)
        #
        self.pushButtonRefresh.clicked.connect(self.onPushButtonRefreshClicked)
        #
        # self.menuAbout.menuAction().triggered.connect(self.onMenuAboutClicked())




# Слоты для описания действий на кнопки
    def onMenuAboutClicked(self) -> None:
        """

        :return:
        """
        text_about = "Это программа подключения и работы с учебной базой DevDB2023 на сервере gpngw.avalon.ru \n Все права защищены"
        print(text_about)
        pass

    def onPushButtonAddClicked(self) -> None:
        """
        Добавление элемента в список сотрудников
        :return:
        """
        new_emp_window = QtWidgets.QApplication
        new_emp = NewEmpForm()
        new_emp.show()

        new_emp_window.exec()

    def onPushButtonDeleteClicked(self):
        pass

    def onPushButtonRequestClicked(self):
        pass

    def onPushButtonRefreshClicked(self):
        pass

    def onPushButtonEditClicked(self):
        pass





if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = DB_client()

    win.show()

    app.exec()
