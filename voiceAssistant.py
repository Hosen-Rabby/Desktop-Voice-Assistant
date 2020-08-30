import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
from datetime import date




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  # setting voice
engine.setProperty('voice', voices[1].id) # male/female voice


def speak(audio): # will speak by this function
  engine.say(audio)
  engine.runAndWait()


def wishme():
  hour = int(datetime.datetime.now().hour)

  if hour>=0 and hour<12:
    speak('Good Morning.')

  elif hour>=12 and hour<18:
    speak('Good Afternoon.')

  else:
    speak('Good Evening')

  speak('I am your voice assistant, how can i help you!')


def takeCommand():
  # It will take voice from micro phone, and return speech to text(string).
  r = sr.Recognizer()
  with sr.Microphone() as source:
    print('Listening...')
    r.pause_threshold = 1
    audio = r.listen(source)
  try:
    print('Recognizing...')
    query = r.recognize_google(audio, language='en-bn')
    print(f'User said: {query}\n')
  except Exception as e:
    print(e)
    print('Say that again please...')
    return 'None'
  return query


if __name__ == "__main__":
  wishme()

  # logic on executing tasks based on query
  if 1:
    query = takeCommand().lower()

    if 'wikipedia' in query:
      speak('Searching Wikipedia...')
      query = query.replace('wikipedia', '')
      results = wikipedia.summary(query, sentences=5)
      speak('According to wikipedia')
      print(results)
      speak(results)

    elif 'open' in query:
      open = query.split(' ',1)[1]
      speak(f'Opening {open}')
      webbrowser.open(f'{open}.com')

    elif 'time' in query:
      strtime = datetime.datetime.now().strftime("%H:%M:%S")
      print(strtime)
      speak(f"The time is {strtime}")

    elif 'date' in query:

      today = date.today()
      d2 = today.strftime("%B %d, %Y")
      print(d2)
      speak(f"Today is {d2}")


    else:
      results = wikipedia.summary(query, sentences=5)
      print(results)
      speak(results)


  # takeCommand()
  # speak("Who is good? Waiting for call")