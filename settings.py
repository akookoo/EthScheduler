from PyQt5 import QtGui, QtCore, QtWidgets

def init():

	global DEFAULT_CONFIG_LOCATION
	global DEFAULT_MINING_ADDRESS
	global SCHEDULE_DAILY
	global SCHEDULE_WEEKLY
	global SCHEDULE_ONCE
	global SCHEDULE_MODES
	global DAYS_OF_WEEK
	global YELLOW
	global GREEN
	global WORKER_FILE

	DEFAULT_CONFIG_LOCATION = "/home/bradley/.eth/"
	DEFAULT_MINING_ADDRESS = "0x41B145f770e5FCFd691aCFD9E94aaE19817d52b9"
	SCHEDULE_DAILY = 'daily'
	SCHEDULE_WEEKLY = 'weekly'
	SCHEDULE_ONCE = 'once'
	SCHEDULE_MODES = [SCHEDULE_ONCE, SCHEDULE_DAILY, SCHEDULE_WEEKLY ]
	DAYS_OF_WEEK = ['none','mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
	YELLOW = QtGui.QColor(216,212,127)
	GREEN = QtGui.QColor(88,127,62)
	WORKER_FILE = 'worker_data.txt'