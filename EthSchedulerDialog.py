from PyQt5 import QtGui, QtCore, QtWidgets
import settings


class AddWorkerDialog(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super(AddWorkerDialog, self).__init__(parent)

        layout = QtWidgets.QFormLayout(self)


        # nice widget for editing the date
        self.username = QtWidgets.QLineEdit("mosaic")
        layout.addRow("Username: ", self.username)

        self.ip = QtWidgets.QLineEdit("127.0.0.1")
        layout.addRow("IP: ", self.ip)

        self.name = QtWidgets.QLineEdit("Worker1")
        layout.addRow("Name: ", self.name)

        self.address = QtWidgets.QLineEdit(settings.DEFAULT_MINING_ADDRESS)
        layout.addRow("Address: ", self.address)


        # OK and Cancel buttons
        buttons = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel,
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
        address = dialog.getAddress()
        return (username, ip, name, address , result == QtWidgets.QDialog.Accepted)



class AddTimeDialog(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super(AddTimeDialog, self).__init__(parent)

        layout = QtWidgets.QFormLayout(self)

        # nice widget for editing the date
        self.startTime = QtWidgets.QLineEdit("16:00")
        layout.addRow("Start Time: ", self.startTime)

        self.endTime = QtWidgets.QLineEdit("7:00")
        layout.addRow("End Time: ", self.endTime)

        self.mode = QtWidgets.QComboBox()
        self.mode.addItems(settings.SCHEDULE_MODES)
        layout.addRow("Occurrence: ", self.mode)

        # enable day selection if weekly selected
        self.day = QtWidgets.QComboBox()
        self.day.addItems(settings.DAYS_OF_WEEK)
        layout.addRow("Day: ", self.day)

        # OK and Cancel buttons
        buttons = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel,
            QtCore.Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addRow(buttons)

    # get times and mode
    def getStartTime(self):
        return self.startTime.text()

    def getEndTime(self):
        return self.endTime.text()

    def getMode(self):
        return self.mode.currentText()

    def getDay(self):
        return self.day.currentText()

    # static method to create the dialog and return (date, time, accepted)
    @staticmethod
    def addTime(parent = None):
        dialog = AddTimeDialog(parent)
        result = dialog.exec_()
        startTime = dialog.getStartTime()
        endTime = dialog.getEndTime()
        mode = dialog.getMode()
        day = dialog.getDay()
        return (startTime, endTime, mode, day, result == QtWidgets.QDialog.Accepted)
