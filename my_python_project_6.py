#It is my 6th python project
from win32com.client import Dispatch

#This function will help to speak python
def speak(str):
    speak = Dispatch(("SAPI.SpVoice"))
    speak.speak(str)

#now i am calling speak function
speak("hello world")
speak ("it is my 10th python project")
speak ("here my python is speaking")
speak ("i am happy today")
speak ("be allways happy")




'''In this project I am using pywin32.
pywin32 will help python to speak


To install pywin32 type in cmd 
"pip install pywin32"

To import this module type

"from win32com.client import Dispatch"
'''
