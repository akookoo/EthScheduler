
def init():

	global DEFAULT_CONFIG_LOCATION
	global DEFAULT_MINING_ADDRESS
	global SCHEDULE_DAILY
	global SCHEDULE_WEEKLY
	global SCHEDULE_ONCE
	global SCHEDULE_MODES
	global DAYS_OF_WEEK

	DEFAULT_CONFIG_LOCATION = "/home/bradley/.eth/"
	DEFAULT_MINING_ADDRESS = "0x41B145f770e5FCFd691aCFD9E94aaE19817d52b9"
	SCHEDULE_DAILY = 'DAILY'
	SCHEDULE_WEEKLY = 'WEEKLY'
	SCHEDULE_ONCE = 'ONCE'
	SCHEDULE_MODES = [SCHEDULE_ONCE, SCHEDULE_DAILY, SCHEDULE_WEEKLY ]
	DAYS_OF_WEEK = ['NONE','MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']