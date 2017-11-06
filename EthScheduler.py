from PyQt4 import QtCore, QtGui

import sys 
import EthSchedulerGUI # This file holds MainWindow and all design related things
import EthSchedulerDialog

DEFAULT_MINING_ADDRESS = "A688479f3C579Fb7F57A4833dA48e393de3F7a98"

class EthScheduler(QtGui.QMainWindow, EthSchedulerGUI.Ui_EthScheduler, ):

    def __init__(self):
        # access variables, methods etc in the AquetiOperationGUI.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in AquetiOperationGUI.py file automatically
                            # It sets up layout and widgets that are defined

        self.currentWorkers = 0

        # setup signals and slots
        self.actionAdd_Worker.triggered.connect(self.addWorker)
        self.delete_worker_pushButton.clicked.connect(self.deleteWorker)
        self.start_worker_pushButton.clicked.connect(self.startWorker)


    def addWorker(self):
        '''
        add a worker to the interface
        '''
        ip, name, startTime, endTime, address, ok = EthSchedulerDialog.AddWorkerDialog.addWorker()
        if ok != QtGui.QDialog.Accepted:
            return


        self.worker_tableWidget.insertRow(self.currentWorkers)
        self.worker_tableWidget.setItem(self.currentWorkers, 0, QtGui.QTableWidgetItem(name))
        self.worker_tableWidget.setItem(self.currentWorkers, 1, QtGui.QTableWidgetItem(ip))
        self.worker_tableWidget.setItem(self.currentWorkers, 2, QtGui.QTableWidgetItem("IDLE"))
        self.worker_tableWidget.setItem(self.currentWorkers, 3, QtGui.QTableWidgetItem(startTime + "-" + endTime))
        self.worker_tableWidget.setItem(self.currentWorkers, 4, QtGui.QTableWidgetItem(address))



    def deleteWorker(self):
        '''
        '''
        return


    def startWorker(self):
        '''
        '''
        if self. start_worker_pushButton.isChecked():
            currentRow = self.worker_tableWidget.currentRow()

            addressName = self.worker_tableWidget.item(currentRow, 4).text()+"."+self.worker_tableWidget.item(currentRow, 0).text()

            cmd = ["./ethminer"]
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


    def runRemoteProcess(self, ip, cmd):
        '''
        runs Acos on all the tegras
        '''
        runRemoteProcess = subprocess.Popen(["ssh", "mosaic@%s"% ip, cmd], stdout=subprocess.PIPE, shell=False, stderr=subprocess.PIPE)
        runRemoteProcess.wait()


    def toggleAcos(self):
        '''
        Turns on and off Acos on all tegras
        '''

        self.updateStateLabel(WORKING)

        if self.start_camera_pushButton.isChecked():
            cmd = ['acosd','-R','acosdLog']

            if self.encoder_type_comboBox.currentIndex() == H264_ENCODER:
                cmd.append('-C')
                cmd.append('H264')
                cmd.append('-s')
                cmd.append('1')

            elif self.encoder_type_comboBox.currentIndex() == JPEG_ENCODER:
                cmd.append('-C')
                cmd.append('JPEG')
                cmd.append('-s')
                cmd.append('2')

            elif self.encoder_type_comboBox.currentIndex() == H265_ENCODER:
                cmd.append('-C')
                cmd.append('H265')
                cmd.append('-s')
                cmd.append('1')

            if self.enable_commands_checkBox.isChecked():
                self.printMessage(QtCore.QString(' '.join(cmd)))

            self.toggleAllAcos(' '.join(cmd),True)
            acosRunning = True
        else:

            self.closeAcosd()
            acosRunning = False

        self.updateStateLabel(IDLE)


    def closeAcosd(self):
        '''
        terminates Acosd
        '''
        if self.acosRunning:
            self.toggleAcosButtonState(False)
            cmd = ['pkill', '-2', 'acosd']
            if self.enable_commands_checkBox.isChecked():
                self.printMessage(QtCore.QString(' '.join(cmd)))

            self.toggleAllAcos(' '.join(cmd),False)




def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = EthScheduler()                        # We set the form to be our App
    form.show()                         # Show the form
    app.exec_()                         # and execute the app


if __name__ == '__main__':              # if we're running file directly and not importing it
    main()                              # run the main function