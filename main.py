import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib


print("Initializing jarvis")


MASTER = "uma" 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
#speak function will pronounce the string which is passed to it.

def speak(text):
    engine.say(text)
    engine.runAndWait()

#speak("uma is a good girl")

#this function will wish you as per the current time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)

    if hour>=0 and hour<=12:
        speak("Good Morning" + MASTER)

    elif hour>=12 and hour<=18:
          speak("Good Afternoon" + MASTER) 
    else:
        speak("Good Evening" + MASTER)

    speak("I am jarvis. How may I help you?")    

#this function take command from the microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en_in')
        print(f"user said:{query}\n")

    except Exception as e:
        print("say that again please")
        query = ("None")
    return query

    def sendEmail(to,content):
        server=smtplib.SMTP("smtp.gmail.com",587)
        server.ehlo()
        server.starttls()
        server.login('youremail@gmail.com','password')
        server.sendmail('umaparwani1234@gmail.com',to,content)
        server.close()
#Main program starts here.
#speak("Initializing Jarvis...")
wishMe()
query = takeCommand()

 #logic forexecuting basic tasks as per the query
while 1:
    if 'wikipedia' in query.lower():
        speak('Searching wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences =2)
        print(results)
        speak(results)
    elif 'open youtube' in query.lower():
       # webbrowser.open("youtube.com")
        url= "youtube.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
    
    elif 'open google' in query.lower():
       # webbrowser.open("youtube.com")
        url= "google.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
    elif 'open reddit' in query.lower():
           # webbrowser.open("youtube.com")
        url= "reddit.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)    
    elif 'play music' in query.lower():
        songs_dir = "c:\\Users\\User\\Downloards\\music"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir,songs[0]))
    elif 'the time' in query.lower():
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"(MASTER) the time is (strTime)")
    elif'open code' in query.lower():
        codePath="C:\\Users\\User\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
        os.startfile(codePath)        
    elif'email to uma' in query.lower():
        try:
            speak('what should i send')
            content = takecommand()
            to = "umaparwani1234@gmail.com"
            sendEmail(to,content)
            speak("Email has been sent successfully")
        except exception as e:
            print(e)