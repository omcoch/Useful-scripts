import ctypes  # An included library with Python install.
import random
import datetime
import os

Msseages = [[('first title', "first content"), ("second title","second title.")]]


def Mbox(title, text):
	return ctypes.windll.user32.MessageBoxW(0, text, title, 0)


def picOneMessage(lib):
	byDay = datetime.datetime.today().weekday() % len(Msseages)
	msgs_today = Msseages[byDay]
	return msgs_today[random.randrange(0, len(msgs_today))]


def oneAlert():
	msg = picOneMessage(Msseages)
	Mbox(msg[0], msg[1])


def DoRandomPopUp(times = 1):
	 for i in range(times):
		 oneAlert()
	


def main():
 
	Mbox("another title","another content")
	if datetime.datetime.now().hour > 18: #depending on time
		Mbox("evening title","evening content")
	
	DoRandomPopUp()


if __name__ == '__main__':
    main()