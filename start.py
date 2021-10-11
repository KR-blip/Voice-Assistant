#libraries

import pyttsx3 #text to speech
import speech_recognition as sr
import webbrowser
import datetime
import pywhatkit
import os
from wikipedia.wikipedia import search
import yfinance as yf
import pyjokes
import wikipedia



#functions..

#1.Listen to our microphones and return the audio as text using google

def transform():
    r=sr.Recognizer()
    print('Say something to voice assistant')
    with sr.Microphone() as source:
        r.pause_threshold=0.8
        said=r.listen(source)
        try:
            print('I am listening..')
            q=r.recognize_google(said, language='en')
            return q
        except sr.UnknownValueError:
            print("Sorry I didn't understand.")
            return "I am waiting"
        except sr.RequestError:
            print('Sorry the service is down.')
            return "I am waiting."
        except:
            return "I am waiting"

#2. Speaking the text
def speaking(message):
    engine=pyttsx3.init() #initialize an engine object which has the ability to speak
    engine.say(message)
    engine.runAndWait()

#3.returns the weekday name
def query_day():
    day=datetime.date.today()
    #print(day)      print date
    weekday=day.weekday()
    #print(weekday) #Will print the Number as Monday as 0 and on
    mapping={
        0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'
    }
    try:
        print(f'Today is {mapping[weekday]}')
        speaking(f'Today is {mapping[weekday]}')
    except:
        pass

#4. returns the time
def query_time():
    time=datetime.datetime.now().strftime('%I:%M:%S')
    speaking(f"The time is : {time[1]} o'clock and {time[3:5]} minutes")

#5.greeting from voice assistant
def whatsup():
    print('''Hi,my name is Cookie. I am your personal assistant.
    How may i help you?
    ''')
    speaking('''Hi,my name is Cookie. I am your personal assistant.
    How may i help you?
    ''')
    print('''Hi,my name is Cookie. I am your personal assistant.
    How may i help you?
    ''')

#6.the heart of our assistant. Takes queries an returns answers.
def heart():
    whatsup()
    start=True
    while(start):
        x=transform().lower()
        print(x)
        speaking(x)
        if 'start youtube' in x:
            speaking('starting youtube. Just a second')
            print('starting youtube. Just a second')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'start webbrowser' in x:
            speaking('opening browser')
            webbrowser.open('https://www/google.com')
            continue
        elif 'what day it is' in x:
            query_day()
            continue
        elif 'what time it is' in x:
            query_time()
            continue
        elif 'shutdown' in x:
            speaking('Ok i am shutting down. Bye, have a nice day')
            break
        elif 'from wikipedia' in x:
            speaking('Checking wikipedia')
            x=x.replace('wikipedia',"")
            result=wikipedia.summary(x,sentences=3)
            speaking('found on wikipedia')
            speaking(result)
            continue
        elif 'your name' in x:
            whatsup()
            continue
        elif 'search web' in x:
            pywhatkit.search(x)
            speaking('that is what i found')
            continue
        elif 'play' in x:
            x=x.replace('play','')
            speaking(f'playing {x}')
            pywhatkit.playonyt(x)
            continue
        elif 'joke' in x:
            speaking(pyjokes.get_joke())
            continue
        elif 'stock price' in x:
            search=x.split('of')[-1].strip()
            lookup={'apple':'AAPL',
            'amazon': 'AMZN',
            'google': 'GOOGL'}
            try:
                stock=lookup[search]
                stock=yf.Ticker(stock)
                currentprice=stock.info['regularMarketPrice']
                speaking(f'found it, the price for {search} is {currentprice}')
                continue
            except:
                speaking(f"sorry i have no data for {search}")
                continue



    

#Calling the function
heart()

""" #print all voices in your system.
engine=pyttsx3.init()
for voice in engine.getProperty('voices'):
    print(voice)

#You can download voices in your system and pass it to the id variable here and it'll change the voice to id set
id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0Tokens\TTS_MS_EN-US_ZIRA_11.0'
engine.setProperty('voice',id)
engine.say('Hello World')
engine.runAndWait() """




