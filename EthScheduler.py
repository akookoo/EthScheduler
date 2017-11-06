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

        # setup signals and slots
        self.actionAdd_Worker.triggered.connect(self.addWorker)
        self.delete_worker_pushButton.clicked.connect(self.deleteWorker)
        self.start_worker_pushButton.clicked.connect(self.startWorker)
        self.stop_worker_pushButton.clicked.connect(self.stopWorker)

    def addWorker(self):
        '''
        '''
        ip, name, startTime, endTime, address, ok = EthSchedulerDialog.AddWorkerDialog.addWorker()
        if ok != QtGui.QDialog.Accepted:
            return

        print(ip)
        print(name)
        print(startTime)
        print(endTime)
        print(address)

    def deleteWorker(self):
        '''
        '''
        return


    def startWorker(self):
        '''
        '''
        return


    def stopWorker(self):
        '''
        '''
        return




def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = EthScheduler()                        # We set the form to be our App
    form.show()                         # Show the form
    app.exec_()                         # and execute the app


if __name__ == '__main__':              # if we're running file directly and not importing it
    main()                              # run the main function