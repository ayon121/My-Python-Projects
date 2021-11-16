#it is my 8th project in python 

#import dispatch form win32com.client
from win32com.client import Dispatch

#this function will help python to speak
def speak(str):
    speak = Dispatch(("SAPI.Spvoice"))
    speak.speak(str)

say = input("type somethink that you want to listen \n")

speak(say)


''''
#for this project we have to install pywin32 in our cmd
#to install pywin32 type in cmd "pip install pywin32"


Than import dispatch form win32com.client
To import this module type
"from win32com.client import Dispatch"

'''
