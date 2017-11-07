from PyQt4 import QtCore, QtGui

import sys 
import EthSchedulerGUI # This file holds MainWindow and all design related things
import EthSchedulerDialog
import subprocess
import os
import schedule
import time

DEFAULT_MINING_ADDRESS = "0x41B145f770e5FCFd691aCFD9E94aaE19817d52b9"
DEFAULT_CONFIG_LOCATION = "/home/bradley/.eth/"

class EthScheduler(QtGui.QMainWindow, EthSchedulerGUI.Ui_EthScheduler, ):

    def __init__(self):
        # access variables, methods etc in the AquetiOperationGUI.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in AquetiOperationGUI.py file automatically
                            # It sets up layout and widgets that are defined

        self.currentWorkers = 0
        self.workers = {}

        # setup signals and slots
        self.actionAdd_Worker.triggered.connect(self.addWorker)
        self.delete_worker_pushButton.clicked.connect(self.deleteWorker)
        self.start_worker_pushButton.clicked.connect(self.startWorker)
        self.actionQuit.triggered.connect(self.close)

        # fill table from file on disk
        self.readWorkerFile()

        for key, value in sorted(self.workers.items()):
            self.worker_tableWidget.insertRow(self.currentWorkers)
            self.worker_tableWidget.setItem(self.currentWorkers, 0, QtGui.QTableWidgetItem(value['name']))
            self.worker_tableWidget.setItem(self.currentWorkers, 1, QtGui.QTableWidgetItem(value['ip']))
            self.worker_tableWidget.setItem(self.currentWorkers, 2, QtGui.QTableWidgetItem("IDLE"))
            self.worker_tableWidget.setItem(self.currentWorkers, 3, QtGui.QTableWidgetItem(value['startTime']))
            self.worker_tableWidget.setItem(self.currentWorkers, 4, QtGui.QTableWidgetItem(value['address']))
            self.currentWorkers =self.currentWorkers+1
        # start schedules for each item


    def updateWorkerFile(self):
        '''
        updates a file on disk containing workers
        '''
        target = open(DEFAULT_CONFIG_LOCATION+'workers.txt', 'w')
        target.write(str(self.workers))


    def readWorkerFile(self):
        '''
        read the worker file into memory
        '''
        if os.path.isfile(DEFAULT_CONFIG_LOCATION+'workers.txt'):
            with open(DEFAULT_CONFIG_LOCATION+'workers.txt', 'r') as f:
                s = f.read()
                self.workers = eval(s)


    def addWorker(self):
        '''
        add a worker to the interface
        '''
        worker = {}


        username, ip, name, startTime, endTime, address, ok = EthSchedulerDialog.AddWorkerDialog.addWorker()
        if ok != QtGui.QDialog.Accepted:
            return

        # add worker to the next line in the table
        self.worker_tableWidget.insertRow(self.currentWorkers)
        self.worker_tableWidget.setItem(self.currentWorkers, 0, QtGui.QTableWidgetItem(name))
        self.worker_tableWidget.setItem(self.currentWorkers, 1, QtGui.QTableWidgetItem(ip))
        self.worker_tableWidget.setItem(self.currentWorkers, 2, QtGui.QTableWidgetItem("IDLE"))
        self.worker_tableWidget.setItem(self.currentWorkers, 3, QtGui.QTableWidgetItem(startTime + "-" + endTime))
        self.worker_tableWidget.setItem(self.currentWorkers, 4, QtGui.QTableWidgetItem(address))

        worker['username'] = str(username)
        worker['name'] = str(name)
        worker['ip'] = str(ip)
        worker['startTime'] = str(startTime)
        worker['endTime'] = str(endTime)
        worker['address'] = str(address)

        self.workers[str(name)] = worker
        self.currentWorkers =self.currentWorkers+1

        #append to the file on disk
        self.updateWorkerFile();

    def deleteWorker(self):
        '''
        remove a worker from the interface
        '''
        currentRow = self.worker_tableWidget.currentRow()
        currentName = self.worker_tableWidget.item(currentRow, 0).text()

        for key, item in  self.workers.items():
            if key == currentName:
                del self.workers[key]

        self.updateWorkerFile();

        self.worker_tableWidget.removeRow(currentRow)


    def startWorker(self):
        '''
        '''
        currentRow = self.worker_tableWidget.currentRow()
        currentIp = self.worker_tableWidget.item(currentRow, 1).text()

        if self.start_worker_pushButton.isChecked():
            addressName = self.worker_tableWidget.item(currentRow, 4).text()+"."+self.worker_tableWidget.item(currentRow, 0).text()
            cmd = ["~/.eth/ethminer"]
            cmd.append('--farm-recheck')
            cmd.append('2000')
            cmd.append('-G')
            cmd.append('-S')
            cmd.append('us1.ethermine.org:4444')
            cmd.append('-FS')
            cmd.append('us1.ethermine.org:14444')
            cmd.append('-O')
            cmd.append( str(addressName))

            print(cmd)
            self.runRemoteProcess(str(currentIp), ' '.join(cmd))
            self.start_worker_pushButton.setText('Stop Worker')
            self.worker_tableWidget.setItem(currentRow, 2, QtGui.QTableWidgetItem('RUNNING'))
        else:
            cmd = ["pkill"]
            cmd.append('-15')
            cmd.append('ethminer')
            self.runRemoteProcess(str(currentIp),' '.join(cmd))
            self.start_worker_pushButton.setText('Start Worker')
            self.worker_tableWidget.setItem(currentRow, 2, QtGui.QTableWidgetItem('IDLE'))


    def runRemoteProcess(self, ip, cmd):
        '''
        runs Acos on all the tegras
        '''
        runRemoteProcess = subprocess.Popen(["ssh", "mosaic@%s"% ip, cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def closeEvent(self, event):
        '''
        catches the close event 
        '''
        reply = QtGui.QMessageBox.question(self, 'Shutdown',
            "Are you sure you want to quit?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            self.shutdown()
        else:
            event.ignore()
        

    def shutdown(self):
        '''
        shuts down the GUI
        '''
        # stop all workers?

        self.close()


def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = EthScheduler()                        # We set the form to be our App
    form.show()                         # Show the form
    app.exec_()                         # and execute the app


if __name__ == '__main__':              # if we're running file directly and not importing it
    main()                              # run the main function