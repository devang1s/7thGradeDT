"""
OS for tablet interface
"""
'''
Imports

Import statement:
pip install google-generativeai
pip install pyttsx3
pip install SpeechRecognition
pip install pyaudio
'''

import pyaudio # type: ignore
import google.generativeai as genai# pyright: ignore[reportMissingImports]
import pyttsx3 # pyright: ignore[reportMissingImports]
import speech_recognition as sr# pyright: ignore[reportMissingImports]
import time
import toga # pyright: ignore[reportMissingImports]
from toga.style.pack import COLUMN, ROW # pyright: ignore[reportMissingImports]

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

class RestartOS(toga.App):
    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(direction=COLUMN)

        name_label = toga.Label(
            "Your name: ",
            margin=(0, 5),
        )
        self.name_input = toga.TextInput(flex=1)

        name_box = toga.Box(direction=ROW, margin=5)
        name_box.add(name_label)
        name_box.add(self.name_input)

        button = toga.Button(
            "Say Hello!",
            on_press=self.say_hello,
            margin=5,
        )

        main_box.add(name_box)
        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def say_hello(self, widget):
        print(f"Hello, {self.name_input.value}")
        
    '''
    Listen (return audio from voice)
    '''

    def listen(CurrentState):

        # Change the state
        if CurrentState!=None:
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


def main():
    return RestartOS()
