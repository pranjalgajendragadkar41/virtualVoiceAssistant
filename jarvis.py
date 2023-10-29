import pyautogui
import pyttsx3
import requests
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import sys
import time
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# to convert voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold = 1
        audio = r.listen(source, timeout=3, phrase_time_limit=6)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("say that again please...")
        return "none"
    return query


# to wish
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if 0 <= hour < 12:
        speak(f"good morning ma'am, its {tt}")
    elif 12 <= hour <= 18:
        speak(f"good afternoon ma'am, its {tt}")
    else:
        speak(f"good evening ma'am, its {tt}")
    speak("i am sherlock your desktop assistant. please tell me how may i help you")


if __name__ == "__main__":
    wish()
    while True:
        # if 1:

        query = takecommand().lower()

        # logic building for tasks
        # to open notepad
        if "open notepad" in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)
            speak("opening notepad for you ma'am")

        # to open wps office
        elif "open wps office" in query:
            wpath = "C:\\Users\\Admin\\AppData\\Local\\Kingsoft\\WPS Office\\ksolaunch.exe"
            os.startfile(wpath)
            speak("opening wps office for you ma'am")

        # to open command prompt
        elif "open command prompt" in query:
            os.system("start cmd")
            speak("opening command prompt for you ma'am")

        # to open camera
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()
            speak("opening camera for you ma'am")

        # to play music from local directory
        elif "play music" in query:
            music_dir = "D:\\Songs\\Hindi"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))
            speak("playing music for you ma'am")

        # to find my ip address
        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")

        # to find anything on wikipedia
        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)

        # to open youtube
        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
            speak("opening youtube for you ma'am")

        # to open geeksforgeeks website
        elif "open geeksforgeeks" in query:
            webbrowser.open("https://www.geeksforgeeks.org/")
            speak("opening geeksforgeeks for you ma'am")

        # to open google meet in browser
        elif "open google meet" in query:
            webbrowser.open("https://meet.google.com/?hs=197&pli=1&authuser=0")
            speak("opening google meet for you ma'am")

        # to open google classroom in browser
        elif "open google classroom" in query:
            webbrowser.open("https://classroom.google.com/u/0/h")
            speak("opening google classroom with your college id")

        # to open gmail in web browser
        elif "open gmail" in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
            speak("opening your gmail account for mksss cummins college of engineering for women")

        # to open google in web browser
        elif "open google" in query:
            speak("ma'am, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")
            speak("searching...")
            speak("here are the results..")

        # to open whatsapp and send message
        elif "send whatsapp message" in query:
            kit.sendwhatmsg("+918380872082", "This is testing protocol", 20, 48)
            speak("sending message...")

        # to play songs from youtube
        elif "play songs on youtube" in query:
            speak("playing hindi party hits on youtube")
            kit.playonyt("hindi party hits")

        # to quit assistant
        elif "no thanks" in query:
            speak("thank you ma'am for using me. have a good day ma'am.")
            sys.exit()

        # to close any application
        elif "close notepad" in query:
            speak("okay ma'am, closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "close wps office" in query:
            speak("okay ma'am, closing wps office")
            os.system("taskkill /f /im ksolaunch.exe")

        # to set alarm
        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn == 22:
                music_dir = "D:\\Alarm"
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                os.startfile(os.path.join(music_dir, rd))
                speak("please, wakeup ma'am. its time to study")
                speak("please get up ma'am otherwise i will call mummy")
                speak("Okay ma'am")

        # to find a joke
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        # to switch the window
        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        # to read the news
        elif "tell me latest news" in query:
            api_key = "6dfb9253a305410981f17116332ac1df"


            def news():
                main_url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=" + api_key
                response = requests.get(main_url).json()
                speak("please wait, fetching latest news")
                # print(response)
                # talk(response)
                article: response = response["articles"]
                # print(article)
                # talk(article)
                response_article = []
                for arti in article:
                    response_article.append(arti['title'])
                    # print(response_article)
                    # talk(response_article)
                for i in range(5):
                    # print(response_article[i])
                    speak(response_article[i])


            news()
        speak("ma'am, do you have any other work")
