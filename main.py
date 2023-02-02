import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia 
import webbrowser as wb
import os
from selenium import webdriver
import psutil as pu
import pyjokes as pj
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager




# initialization of pyttsx3 module 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
  
# function for jokes  
def jokes():
    joke=pj.get_joke(language="en",category="neutral")
    print(joke)
    speak(joke)
        
# function for speaking something
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# function for wishing
def wish():
    hour = datetime.datetime.now().hour

    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!") 
    speak("I am Jolene . Please tell me,how may I help you ?")    

# function for time
def time():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    print(time)
    speak(time)

# function for date
def date():
    date = datetime.datetime.now().strftime("%d:%B:%Y")
    speak("the current date is")
    print(date)
    speak(date)

# function for cpu status
def cpu():
    usage = str(pu.cpu_percent())
    speak("cpu is at" + usage)
    battery =pu.sensors_battery()
    speak("battery is at")
    speak(battery) 


# taking command function from user
def takecommand():
        r = sr.Recognizer()
        
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1.5
            audio = r.listen(source)

        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:  
            print("Say that again please...")  
            return "None"
        return query

def chrome():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.google.com")
    
if __name__ == "__main__":
        wish()
        while True:
            query = takecommand().lower()

            if 'time' in query:
                time()

            elif 'what is your name' in query:
                speak(" i am Jolene your ai assitant") 

            elif 'who built you' in query:
                speak('Kawalmeet Singh')  

            elif 'in which language you are coded' in query:
                speak('Python')

            elif 'date' in query:
                date()
    

            elif 'play music' in query:
                music_dir = 'D:\\songs\\Favorite Songs2'
                songs = os.listdir(music_dir)
                print(songs)    
                os.startfile(os.path.join(music_dir, songs[0]))    


            elif 'system status' in query:
                cpu()

            elif 'joke' in query:
                jokes()

            elif 'news' in query:
                wb.open("bbcnews.com")  

            elif 'open youtube' in query:
                wb.open("youtube.com")

            elif 'open chrome' in query:
              chrome()

            elif 'open stack overflow' in query:
                wb.open("stackoverflow.com")   
    
            elif 'offline'in query:
                exit() 