import pyautogui
import platform
import wolframalpha
import requests
import speech_recognition as sr
import pyttsx3
import time
import datetime
import wikipedia
import webbrowser
import os
import json
import pyjokes
import imdb
from translate import Translator
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')
def speak(text):
    engine.say(text)
    engine.runAndWait()
def wish():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)
        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

print("Loading Anish AI personal assistant ")
speak("Loading Anish AI personal assistant ")
wish()
while True:
    speak("Tell me how can I help you now?")
    statement = takeCommand().lower()
    if statement==0:
        continue
    if 'wikipedia' in statement:

        speak('Searching Wikipedia...')
        statement =statement.replace("wikipedia", "")
        results = wikipedia.summary(statement, sentences=3)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif 'open youtube' in statement:
        webbrowser.open_new_tab("https://www.youtube.com")
        speak("youtube is open now")
        time.sleep(5)

    elif 'open google' in statement:
        webbrowser.open_new_tab("https://www.google.com")
        speak("Google chrome is open now")
        time.sleep(5)

    elif 'open gmail' in statement:
        webbrowser.open_new_tab("gmail.com")
        speak("Google Mail open now")
        time.sleep(5)
    elif 'time' in statement:
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"the time is {strTime}")
    elif 'news' in statement:
        news = webbrowser.open_new_tab("https://zeenews.india.com/top-news")
        speak("please wait i will opening the news headlines......")
        print(news)
        time.sleep(6)
    elif 'search'  in statement:
        statement = statement.replace("search", "")
        webbrowser.open_new_tab(statement)
        time.sleep(5)
    elif 'open stack overflow' in statement:
        speak("here you go to stackover flow in just second")
        webbrowser.open("stackoverflow.com")
    elif 'question' in statement:
        speak('I can answer  computational and geographical questions  ...so please ask the question')
        question=takeCommand()
        client = wolframalpha.Client("R9XEJ9-V55QUE4VUJ")
        res = client.query(question)
        answer = next(res.results).text
        speak(answer)
        print(answer)
    elif 'who are you' in statement or 'what can you do' in statement:
        speak('I am deskto voice assistant ')
    elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
        speak("I was built by Smith singh")
        print("I was built by Smith singh")
    elif "shutdown" in statement:
        if platform.system() == "Windows":
            os.system('shutdown -s')
            speak("your os is shutdown.....please close all the running applications")
        elif platform.system() == "Linux" :
            os.system("shutdown -h now")
            speak("your Linux is shutdown....")
        else:
            print("machine not supported!")  
    elif "restart" in statement:
        if platform.system() == "Windows":
            os.system("shutdown /r /t  1")
            speak("your os is restarting in just minute .....")
        elif platform.system() == "Linux" :
            os.system('reboot now')
            speak("your linux is restarting in just minute .....")
        else:
            speak("machine not supported!!")
            print("machine  not supported!") 
    elif  "open word" in statement: 
        speak("Opening Microsoft Word") 
        os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs")   
    elif "open Excel" in statement:
        speak("opening ms-excel")
        os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office")
        time.sleep(5)
    elif 'play music' in statement:
        speak("opening music .......please wait")
        music='C:\\Users\smith\Music\music\mp3'
        songs=os.listdir(music)
        print(songs)
        os.startfile(os.path.join(music, songs[0]))
    elif "tell me a joke" in statement:
            joke = pyjokes.get_joke()
            speak(joke)
            print(joke)
    elif "weather" in statement:
            api_key="bf1e579c03d61f78400bcf1dd1abcf6c"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature ) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))
            else:
                speak(" City Not Found ")
    elif "screenshot" in statement:
        ss=pyautogui.screenshot()
        ss.save("C:\\`Users\smith\Pictures\Screenshots.png")
    elif "location" in statement:
        url = "https://www.google.com/maps/search/Where+am+I+?/"
        webbrowser.get().open(url)
        speak("You must be somewhere near here, as per Google maps")
    elif "movie" in statement:
        speak("please speak your movie name to search......")
        hear=takeCommand()
        movie=imdb.IMDb()
        search=movie.search_movie(hear)
        print(search)
        webbrowser.open(hear)
    elif "language" in statement:
        if True:
            speak("you can translate any of the language from english.....")
            speak("please speak the language you want to translate")
            translator= Translator(to_lang=takeCommand())
            speak("please speak  the word to translate")
            p=takeCommand()
            translation = translator.translate(p)
            print(translation)
        else:
            speak("sorry no language found")
    elif "danger" in statement or "help" in statement :
        if True:
            url = "https://www.fast2sms.com/dev/bulk"
            payload = "sender_id=FSTSMS&message=i'm hit ..help..please call me on 7004010812!!!&language=english&route=p&numbers=7004010812,"
            headers = {
            'authorization': "kmXScCs8v4BgihNu73bdHnj5zZtyexRa2Q1r6fPWqVTGY9DOwLe9LjPOfRrJYliMNcAF0w3Xxu5tdH8U",
            'Content-Type': "application/x-www-form-urlencoded",
            'Cache-Control': "no-cache",}
            response = requests.request("POST", url, data=payload, headers=headers)
            print(response.text)
            speak("your message sent successfully")
        else:
            print("sorry your message will not be sent ")
            speak("sorry your message will not be sent")
    elif "todo" in statement:
        l=[]
        speak("enter your list  to add")
        z=takeCommand().split()
        l.append(z)
        speak("the items in your list is")
        speak(l)
        print(l)
        
    elif "exit" in statement or "good bye" in statement or "ok bye" in statement or "stop" in statement: 
        speak('your personal voice assistant  is shutting down,Good bye')
        print('your personal voice assistant is shutting down,Good bye')
        break

    
