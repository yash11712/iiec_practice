import os
import pyttsx3

pyttsx3.speak("Hello there! Chat with me your requirements!")
while True:
    string = input("Specify the requirment >>> ")
    if (('run' in string) or ('start' in string) or ('open' in string) or ('execute' in string))  and (('chrome' in string) or ('browser' in string)):
        pyttsx3.speak('opening chrome')
        os.system('start chrome')
        
    elif (('run' in string) or ('start' in string) or ('open' in string) or ('execute' in string))   and (('notepad' in string) or ('editor' in string)):
        pyttsx3.speak('opening notepad')
        os.system('start notepad')
        
    elif (('run' in string) or ('start' in string) or ('open' in string) or ('execute' in string)) and ('media' in string) and ('player') in string:
        pyttsx3.speak('opening media player')
        os.system('start wmplayer')
    
    elif (('run' in string) or ('start' in string) or ('open' in string) or ('execute' in string)) and ('pycharm' in string) :
        pyttsx3.speak('opening pycharm')
        os.system('start pycharm')

    elif (('exit' in string) or ('quit' in string) or ('end' in string)):
        break
    
    else:
        pyttsx3.speak("we don't support it!")
    

