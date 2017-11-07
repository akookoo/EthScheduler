from PyQt4 import QtGui # Import the PyQt4 
from PyQt4 import QtCore # Import the PyQt4 

DEFAULT_MINING_ADDRESS = "0x41B145f770e5FCFd691aCFD9E94aaE19817d52b9"

class AddWorkerDialog(QtGui.QDialog):
    def __init__(self, parent = None):
        super(AddWorkerDialog, self).__init__(parent)

        layout = QtGui.QFormLayout(self)


        # nice widget for editing the date
        self.username = QtGui.QLineEdit("mosaic")
        layout.addRow("Username: ", self.username)

        self.ip = QtGui.QLineEdit("127.0.0.1")
        layout.addRow("IP: ", self.ip)

        self.name = QtGui.QLineEdit("Worker1")
        layout.addRow("Name: ", self.name)

        self.startTime = QtGui.QLineEdit("16:00")
        layout.addRow("Start Time: ", self.startTime)

        self.endTime = QtGui.QLineEdit("6:00")
        layout.addRow("End Time: ", self.endTime)

        self.address = QtGui.QLineEdit(DEFAULT_MINING_ADDRESS)
        layout.addRow("Address: ", self.address)


        # OK and Cancel buttons
        buttons = QtGui.QDialogButtonBox(
            QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel,
            QtCore.Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addRow(buttons)

        # get current date and time from the dialog
    def getUsername(self):
        return self.username.text()

    # get current date and time from the dialog
    def getIp(self):
        return self.ip.text()

    def getName(self):
        return self.name.text()

    def getStartTime(self):
        return self.startTime.text()

    def getEndTime(self):
        return self.endTime.text()

    def getAddress(self):
        return self.address.text()

    # static method to create the dialog and return (date, time, accepted)
    @staticmethod
    def addWorker(parent = None):
        dialog = AddWorkerDialog(parent)
        result = dialog.exec_()
        username = dialog.getUsername()
        ip = dialog.getIp()
        name = dialog.getName()
        startTime = dialog.getStartTime()
        endTime = dialog.getEndTime()
        address = dialog.getAddress()
        return (username, ip, name, startTime, endTime, address , result == QtGui.QDialog.Accepted)