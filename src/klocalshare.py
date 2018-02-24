__version__ = "0.1"

# -*- coding: utf-8 -*-
from PyQt5.QtCore import QModelIndex

import mainwindow, sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5.QtGui import QIcon

__version__ = "1.0"

class Frec(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = mainwindow.Ui_MainWindow();
        self.ui.setupUi(self)

        self.init_klocalshare()
        #self.setWindowIcon(QIcon(self.dirs.appicon))

    def init_klocalshare(self):
        #self.setTabOrder(self.ui.lne_firstName, self.ui.lne_lastName)
        #self.setTabOrder(self.ui.lne_lastName, self.ui.comboBox_department)

        self.ui.btn_receive.clicked.connect(self.receive)
        '''
        self.ui.btn_register.clicked.connect(self.save_new_member)
        self.ui.btn_delete.clicked.connect(self.delete_member)
        self.ui.btn_createDesktopEntry.clicked.connect(self.create_desktop_entry)
        self.ui.btn_clear.clicked.connect(self.clear_form)
        self.ui.btn_export.clicked.connect(self.export_cvs)
        self.ui.btn_import.clicked.connect(self.import_cvs)
        self.ui.btn_exportAsCVS.clicked.connect(self.export_cvs)
        self.ui.checkBox_saveLocal.stateChanged.connect(self.save_local)

        self.ui.btn_connectDb.clicked.connect(self.connect_db)

        self.connect_db()
        self.show_member_at_tableWidget()'''

    def receive(self):
        self.show_message("Receive file...")

    def send(self):
        self.show_message("Sending file...")

    def show_message(self, msg, timeout=3000):
        self.ui.statusBar.showMessage(msg, timeout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = Frec()

    myapp.show()
    sys.exit(app.exec_())