# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(459, 151)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("data/appicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.lne_receiverFilePath = QtWidgets.QLineEdit(self.tab)
        self.lne_receiverFilePath.setObjectName("lne_receiverFilePath")
        self.gridLayout_4.addWidget(self.lne_receiverFilePath, 0, 1, 1, 1)
        self.btn_receiveSaveDir = QtWidgets.QPushButton(self.tab)
        self.btn_receiveSaveDir.setObjectName("btn_receiveSaveDir")
        self.gridLayout_4.addWidget(self.btn_receiveSaveDir, 0, 2, 1, 1)
        self.btn_receive = QtWidgets.QPushButton(self.tab)
        self.btn_receive.setObjectName("btn_receive")
        self.gridLayout_4.addWidget(self.btn_receive, 1, 0, 1, 3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.lne_senderFilePath = QtWidgets.QLineEdit(self.tab_2)
        self.lne_senderFilePath.setObjectName("lne_senderFilePath")
        self.gridLayout_3.addWidget(self.lne_senderFilePath, 0, 1, 1, 1)
        self.btn_sendBrowse = QtWidgets.QPushButton(self.tab_2)
        self.btn_sendBrowse.setObjectName("btn_sendBrowse")
        self.gridLayout_3.addWidget(self.btn_sendBrowse, 0, 2, 1, 1)
        self.btn_send = QtWidgets.QPushButton(self.tab_2)
        self.btn_send.setObjectName("btn_send")
        self.gridLayout_3.addWidget(self.btn_send, 1, 0, 1, 3)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "KLocalShare"))
        self.label_2.setText(_translate("MainWindow", "File Path"))
        self.btn_receiveSaveDir.setText(_translate("MainWindow", "Save to directory..."))
        self.btn_receive.setText(_translate("MainWindow", "Receive File"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Receiver"))
        self.label.setText(_translate("MainWindow", "File Path"))
        self.btn_sendBrowse.setText(_translate("MainWindow", "Browse"))
        self.btn_send.setText(_translate("MainWindow", "Send File"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Sender"))

