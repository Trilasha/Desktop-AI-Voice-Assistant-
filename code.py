from black import main
import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Wish you a very Good Morning!")
    
    elif hour>=12 and hour<18:
        speak("Wish you a very Good Afternoon!")

    else:
        speak("Wish you a very Good Evening!")
    speak("Hope you are doing well.Please tell me ma'am how may I help you?")

def takeCommand():
    #It takes microphone input from the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Yes I am all ears...please speak")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print("Just wait for a minute...let me recognize what you said")
        query=r.recognize_google(audio,language='en-in')
        print(f"So you said that : {query}\n")

    except Exception as e:
        print("Sorry:( but I couldn't get you...Speak that again please")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('abc@gmail.com','password')
    server.sendmail('abc@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir='D:\\songs11'
            #thats the location of my music directory
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[43]))
            #will generate the 43rd song available in the queue
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"So ma'am, the time is {strTime}")
        elif 'open code' in query:
            codePath="C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'email to xyz' in query:
            # create dictionaries making names as the keys and their emailIDS as the values
            try:
                # takecommand will return whatever we speak in the form of a string
                speak("What should I say?")
                content=takeCommand()
                to = "xyz@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                print("Oops the mail couldn't be sent.Try once again later")
