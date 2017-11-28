#!/usr/bin/env python3

from PyQt5 import QtGui, QtCore, QtWidgets
import sys 
import EthSchedulerGUI # This file holds MainWindow and all design related things
import EthSchedulerDialog
import subprocess
import os
import time
from datetime import datetime
from apscheduler.schedulers.qt import QtScheduler
import settings


class EthScheduler(QtWidgets.QMainWindow, EthSchedulerGUI.Ui_EthScheduler, ):

    status_changed = QtCore.pyqtSignal(str, bool)

    def __init__(self):
        # access variables, methods etc in the AquetiOperationGUI.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in AquetiOperationGUI.py file automatically
                            # It sets up layout and widgets that are defined
        print("Starting EthScheduler: current time: "+str(datetime.now().time()))
        print("-----------------------------------------------")
        print(" ")

        # create default save location if it doesn't exist
        if not os.path.exists(settings.DEFAULT_CONFIG_LOCATION):
            os.makedirs(settings.DEFAULT_CONFIG_LOCATION)

        self.workers = {}
        self.scheduler = QtScheduler()
        
        # fill table from file on disk
        self.readWorkerFile()

        for key, value in sorted(self.workers.items()):


            # add the item to the table
            self.addItemToTable( value['name'], value['ip'], value['address'])
            
            # start schedules for each item
            for key, time in sorted(value['times'].items()):
                self.scheduleWorker(value['name'],time['startTime'],time['endTime'], time['mode'], time['day'])
                self.addItemToTimeTable(time['startTime'], time['endTime'], time['mode'])

        # setup signals and slots
        self.actionAdd_Worker.triggered.connect(self.addWorker)
        self.add_worker_pushButton.clicked.connect(self.addWorker)
        self.delete_worker_pushButton.clicked.connect(self.deleteWorker)
        self.actionQuit.triggered.connect(self.close)
        self.worker_tableWidget.cellClicked.connect(self.tableCellClicked)
        self.worker_tableWidget.cellChanged.connect(self.tableCellChanged)
        self.add_time_pushButton.clicked.connect(self.addTime)
        self.remove_time_pushButton.clicked.connect(self.removeTime)

        self.status_changed.connect(self.setWorkerColor)

        self.scheduler.start()


    def addItemToTimeTable(self, startTime, endTime, mode ):
        '''
        add an item to the time table
        '''
        row = self.times_tableWidget.rowCount()
        self.times_tableWidget.insertRow(row)

        self.times_tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(startTime))
        self.times_tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(endTime))
        self.times_tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(mode))

        self.times_tableWidget.setCurrentCell(row,0)

    def addItemToTable(self, name, ip, address):
        '''
        adds an item to the table
        '''
        row = self.worker_tableWidget.rowCount()
        self.worker_tableWidget.insertRow(row)

        self.worker_tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(name))
        self.worker_tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(ip))
        self.worker_tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(address))
        self.worker_tableWidget.item(row, 0).setFlags(QtCore.Qt.ItemIsEnabled)

        self.worker_tableWidget.setCurrentCell(row,0)


    def scheduleWorker(self, name, startTime, endTime, mode, day):
        '''
        schedules a worker
        '''
        startTimeList = startTime.split(":")
        endTimeList = endTime.split(":")

        currentTime = datetime.now()
        startPulse = currentTime.replace(hour=int(startTimeList[0] ),minute=int(startTimeList[1]))

        endTimePulse = int(endTimeList[1]) -1
        if endTimePulse > 59:
            endTimePulse = 1
        elif endTimePulse < 1:
            endTimePulse = 59
        endPulse = currentTime.replace(hour=int(endTimeList[0]), minute=endTimePulse )

        # print ("startPulse:"+str(startPulse))
        # print ("endPulse:"+str(endPulse))

        if mode == settings.SCHEDULE_DAILY:
            self.scheduler.add_job(self.launchWorker,  'cron', [name],id=name+startTime,hour=startTimeList[0], minute=startTimeList[1],replace_existing=True)
            self.scheduler.add_job(self.stopWorker,  'cron', [name],id=name+endTime,hour=endTimeList[0], minute=endTimeList[1],replace_existing=True)
            self.scheduler.add_job(self.workerPulse, 'cron', [name],id=name+startTime+'check', second=30, start_date=startPulse,end_date=endPulse,replace_existing=True)
            print("Scheduling "+name + " to start at: "+ startTime+ " and end at: "+endTime+ " everyday")
        elif mode == settings.SCHEDULE_WEEKLY:
            # print(day)
            self.scheduler.add_job(self.launchWorker,  'cron', [name],id=name+startTime,day_of_week=str(day), hour=startTimeList[0], minute=startTimeList[1],replace_existing=True)
            self.scheduler.add_job(self.stopWorker,  'cron', [name],id=name+endTime,day_of_week=str(day), hour=endTimeList[0], minute=endTimeList[1],replace_existing=True)
            self.scheduler.add_job(self.workerPulse, 'cron', [name],id=name+startTime+'check',day_of_week=str(day), second=30, start_date=startPulse,end_date=endPulse,replace_existing=True)
            print("Scheduling "+name + " to start at: "+ startTime+ " and end at: "+endTime+ " on "+ day)
        elif mode == settings.SCHEDULE_ONCE:
            self.scheduler.add_job(self.launchWorker, 'date',[name],id=name+startTime, run_date=datetime(startPulse))
            self.scheduler.add_job(self.stopWorker, 'date',[name],id=name+endTime, run_date=datetime(endPulse))
            # add pulse for interval
            # self.scheduler.add_job(self.workerPulse, 'cron', [name],id=name+'check', second=30, start_date=startPulse,end_date=endPulse,replace_existing=True)
            print("Scheduling "+name + " to start at: "+ startTime+ " and end at: "+endTime)




    def removeWorkerSchedule(self, name):
        '''
        schedules a worker
        '''
        # self.scheduler.remove_job(name+'start')
        # self.scheduler.remove_job(name+'stop')
        # self.scheduler.remove_job(name+'check')


    def tableCellClicked(self, row, column):
        '''
        triggered when a table cell gets clicked
        '''
        self.times_tableWidget.setRowCount(0)

        currentWorker = {}
        currentName = self.worker_tableWidget.item(row, 0).text()
        for key, item in  self.workers.items():
            if key == currentName:
                currentWorker =  self.workers[key]
                for key, time in sorted(self.workers[key]['times'].items()):
                    self.addItemToTimeTable(time['startTime'], time['endTime'], time['mode'])

    def tableCellChanged(self, row, column):
        '''
        triggered when a table cell is changed
        '''
        currentName = self.worker_tableWidget.item(row, 0).text()

        for key, item in  self.workers.items():
            if key == currentName:

                if(column == 1):
                    self.workers[key]['ip'] = str(self.worker_tableWidget.item(row, column).text())
                elif(column == 4):
                    self.workers[key]['address'] = str(self.worker_tableWidget.item(row, column).text())

                self.updateWorkerFile();

                # clear name tasks
                # schedule.clear(self.workers[key]["name"])


    def updateWorkerFile(self):
        '''
        updates a file on disk containing workers
        '''

        target = open(settings.DEFAULT_CONFIG_LOCATION+settings.WORKER_FILE, 'w')
        target.write(str(self.workers))


    def readWorkerFile(self):
        '''
        read the worker file into memory
        '''
        if os.path.isfile(settings.DEFAULT_CONFIG_LOCATION+settings.WORKER_FILE):
            with open(settings.DEFAULT_CONFIG_LOCATION+settings.WORKER_FILE, 'r') as f:
                s = f.read()
                self.workers = eval(s)


    def addTime(self):
        '''
        add worker time
        '''
        #append to the file on disk

        startTime, endTime, mode, day, ok = EthSchedulerDialog.AddTimeDialog.addTime(self)
        if ok != QtWidgets.QDialog.Accepted:
            return

        self.addItemToTimeTable( startTime, endTime, mode)

        currentRow = self.worker_tableWidget.currentRow()
        currentName = self.worker_tableWidget.item(currentRow, 0).text()

        time = {}

        time['startTime'] = str(startTime)
        time['endTime'] = str(endTime)
        time['mode'] = str(mode)
        time['day'] = str(day)


        self.workers[currentName]['times'][time['startTime']+time['endTime']] = time
        self.updateWorkerFile();
        self.scheduleWorker(currentName,time['startTime'],time['endTime'], time['mode'], time['day'])

    def removeTime(self):
        '''
        remove worker time
        '''
        currentRow = self.worker_tableWidget.currentRow()
        currentName = self.worker_tableWidget.item(currentRow, 0).text()

        currentTimeRow = self.times_tableWidget.currentRow()
        currentTimeStart = self.times_tableWidget.item(currentTimeRow, 0).text()
        currentTimeEnd = self.times_tableWidget.item(currentTimeRow, 1).text()

        del self.workers[currentName]['times'][currentTimeStart+currentTimeEnd]

        self.updateWorkerFile();
        self.times_tableWidget.removeRow(currentTimeRow)
        self.removeWorkerSchedule(currentName)


    def addWorker(self):
        '''
        add a worker to the interface
        '''
        worker = {}


        username, ip, name, address, ok = EthSchedulerDialog.AddWorkerDialog.addWorker(self)
        if ok != QtWidgets.QDialog.Accepted:
            return

        # add worker to the next line in the table
        self.addItemToTable( name, ip, address)

        worker['username'] = str(username)
        worker['name'] = str(name)
        worker['ip'] = str(ip)
        worker['address'] = str(address)
        worker['status'] = 'IDLE'
        worker['times'] = {}

        self.workers[str(name)] = worker


        #append to the file on disk
        self.updateWorkerFile();


    def deleteWorker(self):
        '''
        remove a worker from the interface
        '''
        currentRow = self.worker_tableWidget.currentRow()
        currentName = self.worker_tableWidget.item(currentRow, 0).text()

        toRemove = {}
        for key, item in self.workers.items():
            if key == currentName:
                del self.workers[key]


        self.updateWorkerFile();
        self.worker_tableWidget.removeRow(currentRow)
        self.removeWorkerSchedule(currentName)



    def checkWorker(self, name):
        '''
        checks the system for running ethminer
        '''
        CHECK = "ps cax | grep ethminer"

        currentWorker = {}
        for key, item in  self.workers.items():
            if key == name:
                currentWorker = self.workers[key]

        checkProcesses = subprocess.Popen(["ssh", "%s@%s"% (currentWorker['username'],currentWorker['ip']), CHECK], stdout=subprocess.PIPE, shell=False, stderr=subprocess.PIPE)
        checkStdout = checkProcesses.stdout.readlines()

        ethminer = "ethminer"
        for process in checkStdout[:]:

            if ethminer in str(process)[:]:
                # self.setWorkerColor(name,True)
                self.status_changed.emit(name,True)
                return True
        # self.setWorkerColor(name,False)
        self.status_changed.emit(name,False)
        return False

    def setWorkerColor(self, name, enable):
        '''
        '''
        for row in range(self.worker_tableWidget.rowCount()):
            currentName = self.worker_tableWidget.item(row, 0).text()
            if currentName == name:
                if enable:
                    self.worker_tableWidget.item(row, 0).setBackground(settings.GREEN)
                else:
                    self.worker_tableWidget.item(row, 0).setBackground(settings.YELLOW)
    

    def workerPulse(self, name):
        '''
        checks worker and restarts if not found
        '''
        rc = self.checkWorker(name)
        
        if not rc:
            print("Unable to detect: "+ name+" Restarting: "+str(datetime.now().time()))
            self.launchWorker(name)
        else:
            print(name+" was found: "+str(datetime.now().time()))


    def launchWorker(self, name):
        '''
        starts the specified worker
        '''
        currentWorker = {}
        print("Starting: "+ name+" Time is: "+str(datetime.now().time()))
        # self.setWorkerColor(name,True)
        self.status_changed.emit(name,True)

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
        cmd.extend(['>>', '~/.eth/log.txt', '2>&1'])

        # print(' '.join(cmd))
        self.runRemoteProcess(currentWorker['ip'],currentWorker['username'], ' '.join(cmd))
        currentWorker['status'] = 'WORKING'

    def stopWorker(self, name):
        '''
        stops the specified worker
        '''
        currentWorker = {}
        print("Stopping: "+ name+" Time is: "+str(datetime.now().time())) 
        # self.setWorkerColor(name,False)
        self.status_changed.emit(name,False)
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
        runRemoteProcess = subprocess.Popen(["ssh", "%s@%s"%(username, ip), cmd])

    def closeEvent(self, event):
        '''
        catches the close event 
        '''
        reply = QtWidgets.QMessageBox.question(self, 'Shutdown',
            "Are you sure you want to quit?", QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            self.shutdown()
        else:
            event.ignore()
        

    def shutdown(self):
        '''
        shuts down the GUI
        '''
        # stop all workers?
        for key, item in  self.workers.items():
            self.stopWorker(self.workers[key]['name'])

        self.close()


def main():
    QtCore.QMetaType.type("QVector");
    settings.init()
    app = QtWidgets.QApplication(sys.argv)  # A new instance of QApplication
    form = EthScheduler()                        # We set the form to be our App
    form.show()                         # Show the form
    app.exec_()                         # and execute the app


if __name__ == '__main__':              # if we're running file directly and not importing it
    main()                              # run the main function