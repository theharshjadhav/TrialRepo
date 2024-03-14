import speech_recognition as sr
import win32com.client
# link = https://www.lfd.uci.edu/~gohlke/pythonlibs/
# The above link contains the unofficial Python Binaries which can be used to download the required packages if not able to install automatically

speaker = win32com.client.Dispatch("SAPI.SpVoice")
# while 1:
#     print("Enter the text for output")
#     s = input()
#     speaker.Speak(s)

def say(text):
    speaker.Speak(text)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening Sir...")
        r.pause_threshold = 1
        audio = r.listen(source)



if __name__ == '__main__':
    print("I am here")
    say("I am jarvis AI")
    print("Listening...")
    text = takeCommand()
    say(text)
