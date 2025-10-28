'''
Imports

Import statement:
pip install google-generativeai
pip install pyttsx3
pip install SpeechRecognition
pip install pyaudio
'''

from tkinter import *
import google.generativeai as genai
import pyttsx3
import speech_recognition as sr
import pyaudio
import time

'''
Initialisation
'''

genai.configure(api_key="AIzaSyDaXGMRTPQzywNwP91TfaeqSf6hMfjn0i4")
engine = pyttsx3.init("sapi5")
recognizer = sr.Recognizer()
model = genai.GenerativeModel(model_name='gemini-2.5-flash')
chat_history = []
chat = model.start_chat(history=chat_history)
ChatHistoryFile = open(r"C:\Users\devan\OneDrive\Documents\School\Homeroom\2025-2026 7th grade\Design Thinking\Prototype application\chat_history.txt", "a+", encoding='utf-8')
root = Tk()

'''
Retrieve chat history
'''

""" def chat_history_retrieve(txtFile, ChatHistoryVar):

    lines = txtFile.readlines()

    print(lines)
    
    onetwo = 0

    for line in lines:

        role = ""
        content = ""

        if onetwo==1:
            onetwo=2
            role=line
        else:
            onetwo=1
            content=line
            ChatHistoryVar.append({"role": role, "content": content})
            print(ChatHistoryVar)
            

    # for line in txtFile:

    #     ChatHistoryVar.append(line.strip())
    #     print(ChatHistoryVar)
 """
'''
Standby (Wait for command)
'''

def standby(CurrentState):

    
    # Initialise the state
    
    CurrentState = "Standby"

    # Wait for statement "Hey AI"
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Standby")
        audio = recognizer.listen(source)
        if "Hey AI" in recognizer.recognize_google(audio):
            CurrentState = 'Listening'

'''
Listen (return audio from voice)
'''

def listen(CurrentState):

    # Change the state
    CurrentState = "Standby"

    # Input
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening:")
        audio = recognizer.listen(source)
    
    return audio
        


'''
Process the speech (return text from speech)
'''

def process_speech(audio):
    
    # Convert the audio to text
    try:
        # Process the input
        prompt = recognizer.recognize_google(audio)
        return prompt

        # Errors
    except sr.UnknownValueError:
        print(end="")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")

'''
Generate the AI response
'''

def generate_response(prompt):

    # Add prompt to chat history
    # .txt addition to be added...
        
    # Generate and add response to history
    try:
        response = chat.send_message(prompt)
    except:
        print()
    
    # Refer to line 72...
    try:
        return response.text
    except:
        print(end='')

'''
Say the given text
'''

def speak(sentence):
    engine.say(sentence)
    engine.runAndWait()
    time.sleep(1.5)

'''
Append the given string to the chat history as a prompt/response
'''

# def Update_ChatHistory(ChatHistoryList, txtFile):


def initialise_main_window(WindowName,StateVar):
    
    WindowName.title("AI powered voice assistant: APVA")
    WindowName.geometry('350x200')

    global APVA_Status
    APVA_Status = Label(root, text = "Standby")
    APVA_Status.grid()

    global Awaken
    Awaken = Button(root, text = "Click me", command=state_change(StateVar))
    Awaken.grid(column=1, row=0)

    WindowName.mainloop()

def state_change(StateVar):
    if StateVar=="Standby":
        StateVar="Listening"
        APVA_Status.configure(text = "Listening")
    else:
        StateVar="Standby"
        APVA_Status.configure(text = "Standby")