import pyttsx3 as p #import the python module that converts text to speech 
import speech_recognition as sr #import python module that converts speech to text
import time
import selenium_web
import music
from news_display import *
from jokes import *
import randfacts
import sys
from weather import *
import datetime


engine=p.init() #used to initiate the pyttsx3 module to convert text to speech

def speak(text):
        # Set the speech rate (words per minute)
        rate = engine.getProperty('rate')
       
        # print(rate)
        engine.setProperty('rate', 150)  # You can adjust the value to slow down or speed up the speech
        
        voice=engine.getProperty('voices')
        # print(voice)
        engine.setProperty('voice',voice[1].id)
        engine.say(text) #asks our computer to say this particular word.
        engine.runAndWait() #asks our computer to wait until the sentence gets completed.


def wishme():
    hour= int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        return("Morning")
    elif hour>=12 and hour<16:
        return("Afternoon")
    else:
        return("Evening")

today_date=datetime.datetime.now()
r = sr.Recognizer()

speak("Hello SIMRAN, Good "+wishme())
speak(" I am your voice assistant")
speak("Today is " + today_date.strftime("%d") + " " + today_date.strftime("%b") + " and it's currently " + today_date.strftime("%I:%M %p"))
speak("How are you?")


with sr.Microphone() as source:
    r.energy_threshold=10000  #for filtering out background noises and listening.... to the high voice only
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening........")
    audio = r.listen(source) 
    try: 
       text = r.recognize_google(audio)
       print(text)
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand what you said. Exiting the program")
        sys.exit()


if "what" and "about" and "you" in text:
      speak("I am having a great day today")

speak("What can i do for you?")

with sr.Microphone() as source:
    r.energy_threshold=10000  #for filtering out background noises and listening.... to the high voice only
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening........")
    audio = r.listen(source)  
    text2 = r.recognize_google(audio)
    print(text2)



   
if "information" in text2 :
    speak("you need information related to which topic?")
      
    with sr.Microphone() as source:
        r.energy_threshold=10000  #for filtering out background noises and listening........ to the high voice only
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening....")
        audio = r.listen(source)  
        infor = r.recognize_google(audio)
        print(infor)
    speak("searching {} in wikipedia".format(infor))
    
    assist = selenium_web.Inflow()
    assist.get_info(infor)
    


if "news" in text2:
    
    print("Sure, Now I'll read the latest news to you")
    speak("Sure, Now I'll read the latest news to you")
    arr = news()
    for news_item in arr:
        print(news_item)
        speak(news_item)
    sys.exit()


if "fact" in text2 or "facts" in text2:
    speak("Sure")
    x=randfacts.get_fact()
    print(x)
    print("Did you know that?\n "+x)
    speak("Did you know that "+x)
    sys.exit()


if "joke" in text2:
    print("Sure, get ready for some chuckles")
    speak("Sure, get ready for some chuckles")

    pr=joke1()
    
    print(pr[0])
    speak(pr[0])
    print(pr[1])
    speak(pr[1])
    sys.exit()

if "weather" in text2:
    speak("Temperature in Ranchi is " + str(temp()) + " degree Celsius" + " and with " + str(des()))
    print("Temperature in Ranchi is " + str(temp()) + " degree Celsius" + " and with " + str(des()))


if "exit" in text2:
    speak("Exiting the program")
    print("Exiting the program")
    sys.exit()

if "play" in text2 or "video"  or "youtube" in text2:

    speak("Which video you want me to play")
     
    with sr.Microphone() as source:
        r.energy_threshold=10000  #for filtering out background noises and listening........ to the high voice only
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening....")
        audio = r.listen(source)  
        vid = r.recognize_google(audio)
        print(vid)
    speak("searching {} in youtube".format(vid))
    
    assist = music.Inflow()
    assist.music(vid)
    sys.exit()


else:
    speak("Sorry! I am unable to do that, i am still under construction!")
