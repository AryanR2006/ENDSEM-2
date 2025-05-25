import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

# Initialize TTS Engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your personal assistant Jarvis. Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception:
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # NOTE: Replace with environment variables in production
        server.login('aryanrokade29@gmail.com', 'Aryan5959Y')
        server.sendmail('rokadenikhil2003@gmail.com', to, content)
        server.close()
        speak("Email has been sent!")
    except Exception as e:
        print(e)
        speak("Sorry, I was unable to send the email.")

def open_website(name, url):
    speak(f"Opening {name}")
    webbrowser.open(url)

if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand().lower()

        if 'search in wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception:
                speak("Couldn't fetch info from Wikipedia.")

        elif 'open youtube' in query:
            open_website("YouTube", "https://youtube.com")
        elif 'close youtube' in query:
            close_website("YouTube", "https://youtube.com")

        elif 'open whatsapp' in query:
            open_website("WhatsApp", "https://web.whatsapp.com")
        elif 'close whatsapp' in query:
            close_website("WhatsApp", "https://web.whatsapp.com")

        elif 'open google' in query:
            open_website("Google", "https://google.com")
        elif 'close whatsapp' in query:
            close_website("Google", "https://google.com")

        elif 'open instagram' in query:
            open_website("Instagram", "https://www.instagram.com")
        elif 'close whatsapp' in query:
            close_website("Instagram", "https://www.instagram.com")

        elif 'open colab' in query:
            open_website("Google Colab", "https://colab.research.google.com")
        elif 'close whatsapp' in query:
            close_website("Google Colab", "https://colab.research.google.com")


        elif 'open poki' in query:
            open_website("Poki", "https://poki.com")
        elif 'close whatsapp' in query:
            close_website("Poki", "https://poki.com")

        elif 'open wikipedia' in query or 'open wiki' in query:
            open_website("Wikipedia", "https://www.wikipedia.org")
        elif 'close whatsapp' in query:
            close_website("Wikipedia", "https://www.wikipedia.org")

        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            try:
                songs = os.listdir(music_dir)
                if songs:
                    os.startfile(os.path.join(music_dir, songs[0]))
                else:
                    speak("No songs found in the directory.")
            except Exception:
                speak("Unable to access music directory.")

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open he code' in query:
            codePath = r"C:\Users\nikhi\OneDrive\Desktop\ARYAN\projects\jarvis.py"
            try:
                os.startfile(codePath)
            except Exception:
                speak("Unable to open VS Code.")

        elif 'email to sumit' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "sumitinglepatil143@gmail.com"
                sendEmail(to, content)
            except Exception:
                speak("Something went wrong while sending the email.")

        elif 'exit' in query or 'quit' in query or 'bye' in query:
            speak("Goodbye! Have a great day.")
            break
