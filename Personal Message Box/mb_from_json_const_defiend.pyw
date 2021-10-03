import ctypes  # An included library with Python install.
import datetime
import os
import json

Messages = {}


def getMessages():
    with open('data.json', "r", encoding="utf8") as msgsdata:
        return json.load(msgsdata)


def Mbox(title, text):
    return ctypes.windll.user32.MessageBoxW(0, text, title, 0)


def picOneMessage(subject):
    return Messages[subject][-1]


def oneAlert(subject):
    msg = picOneMessage(subject)
    Mbox(msg[0], msg[1])


def main():
    global Messages
    Messages = getMessages()

    
    if datetime.datetime.now().hour > 18:
        Mbox("title", "content 😀")
    else:
        Mbox("title 2", "content 2")
		

if __name__ == '__main__':
    main()
