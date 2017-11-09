from PyQt4 import QtCore, QtGui

import sys 
import EthSchedulerGUI # This file holds MainWindow and all design related things
import EthSchedulerDialog
import subprocess
import os
import time
from datetime import datetime
from apscheduler.schedulers.qt import QtScheduler

DEFAULT_MINING_ADDRESS = "0x41B145f770e5FCFd691aCFD9E94aaE19817d52b9"
DEFAULT_CONFIG_LOCATION = "/home/bradley/.eth/"

class EthScheduler(QtGui.QMainWindow, EthSchedulerGUI.Ui_EthScheduler, ):

    def __init__(self):
        # access variables, methods etc in the AquetiOperationGUI.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in AquetiOperationGUI.py file automatically
                            # It sets up layout and widgets that are defined
        print("Starting EthScheduler: current time: "+str(datetime.now().time()))
        print("-----------------------------------------------")
        print(" ")

        self.workers = {}
        self.scheduler = QtScheduler()
        


        # fill table from file on disk
        self.readWorkerFile()

        for key, value in sorted(self.workers.items()):
            rowPosition = self.worker_tableWidget.rowCount()
            self.worker_tableWidget.insertRow(rowPosition)
            self.worker_tableWidget.setItem(rowPosition, 0, QtGui.QTableWidgetItem(value['name']))
            self.worker_tableWidget.setItem(rowPosition, 1, QtGui.QTableWidgetItem(value['ip']))
            self.worker_tableWidget.setItem(rowPosition, 2, QtGui.QTableWidgetItem(value['startTime']))
            self.worker_tableWidget.setItem(rowPosition, 3, QtGui.QTableWidgetItem(value['endTime']))
            self.worker_tableWidget.setItem(rowPosition, 4, QtGui.QTableWidgetItem(value['address']))

            # start schedules for each item
            self.scheduleWorker(value['name'],value['startTime'],value['endTime'])

        # setup signals and slots
        self.actionAdd_Worker.triggered.connect(self.addWorker)
        self.add_worker_pushButton.clicked.connect(self.addWorker)
        self.delete_worker_pushButton.clicked.connect(self.deleteWorker)
        self.start_worker_pushButton.clicked.connect(self.startWorker)
        self.actionQuit.triggered.connect(self.close)
        self.worker_tableWidget.cellClicked.connect(self.tableCellClicked)
        self.worker_tableWidget.cellChanged.connect(self.tableCellChanged)

        self.scheduler.start()


    def scheduleWorker(self, name, startTime, endTime):
        '''
        schedules a worker
        '''
        startTimeList = startTime.split(":")
        endTimeList = endTime.split(":")

        self.scheduler.add_job(self.launchWorker,  'cron', [name],id=name+'start', hour=startTimeList[0], minute=startTimeList[1],replace_existing=True)
        self.scheduler.add_job(self.stopWorker,  'cron', [name],id=name+'stop', hour=endTimeList[0], minute=endTimeList[1],replace_existing=True)
        print("Scheduling "+name + " to start at: "+ startTime+ " and end at: "+endTime)


    def removeWorkerSchedule(self, name):
        '''
        schedules a worker
        '''
        self.scheduler.remove_job(name+'start')
        self.scheduler.remove_job(name+'stop')


    def tableCellClicked(self, row, column):
        '''
        '''
        currentWorker = {}
        currentName = self.worker_tableWidget.item(row, 0).text()
        for key, item in  self.workers.items():
            if key == currentName:
                currentWorker =  self.workers[key]

        self.status_label.setText(currentWorker['status'])

    def tableCellChanged(self, row, column):
        '''
        '''
        currentName = self.worker_tableWidget.item(row, 0).text()

        for key, item in  self.workers.items():
            if key == currentName:

                if(column == 1):
                    self.workers[key]['ip'] = self.worker_tableWidget.item(row, column).text()
                elif(column == 2):
                    self.workers[key]['startTime'] = self.worker_tableWidget.item(row, column).text()
                elif(column == 3):
                    self.workers[key]['endTime'] = self.worker_tableWidget.item(row, column).text()
                elif(column == 4):
                    self.workers[key]['address'] = self.worker_tableWidget.item(row, column).text()

                self.updateWorkerFile();

                # clear name tasks
                # schedule.clear(self.workers[key]["name"])

                self.scheduleWorker(self.workers[key]['name'],self.workers[key]['startTime'],self.workers[key]['endTime'])



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
        self.worker_tableWidget.setItem(rowPosition, 2, QtGui.QTableWidgetItem(startTime))
        self.worker_tableWidget.setItem(rowPosition, 3, QtGui.QTableWidgetItem(endTime))
        self.worker_tableWidget.setItem(rowPosition, 4, QtGui.QTableWidgetItem(address))

        worker['username'] = str(username)
        worker['name'] = str(name)
        worker['ip'] = str(ip)
        worker['startTime'] = str(startTime)
        worker['endTime'] = str(endTime)
        worker['address'] = str(address)
        worker['status'] = 'IDLE'

        self.workers[str(name)] = worker


        #append to the file on disk
        self.updateWorkerFile();

        self.scheduleWorker(worker['name'],worker['startTime'],worker['endTime'])


    def deleteWorker(self):
        '''
        remove a worker from the interface
        '''
        currentRow = self.worker_tableWidget.currentRow()
        currentName = self.worker_tableWidget.item(currentRow, 0).text()

        for key, item in self.workers.items():
            if key == currentName:
                del self.workers[key]


        self.updateWorkerFile();
        self.worker_tableWidget.removeRow(currentRow)
        self.removeWorkerSchedule(currentName)



    def startWorker(self):
        '''
        '''
        currentRow = self.worker_tableWidget.currentRow()
        name = self.worker_tableWidget.item(currentRow, 0).text()

        if self.start_worker_pushButton.isChecked():
            self.launchWorker(str(name))
            self.start_worker_pushButton.setText('Stop Worker')
        else:
            self.stopWorker(str(name))
            self.start_worker_pushButton.setText('Start Worker')


    def launchWorker(self, name):
        '''
        starts the specified worker
        '''
        currentWorker = {}
        print("Starting: "+ name+" Time is: "+str(datetime.now().time()))

        for key, item in  self.workers.items():
            if key == name:
                currentWorker = self.workers[key]


        addressName = currentWorker['address']+"."+name
        cmd = ["~/.eth/ethminer"]
        cmd.append('--farm-recheck')
        cmd.append('400')
        cmd.append('--cl-global-work')
        cmd.append('16384')
        cmd.append('-G')
        cmd.append('-RH')
        cmd.append('-S')
        cmd.append('us1.ethermine.org:4444')
        cmd.append('-FS')
        cmd.append('us1.ethermine.org:14444')
        cmd.append('-O')
        cmd.append( str(addressName))

        print(' '.join(cmd))
        self.runRemoteProcess(currentWorker['ip'],currentWorker['username'], ' '.join(cmd))
        currentWorker['status'] = 'WORKING'

    def stopWorker(self, name):
        '''
        stops the specified worker
        '''
        currentWorker = {}
        print("Stopping: "+ name+" Time is: "+str(datetime.now().time())) 

        for key, item in  self.workers.items():
            if key == name:
                currentWorker = self.workers[key]


        cmd = ["pkill"]
        cmd.append('-15')
        cmd.append('ethminer')
        self.runRemoteProcess(currentWorker['ip'], currentWorker['username'], ' '.join(cmd))
        currentWorker['status'] = 'IDLE'


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