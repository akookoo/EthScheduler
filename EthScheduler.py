from PyQt4 import QtCore, QtGui

import sys 
import EthSchedulerGUI # This file holds MainWindow and all design related things
import EthSchedulerDialog
import subprocess
import os
import schedule
import time
import _thread

DEFAULT_MINING_ADDRESS = "0x41B145f770e5FCFd691aCFD9E94aaE19817d52b9"
DEFAULT_CONFIG_LOCATION = "/home/bradley/.eth/"

class EthScheduler(QtGui.QMainWindow, EthSchedulerGUI.Ui_EthScheduler, ):

    def __init__(self):
        # access variables, methods etc in the AquetiOperationGUI.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in AquetiOperationGUI.py file automatically
                            # It sets up layout and widgets that are defined

        self.workers = {}

        # setup signals and slots
        self.actionAdd_Worker.triggered.connect(self.addWorker)
        self.delete_worker_pushButton.clicked.connect(self.deleteWorker)
        self.start_worker_pushButton.clicked.connect(self.startWorker)
        self.actionQuit.triggered.connect(self.close)

        # fill table from file on disk
        self.readWorkerFile()

        for key, value in sorted(self.workers.items()):
            rowPosition = self.worker_tableWidget.rowCount()
            self.worker_tableWidget.insertRow(rowPosition)
            self.worker_tableWidget.setItem(rowPosition, 0, QtGui.QTableWidgetItem(value['name']))
            self.worker_tableWidget.setItem(rowPosition, 1, QtGui.QTableWidgetItem(value['ip']))
            self.worker_tableWidget.setItem(rowPosition, 2, QtGui.QTableWidgetItem("IDLE"))
            self.worker_tableWidget.setItem(rowPosition, 3, QtGui.QTableWidgetItem(value['startTime']))
            self.worker_tableWidget.setItem(rowPosition, 4, QtGui.QTableWidgetItem(value['endTime']))
            self.worker_tableWidget.setItem(rowPosition, 5, QtGui.QTableWidgetItem(value['address']))

            # start schedules for each item
            schedule.every().day.at(value["startTime"]).do(self.launchWorker, value['name'])
            schedule.every().day.at(value["endTime"]).do(self.stopWorker, value['name'])


        # start the update thread
        self.updateSchedule()

    def updateSchedule(self):

        def helper(self):
            while True:
                schedule.run_pending()
                time.sleep(1)
            
        _thread.start_new_thread(helper,(self,))


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
        rowPosition = self.worker_tableWidget.rowCount()
        self.worker_tableWidget.insertRow(rowPosition)
        self.worker_tableWidget.setItem(rowPosition, 0, QtGui.QTableWidgetItem(name))
        self.worker_tableWidget.setItem(rowPosition, 1, QtGui.QTableWidgetItem(ip))
        self.worker_tableWidget.setItem(rowPosition, 2, QtGui.QTableWidgetItem("IDLE"))
        self.worker_tableWidget.setItem(rowPosition, 3, QtGui.QTableWidgetItem(startTime))
        self.worker_tableWidget.setItem(rowPosition, 4, QtGui.QTableWidgetItem(endTime))
        self.worker_tableWidget.setItem(rowPosition, 5, QtGui.QTableWidgetItem(address))

        worker['username'] = str(username)
        worker['name'] = str(name)
        worker['ip'] = str(ip)
        worker['startTime'] = str(startTime)
        worker['endTime'] = str(endTime)
        worker['address'] = str(address)

        self.workers[str(name)] = worker


        #append to the file on disk
        self.updateWorkerFile();

        schedule.every().day.at(worker["startTime"]).do(self.launchWorker, worker['name'])
        schedule.every().day.at(worker["endTime"]).do(self.stopWorker, worker['name'])

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
        name = self.worker_tableWidget.item(currentRow, 0).text()

        if self.start_worker_pushButton.isChecked():
            self.launchWorker(str(name))
            self.start_worker_pushButton.setText('Stop Worker')
            self.worker_tableWidget.setItem(currentRow, 2, QtGui.QTableWidgetItem('RUNNING'))
        else:
            self.stopWorker(str(name))
            self.start_worker_pushButton.setText('Start Worker')
            self.worker_tableWidget.setItem(currentRow, 2, QtGui.QTableWidgetItem('IDLE'))


    def launchWorker(self, name):
        '''
        starts the specified worker
        '''
        currentWorker = {}
        print("starting: %s"%name)

        for key, item in  self.workers.items():
            if key == name:
                currentWorker = self.workers[key]


        addressName = currentWorker['address']+"."+name
        cmd = ["~/.eth/ethminer"]
        cmd.append('--farm-recheck')
        cmd.append('2000')
        cmd.append('-G')
        cmd.append('-S')
        cmd.append('us1.ethermine.org:4444')
        cmd.append('-FS')
        cmd.append('us1.ethermine.org:14444')
        cmd.append('-O')
        cmd.append( addressName)

        print(cmd)
        self.runRemoteProcess(currentWorker['ip'],currentWorker['username'], ' '.join(cmd))

    def stopWorker(self, name):
        '''
        stops the specified worker
        '''
        currentWorker = {}
        print("stopping: %s"%name)

        for key, item in  self.workers.items():
            if key == name:
                currentWorker = self.workers[key]


        cmd = ["pkill"]
        cmd.append('-15')
        cmd.append('ethminer')
        self.runRemoteProcess(currentWorker['ip'], currentWorker['username'], ' '.join(cmd))


    def runRemoteProcess(self, ip, username, cmd):
        '''
        runs Acos on all the tegras
        '''
        runRemoteProcess = subprocess.Popen(["ssh", "%s@%s"%(username, ip), cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

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