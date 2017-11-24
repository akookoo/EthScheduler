# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EthScheduler.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EthScheduler(object):
    def setupUi(self, EthScheduler):
        EthScheduler.setObjectName("EthScheduler")
        EthScheduler.resize(560, 526)
        self.centralwidget = QtWidgets.QWidget(EthScheduler)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.worker_tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.worker_tableWidget.setDragEnabled(True)
        self.worker_tableWidget.setAlternatingRowColors(True)
        self.worker_tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.worker_tableWidget.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.worker_tableWidget.setShowGrid(False)
        self.worker_tableWidget.setObjectName("worker_tableWidget")
        self.worker_tableWidget.setColumnCount(3)
        self.worker_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.worker_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.worker_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.worker_tableWidget.setHorizontalHeaderItem(2, item)
        self.worker_tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.worker_tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.worker_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.worker_tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.worker_tableWidget.verticalHeader().setSortIndicatorShown(True)
        self.verticalLayout.addWidget(self.worker_tableWidget)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 9)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.status_label = QtWidgets.QLabel(self.frame_2)
        self.status_label.setObjectName("status_label")
        self.horizontalLayout_2.addWidget(self.status_label)
        self.verticalLayout.addWidget(self.frame_2)
        self.start_worker_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.start_worker_pushButton.setCheckable(True)
        self.start_worker_pushButton.setObjectName("start_worker_pushButton")
        self.verticalLayout.addWidget(self.start_worker_pushButton)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_worker_pushButton = QtWidgets.QPushButton(self.frame)
        self.add_worker_pushButton.setObjectName("add_worker_pushButton")
        self.horizontalLayout.addWidget(self.add_worker_pushButton)
        self.delete_worker_pushButton = QtWidgets.QPushButton(self.frame)
        self.delete_worker_pushButton.setObjectName("delete_worker_pushButton")
        self.horizontalLayout.addWidget(self.delete_worker_pushButton)
        self.verticalLayout.addWidget(self.frame)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.times_tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.times_tableWidget.setAlternatingRowColors(True)
        self.times_tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.times_tableWidget.setShowGrid(False)
        self.times_tableWidget.setObjectName("times_tableWidget")
        self.times_tableWidget.setColumnCount(3)
        self.times_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.times_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.times_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.times_tableWidget.setHorizontalHeaderItem(2, item)
        self.times_tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.times_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.times_tableWidget)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.add_time_pushButton = QtWidgets.QPushButton(self.frame_3)
        self.add_time_pushButton.setObjectName("add_time_pushButton")
        self.horizontalLayout_3.addWidget(self.add_time_pushButton)
        self.remove_time_pushButton = QtWidgets.QPushButton(self.frame_3)
        self.remove_time_pushButton.setObjectName("remove_time_pushButton")
        self.horizontalLayout_3.addWidget(self.remove_time_pushButton)
        self.verticalLayout.addWidget(self.frame_3)
        EthScheduler.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EthScheduler)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 560, 20))
        self.menubar.setObjectName("menubar")
        self.menuEthScheduler = QtWidgets.QMenu(self.menubar)
        self.menuEthScheduler.setObjectName("menuEthScheduler")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        EthScheduler.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EthScheduler)
        self.statusbar.setObjectName("statusbar")
        EthScheduler.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(EthScheduler)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAdd_Worker = QtWidgets.QAction(EthScheduler)
        self.actionAdd_Worker.setObjectName("actionAdd_Worker")
        self.menuEthScheduler.addAction(self.actionQuit)
        self.menuFile.addAction(self.actionAdd_Worker)
        self.menubar.addAction(self.menuEthScheduler.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(EthScheduler)
        QtCore.QMetaObject.connectSlotsByName(EthScheduler)

    def retranslateUi(self, EthScheduler):
        _translate = QtCore.QCoreApplication.translate
        EthScheduler.setWindowTitle(_translate("EthScheduler", "EthScheduler"))
        self.worker_tableWidget.setSortingEnabled(True)
        item = self.worker_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("EthScheduler", "Name"))
        item = self.worker_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("EthScheduler", "IP"))
        item = self.worker_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("EthScheduler", "Address"))
        self.label_2.setText(_translate("EthScheduler", "Status:"))
        self.status_label.setText(_translate("EthScheduler", "IDLE"))
        self.start_worker_pushButton.setText(_translate("EthScheduler", "Start Worker"))
        self.add_worker_pushButton.setText(_translate("EthScheduler", "Add Worker"))
        self.delete_worker_pushButton.setText(_translate("EthScheduler", "Delete Worker"))
        self.times_tableWidget.setSortingEnabled(True)
        item = self.times_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("EthScheduler", "Start"))
        item = self.times_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("EthScheduler", "End"))
        item = self.times_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("EthScheduler", "Mode"))
        self.add_time_pushButton.setText(_translate("EthScheduler", "Add Time"))
        self.remove_time_pushButton.setText(_translate("EthScheduler", "Remove Time"))
        self.menuEthScheduler.setTitle(_translate("EthScheduler", "EthScheduler"))
        self.menuFile.setTitle(_translate("EthScheduler", "File"))
        self.actionQuit.setText(_translate("EthScheduler", "Quit"))
        self.actionAdd_Worker.setText(_translate("EthScheduler", "Add Worker"))

