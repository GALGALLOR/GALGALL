import speech_recognition as sr  # recognise speech
import playsound  # to play an audio file
from gtts import gTTS  # google text to speech
import random
import datetime  # get time details
import webbrowser  # open browser
import time
import re
import mysql.connector
import os  # to remove created audio files
from PIL import Image
import pyautogui
import bs4 as bs
import urllib.request
import requests
import pandas as pd




r = sr.Recognizer()  # initialise a recogniser


# listen for audio and convert it to text:
def record_audio():
    with sr.Microphone() as source:  # microphone as source
        audio = r.listen(source)  # listen for the audio via source
        print("Done Listening")
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text

            print(voice_data)
        except :  # error: recognizer does not understand
            record_audio()
        return  voice_data

# get string and make a audio file to be played
def aspeak(audio_string):
    audio_string = str(audio_string)
    tts = gTTS(text=audio_string, lang='en')  # text to speech(voice)
    r = random.randint(1, 20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file)  # save as mp3
    playsound.playsound(audio_file)  # play the audio file
    print('ALIE' + ":", audio_string)  # print what app said
    os.remove(audio_file)  # remove audio file



aspeak('what is your name')
names = record_audio()
aspeak('welcome '+str(names))
pattern = '[a-zA-Z]'
first_letter = names[0]
other_letters = names[1:]
first_letter = first_letter.upper()
other_letters  = other_letters.lower()
names = first_letter + other_letters
if len(names)<14:
    print('welcome '+ names)
else:
    print('ERROR! Your name is too long')
    exit()

