#import required modules
import os
import datetime
import pyttsx3
import speech_recognition as sr
import webbrowser


# create engine for text to speech
engine = pyttsx3.init()
engine.setProperty('rate',175)


# speak function
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


#commmand taking function
def take_command():
    listner = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = listner.listen(source)
        try:
            command = listner.recognizer_google(audio) # audio to text
            command = command.lower()
            print("You said:", command)
            return command
        except:
            return ""
    
#create run assistant function
def run_assistant():
    command = take_command()



    # in commmand it have time word
    if "time" in command:
        time=datetime.datetime.now().strftime("%I: %M %p")
        speak(f"The Cuurent Time {time}")


# date in command ,it returns  the current date
    elif "date" in command:
        date = datetime.date()
        speak(f"today date is {date}")
        # open notepad
    elif "open notepad" in command:
        speak("opening notepad")
        os.system('notepad')

    elif "open youtube" in command:
        speak("opening youtube")
        webbrowser.open("https://www.youtube.com/")


        #search for any query
    elif "hey siri" in command:
        query = command.replace("hey siri","")
        if query:
            url = "https://www.google.com/search?q={query}"
            speak(f"Lokking for {query}")
            webbrowser.open(url)
    elif "bye" in command or "stop" in command:
        speak("Okay bye bye")
        exit()
    else:
        speak("I am here to assist you,ask like open youtube,open notepad,time or date")

#main function 
if __name__ == "__main__":
    speak("hey Man whassup hi,today i am here to ssist you in open youtube,open notepad and like any query ")
    while True:
        run_assistant()