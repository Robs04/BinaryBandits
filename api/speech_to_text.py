# Used libraries: SpeechRecognition 3.14.1
# brew install portaudio
# pip install SpeechRecognition
# pip install pyaudio
# pip install pyttsx3
# Documentation: https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rstpio
import speech_recognition as sr
import pyttsx3
import keyword_extraction
import parser
# Each paragraph of spoken text gets written on a new line in the output.txt file
# The idea is to extract the text from the output file line by line. 
# Whenever a line is written the pointer wo which line is being fetched is incremented.

r = sr.Recognizer()

def record_text(socket):
    # Loop in case of error
    while(1):
        try:
            # Use microphone as source input
            with sr.Microphone() as source2:
                # Prepare recognizer to get input
                r.adjust_for_ambient_noise(source2, duration=0.2)

                # Listen for the user input
                audio2 = r.listen(source2)

                # Using google to recognize audio 
                MyText = r.recognize_google(audio2)

                keyword_extraction.process_text(MyText, socket)

        except sr.RequestError as e:
            print("Could not request result: {0}".format(e) )
        
        except sr.UnknownValueError:
            print("Gibberisch detected")

    return


def execute_listen(socket):
    while(1):
        text = record_text(socket)

