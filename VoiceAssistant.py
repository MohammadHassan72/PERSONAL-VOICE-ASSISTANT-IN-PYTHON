import speech_recognition as sr
import pyttsx3
import pywhatkit
import webbrowser   

def recognize_speech():
    recognizer = sr.Recognizer()
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    with sr.Microphone() as source:
        print('Clearing background noises... Please wait.')
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print('Listening...')
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio, language="en-US").lower()
        print("You said:", command)
        
        if "Hi" in command:
            greet()
        elif "open youtube" in command:
            open_youtube()
        elif "play song" in command:
            play_song()
        elif "open whatsapp" in command:
            open_whatsapp()
        elif "search google" in command:
            search_google(command)
        elif "open wikipedia" in command:
            open_wikipedia(command)
        elif "open facebook" in command:
            open_facebook(command)
        elif "open gpt" in command:
            open_GPT(command)
        elif "open instagram" in command:
            open_instagram(command)
        elif "open zomato" in command:
             open_zomato()
        elif "open amazon" in command:
            open_amazon()
            
            
        else:
            speak("Sorry, I didn't understand that command.")
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
        speak("Sorry, I could not understand what you said.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        speak("There was an error processing your request.")

def greet():
    speak("Hello! What can I do for you?")

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def open_youtube():
    speak("Opening YouTube")
    webbrowser.open("https://youtube.com/")


def play_song():
    speak("Playing a song")
    pywhatkit.playonyt("random Arijit Singh song")


def open_whatsapp():
    speak("Opening WhatsApp")
    webbrowser.open("https://web.whatsapp.com/")


def search_google(command):
    query = command.replace("search google", "")
    speak(f"Opening Google {query}")
    webbrowser.open(f"https://www.google.com/search?q={query}")


def open_wikipedia(command):
    query = command.replace("open wikipedia", "")
    speak(f"Opening Wikipedia {query}")
    webbrowser.open(f"https://en.wikipedia.org/wiki/{query}")


def open_facebook(command):
    speak("Opening Facebook")
    webbrowser.open("https://facebook.com/")


def open_GPT(command):
    speak("Opening Chat-GPT")
    webbrowser.open("https://chat.openai.com/")


def open_instagram(command):
    speak("Opening Instagram")
    webbrowser.open("https://www.instagram.com/")

def open_zomato():
    speak("Opening Zomato")
    webbrowser.open("https://www.zomato.com/india")
    
def open_amazon():
    speak("Opening Amazon")
    webbrowser.open("https://www.amazon.in/")
    
    
if __name__ == "__main__":
    recognize_speech()




































































































