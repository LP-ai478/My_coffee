import sqlite3

import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class Window(QMainWindow):
    def __init__(self, ed):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.connection = sqlite3.connect("coffee.db")
        self.pushButton.clicked.connect(self.show_table)
        self.textEdit.setPlainText("SELECT * FROM coffee")
        self.pushButton_2.clicked.connect(ed.show)

    def show_table(self):
        result = self.connection.cursor().execute(self.textEdit.toPlainText())
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(result):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))


class Edit(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.connection = sqlite3.connect("coffee.db")
        self.pushButton.clicked.connect(self.edit)
        self.textEdit.setPlainText("INSERT INTO coffee('id','Sort Name','Roasting degree','Ground/whole bean','Taste',"
                                   "'Price','Packing volume') VALUES(2,'Liberica','Middle','whole bean','???',300,400)")

    def edit(self):
        self.connection.cursor().execute(self.textEdit.toPlainText())
        self.connection.commit()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ed = Edit()
    ex = Window(ed)
    sys.excepthook = except_hook
    ex.show()
    sys.exit(app.exec())
