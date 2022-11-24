import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os

try:
    while True :
        r= sr.Recognizer()
        
        with sr.Microphone() as source:
            print("원하는 메뉴를 말씀하세요")
            audio = r.record(source, offset=1, duration=3)
        try:
            stt = r.recognize_google(audio, language="ko-KR")
            if "아이스" in stt:
                tts = gTTS(text= "아이스 아메리카노를 주문하시겠습니까?", lang='ko')
                tts.save("ice.mp3")
                playsound("ice.mp3")
        except sr.UnknownValueError :
            print("오디오를 이해할 수 없소.")
except KeyboardInterrupt :
    pass