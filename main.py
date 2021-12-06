import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import requests
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishuser():
    hournow = int(datetime.datetime.now().hour)
    if hournow>=0 and hournow<12:
        speak("Good morning Master!")
    elif hournow>=12 and hournow<18:
        speak("Good Afternoon Master!")
    else:
        speak("Good evening, master!")

    speak("Welcome Master, I am Animatrix, How may I assist you today?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        userinput = f"You said: {query}"
        speak(userinput)
    
    except Exception as e:
        print("I wasn't able to understand. May you repeat Sire")
        return "None"
    return query

def timer():
    pass

def optionsavailable():
    print("Speak 'google topic' for seaching about topic in google")
    print("Speak 'open google' for opening google in browser" )
    print("Speak 'top news' for getting top 10 news")
    print("Speak 'open youtube' for opening youtube in your browser")
    print("Speak 'time now' for getting time right now")
    print("Speak 'You can sleep now' for closing the assistant")

def sleep():
    speak("Hope you have a nice day")
    sys.exit()

def timenow():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"Master, the right now is {strTime}")

def newsgetter():
    	# BBC news api
	# following query parameters are used
	# source, sortBy and apiKey
	query_params = {
	"source": "bbc-news",
	"sortBy": "top",
	"apiKey": "0ea54bfd94b7423d8654e9d59809db7d"
	}
	main_url = " https://newsapi.org/v1/articles"

	# fetching data in json format
	res = requests.get(main_url, params=query_params)
	open_bbc_page = res.json()

	# getting all articles in a string article
	article = open_bbc_page["articles"]

	# empty list which will
	# contain all trending news
	results = []
	
	for ar in article:
		results.append(ar["title"])
		
	for i in range(len(results)):
		
		# printing all trending news
		print(i + 1, results[i])

	#to read the news out loud for us
	from win32com.client import Dispatch
	speak = Dispatch("SAPI.Spvoice")
	speak.Speak(results)

if __name__ == "__main__":
    wishuser()
    optionsavailable()

    while True:
        query = takeCommand().lower()

        if 'google' in query:
            webbrowser.open(f"https://www.google.com/search?q={query}")
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'set timer' in query:
            timer()
        
        elif 'top news' in query:
            newsgetter()

        elif 'time now' in query:
            timenow()

        elif 'you can sleep now':
            sleep()
        
