#1 setup text to speexh gtts
import os
from gtts import gTTS
def text_to_speech_old(input_text,output_filepath):
    language = 'en'
    audioobj=gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
input_text="Hello! How are you? I hope you are doing well."
#text_to_speech_old(input_text,output_filepath="gtts_testing.mp3")

#2 Use model text output to voice
import subprocess
import platform
def text_to_speech_with_gtts(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['start', output_filepath], shell=True)
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath]) 
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")
input_text="Hello! How are you? I hope you are doing well."
text_to_speech_with_gtts(input_text,output_filepath="gtts_testing_autosave.mp3")