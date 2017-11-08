# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EthScheduler.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_EthScheduler(object):
    def setupUi(self, EthScheduler):
        EthScheduler.setObjectName(_fromUtf8("EthScheduler"))
        EthScheduler.resize(560, 382)
        self.centralwidget = QtGui.QWidget(EthScheduler)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.worker_tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.worker_tableWidget.setDragEnabled(True)
        self.worker_tableWidget.setAlternatingRowColors(True)
        self.worker_tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.worker_tableWidget.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.worker_tableWidget.setShowGrid(False)
        self.worker_tableWidget.setObjectName(_fromUtf8("worker_tableWidget"))
        self.worker_tableWidget.setColumnCount(5)
        self.worker_tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.worker_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.worker_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.worker_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.worker_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.worker_tableWidget.setHorizontalHeaderItem(4, item)
        self.worker_tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.worker_tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.worker_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.worker_tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.worker_tableWidget.verticalHeader().setSortIndicatorShown(True)
        self.verticalLayout.addWidget(self.worker_tableWidget)
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 9)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.frame_2)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.status_label = QtGui.QLabel(self.frame_2)
        self.status_label.setObjectName(_fromUtf8("status_label"))
        self.horizontalLayout_2.addWidget(self.status_label)
        self.verticalLayout.addWidget(self.frame_2)
        self.start_worker_pushButton = QtGui.QPushButton(self.centralwidget)
        self.start_worker_pushButton.setCheckable(True)
        self.start_worker_pushButton.setObjectName(_fromUtf8("start_worker_pushButton"))
        self.verticalLayout.addWidget(self.start_worker_pushButton)
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.add_worker_pushButton = QtGui.QPushButton(self.frame)
        self.add_worker_pushButton.setObjectName(_fromUtf8("add_worker_pushButton"))
        self.horizontalLayout.addWidget(self.add_worker_pushButton)
        self.delete_worker_pushButton = QtGui.QPushButton(self.frame)
        self.delete_worker_pushButton.setObjectName(_fromUtf8("delete_worker_pushButton"))
        self.horizontalLayout.addWidget(self.delete_worker_pushButton)
        self.verticalLayout.addWidget(self.frame)
        EthScheduler.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(EthScheduler)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 560, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuEthScheduler = QtGui.QMenu(self.menubar)
        self.menuEthScheduler.setObjectName(_fromUtf8("menuEthScheduler"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        EthScheduler.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(EthScheduler)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        EthScheduler.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(EthScheduler)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionAdd_Worker = QtGui.QAction(EthScheduler)
        self.actionAdd_Worker.setObjectName(_fromUtf8("actionAdd_Worker"))
        self.menuEthScheduler.addAction(self.actionQuit)
        self.menuFile.addAction(self.actionAdd_Worker)
        self.menubar.addAction(self.menuEthScheduler.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(EthScheduler)
        QtCore.QMetaObject.connectSlotsByName(EthScheduler)

    def retranslateUi(self, EthScheduler):
        EthScheduler.setWindowTitle(_translate("EthScheduler", "EthScheduler", None))
        self.worker_tableWidget.setSortingEnabled(True)
        item = self.worker_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("EthScheduler", "Name", None))
        item = self.worker_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("EthScheduler", "IP", None))
        item = self.worker_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("EthScheduler", "Start Time", None))
        item = self.worker_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("EthScheduler", "End Time", None))
        item = self.worker_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("EthScheduler", "Address", None))
        self.label_2.setText(_translate("EthScheduler", "Status:", None))
        self.status_label.setText(_translate("EthScheduler", "IDLE", None))
        self.start_worker_pushButton.setText(_translate("EthScheduler", "Start Worker", None))
        self.add_worker_pushButton.setText(_translate("EthScheduler", "Add Worker", None))
        self.delete_worker_pushButton.setText(_translate("EthScheduler", "Delete Worker", None))
        self.menuEthScheduler.setTitle(_translate("EthScheduler", "EthScheduler", None))
        self.menuFile.setTitle(_translate("EthScheduler", "File", None))
        self.actionQuit.setText(_translate("EthScheduler", "Quit", None))
        self.actionAdd_Worker.setText(_translate("EthScheduler", "Add Worker", None))

