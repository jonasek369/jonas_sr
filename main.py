import speech_recognition as sr
from time import ctime
import time
import webbrowser
import os
import playsound
import random
from gtts import gTTS


r = sr.Recognizer()


def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            jonas_speak(ask)
        audio = r.listen(source)
        voice_data = ""
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            jonas_speak("sorry, I did not get that")
        except sr.RequestError:
            jonas_speak("something wen wrong")
        return voice_data

def jonas_speak(audio_string):
    tts = gTTS(text=audio_string, lang="en")
    r = random.randint(1, 1000000)
    audio_file ="audio-" + str(r) + ".mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)
    os.remove(audio_file)

def respond(voice_data):
    if "what is your name" in voice_data:
        jonas_speak("my name is jonas")
    if "what time is it" or "time" or "what time" in voice_data:
        jonas_speak(ctime())
    if "search" or "search for" in voice_data:
        search = record_audio("what do you want to search for?")
        url = "https://google.com/search?q=" + search
        webbrowser.get().open(url)
        jonas_speak("here is what i found for " + search)
    if "find location" or "location" in voice_data:
        location = record_audio("what is the location ?")
        url = "https://google.nl/maps/place/" + location + "/&amp;"
        webbrowser.get().open(url)
        jonas_speak("here is the location of " + location)
    if "exit" in voice_data:
        jonas_speak("exiting now")
        exit()
    if "turn off " in voice_data:
        jonas_speak("are you sure")
    if "weather" or "what is the weather" in voice_data:
        city = record_audio("what is the city")
        url = "https://www.in-pocasi.cz/predpoved-pocasi/?hledat=" + city
        webbrowser.get().open(url)
        jonas_speak("here is the weather for " + city)
    if "how much is one plus one" in voice_data:
        jonas_speak("its two")




time.sleep(1)
jonas_speak("how can i help you ?")
while 1:
    voice_data = record_audio()
    respond(voice_data)
