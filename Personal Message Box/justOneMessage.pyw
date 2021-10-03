import ctypes
import random

def Mbox(title, text):
    return ctypes.windll.user32.MessageBoxW(0, text, title, 1)
	

if (random.randrange(0,2) > 0):
	Mbox("first","123")
else:
	Mbox("second","456")