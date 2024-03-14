# import os
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
print("Welcome to the RoboSpeaker 1.1")
while True:
    x = input("What do you want me to speak\n")
    if x == 'q':
        break
    command = x
    speaker.Speak(command)
