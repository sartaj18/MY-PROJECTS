import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

recognizer=sr.Recognizer()
engine=pyttsx3.init()

def speak(text):
    engine=pyttsx3.init("sapi5")
    engine.setProperty("rate",170)
    voices=engine.getProperty("voices")
    engine.setProperty("voice",voices[0].id)
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
        
    elif c.lower().startswith("play") :
        song=c.lower().split(" ")[1]
        link=musicLibrary.music[song]
        webbrowser.open(link)    
        
        
if __name__=="__main__" :
    speak("initializing jarvis")  
    while True:
        r=sr.Recognizer()
        print("recognizing....")
        try:
            with sr.Microphone() as source:
                print("Listening")
                audio=r.listen(source, timeout=5, phrase_time_limit=2)
            word = r.recognize_google(audio)
            print("HEARD",word) 
            if(word.lower()=="jarvis"):
                speak("ya")
                with sr.Microphone() as source:
                    print("jarvis is activated....")
                    audio=r.listen(source, timeout=5, phrase_time_limit=2)
                    command= r.recognize_google(audio)
                    print("HEARD",command) 
                    
                    processcommand(command)
            elif(word.lower()=="destroy"):
                break
                    
                    
        except Exception as e:
            print("Error; {0}".format(e))                