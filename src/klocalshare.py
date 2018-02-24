# -*- coding: utf-8 -*-
from PyQt5.QtCore import QModelIndex

import mainwindow, sys, config

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QIcon

from ksender import KSender
from kreceiver import KReceiver
from kfile import *
from khost import *

__version__ = "0.5"


class KLocalShare(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = mainwindow.Ui_MainWindow();
        self.ui.setupUi(self)

        self.dirs = config.dirs

        self.init_klocalshare()
        self.setWindowIcon(QIcon(self.dirs.appicon))

    def init_klocalshare(self):
        # self.setTabOrder(self.ui.lne_bisey1, self.ui.lne_name)    # First tab order
        # self.setTabOrder(self.ui.lne_bisey2, self.ui.lne_surName) # Second tab order
        self.ui.btn_receive.clicked.connect(self.receive)
        self.ui.btn_send.clicked.connect(self.send)
        self.ui.btn_sendBrowse.clicked.connect(self.browser)
        self.ui.btn_receiveSaveDir.clicked.connect(self.saveDir)

    def receive(self):
        host = KHost("0.0.0.0", 9301)
        file = KFileWriter(self.dirName + "/new-ft.zip")

        receiver = KReceiver(host, file)
        receiver.start_listening()
        receiver.socket.close()

    def send(self):
        host = KHost("0.0.0.0", 9301)
        file = KFileReader(self.fileName, 2 ** 13)
        sender = KSender(host, file)
        sender.start_sending()

    def show_message(self, msg, timeout=3000):
        self.ui.statusBar.showMessage(msg, timeout)

    def browser(self):
        self.fileName = QFileDialog.getOpenFileName()[0]
        self.ui.lne_senderFilePath.setText(self.fileName)

    def saveDir(self):
        self.dirName = QFileDialog.getExistingDirectory()
        self.ui.lne_receiverFilePath.setText(self.dirName)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = KLocalShare()

    myapp.show()
    sys.exit(app.exec_())
