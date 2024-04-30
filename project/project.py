import ffmpeg
from gtts import gTTS
import os
import re
import sys



def main():

    text_it = input("Italian: ")
    text_esp = input("Spanish: ")
    text_pt = input("Georgian: ")
    text_to_speech_it(text_it)
    text_to_speech_esp(text_esp)
    text_to_speech_pt(text_pt)

    print(int(count_um(text_it))+int(count_um(text_esp)))
    sys.exit(0)

def count_um(s):
    s=s.lower().strip()
    word=r"\bum\b"
    number=re.findall(word,s)
    return len(number)

# Text-to-speech example
def text_to_speech_it(text):
    language = 'it'
    tts_it = gTTS(text=text, lang=language, slow=False)
    tts_it.save("italian.mp3")
def text_to_speech_esp(text):
    language = 'es'
    tts_esp = gTTS(text=text, lang=language, slow=False)
    tts_esp.save("spanish.mp3")
def text_to_speech_pt(text):
    language = 'pt'
    tts_pt = gTTS(text=text, lang=language, slow=False)
    tts_pt.save("portuguese.mp3")
    # Playing the audio file
    # os.system("speech.mp3")

if __name__ == "__main__":
    main()