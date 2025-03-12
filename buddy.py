import speech_recognition as sr 
import pyttsx3 
import webbrowser  
import re
import google.generativeai as genai
from apikey import API_KEY

# Text Cleaning Function
def clean_text(data):
    cleaned_data = re.sub(r"\n- ", " ", data)
    cleaned_data = re.sub(r"\n\n", " ", cleaned_data)
    cleaned_data = re.sub(r"\n", " ", cleaned_data)
    cleaned_data = re.sub(r"\*", "", cleaned_data)
    return cleaned_data

# Gemini AI Response Function
def response(question):
    
    genai.configure(api_key=API_KEY)
    
    model = genai.GenerativeModel("gemini-1.5-pro-latest") 
    try:
        response = model.generate_content(question)
        data = response.text
        cleaned_data = clean_text(data)
        return cleaned_data 
    except Exception as e:
        return f"Error: {e}"

# Initialize Speech Engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Speak Function
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Speech Recognition Function
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said: {} \n".format(query))
        return query
    except Exception:
        print("Say that again please...")
        return "None"

# Main Loop
if __name__ == '__main__':
    print("Hello! How can I help you?")
    speak("Hello! How can I help you?")
    
    while True:
        query = takeCommand()

        if query == "none":
            continue  # Ignore unrecognized input
        
        if "open youtube" in query:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube")
        elif "open google" in query:
            webbrowser.open("https://www.google.com")
            speak("Opening Google")
        elif "bye" in query:
            speak("Goodbye! Have a nice day.")
            break  # Exit loop properly
        else:
            reply = response(query) 
            print(reply)
            speak(reply)