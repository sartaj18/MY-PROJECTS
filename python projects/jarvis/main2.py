import pyttsx3
import speech_recognition as sr
import webbrowser
import musicLibrary


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
        
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musicLibrary.music[song]
        webbrowser.open(link)
        

if __name__ =="__main__" :
     
    speak("starting jarvis")
    
    while True:
        r=sr.Recognizer()
        print("recognizing....")
        try:
        
            with sr.Microphone() as source:
                print("Listening....")
                audio=r.listen(source,timeout=5,phrase_time_limit=2)
            word=r.recognize_google(audio)
            print("Heard: ",word)
            if word.lower()=="jarvis" :
               print("jarvis is activated")
               speak("yah")
               with sr.Microphone() as source:
                print("Listening....")
                audio=r.listen(source,timeout=5,phrase_time_limit=2)
               word=r.recognize_google(audio)
               print("Heard: ",word)
               processcommand(word)
            elif word.lower()=="destroy":
                break    
        except Exception as e:
                print("Error; {0}".format(e))                