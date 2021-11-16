
#here i am importing voice recognition.
import speech_recognition as sr
#this is for takeing command for microphone
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ("listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
        print("  ")
    try:
        text = r.recognize_google(audio , language= 'eng-us')
        print (text)
    except Exception as e:
        print("plz say that again")
takecommand()
