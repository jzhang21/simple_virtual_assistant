import pyttsx3
import datetime
import calendar
import speech_recognition as sr
import sys
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui 
import psutil
import pyjokes

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def time():
    #Time = datetime.datetime.now().strftime("%I:%M:%S")
    time = datetime.datetime.now().strftime("%I:%M %p")
    speak("the current time is")
    speak(time)
    
def date():
    year = int(datetime.datetime.now().year)
    month = calendar.month_name[datetime.datetime.now().month]
    #date = int(datetime.datetime.now().day)
    day = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(month)
    speak(day)
    speak(year)

def wishme():
    #speak("Welcome back!")
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good morning!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    time()
    date()
    speak("How can I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        print("Listening. . .")
        r.pause_threshold = 1
        audio = r.listen(source) #sound input
    try:
        print("Recognizing. . .")
        query = r.recognize_google(audio, language='en-in') # convert input 
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please. . ")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('xxx@gmail.com', 'password')
    server.sendmail('xxx@gmail.com', to, content)

def screenshot():
    img = pyautogui.screenshot()
    img.save"C:\Users\Jared Zhang\Desktop\ss.png"

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at' + usuage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        
        if 'time' in query:
            time()    
        
        elif 'date' in query:
            date()
        
        elif 'wikipedia' in query: # improve functionality
            speak("Searching. . . ")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        
        elif 'send email' in query: # improve functionality
            try:
                speak("What should I say") 
                content = takeCommand()
                to = 'xxx@gmail.com'
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Unable to send email")
       
        elif 'search in chrome' in query: # improve functionality
            speak("What should I search for?")
            chromepath = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + '.com')
        
        elif 'logout' in query:
            os.system("shutdown -l")
        
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        
        elif 'play songs' in query: # improve functionality
            songs_dir = 'D:\\Music'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))
        
        elif 'remember that' in query: # improve functionality
            speak("What should I remember?")
            data = takeCommand()
            speak("You said to remember that" + data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()
            
        elif 'do you know anything' in query: #improve wording
            remember = open('data.txt', 'r')
            speak("You said to me to remember that" + remember.read())

        elif 'screenshot' in query:
            screenshot()
            speak("Done!")
        
        elif 'cpu' in query:
            cpu()
            
        elif 'joke' in query:
            jokes()
        
        elif 'offline' in query:
            sys.exit()
    

