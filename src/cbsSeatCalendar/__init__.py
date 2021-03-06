# Top-level objects and function for command line entry point
from cbsSeatCalendar.cbsCalendarUpdateClass import CBSaccount

__version__ = '1.1.1'


def executeCBScal():
	from getpass import getpass
	
	username = input('CBS username: ')
	password = getpass('Password: ')
	
	myAcc = CBSaccount(username, password)
	myAcc.updateCalendar()
