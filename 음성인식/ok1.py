import speech_recognition as sr
from gtts import gTTS
import time
from playsound import playsound
import os 

def speak(text):

    tts = gTTS(text=text, lang='ko')
    filename='voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)




try:
    while True :
        r = sr.Recognizer()
        
        with sr.Microphone() as source:
            print("음성을 입력하세요.")
            audio = r.record(source, offset=1, duration=3)
        try:
            stt = r.recognize_google(audio, language='ko-KR')
            print("음성변환  : " + stt)
            if "아이스" in stt:
                speak("아이스 아메리카노를 주문하시겠습니까?")
            elif "날씨" in stt:
                print(" 추울때는 따듯한 음료를 Willy!")
                
        except sr.UnknownValueError:
            print("오디오를 이해할 수 없습니다.")
        except sr.RequestError as e:
            print(f"에러가 발생하였습니다. 에러원인 : {e}")
            
except KeyboardInterrupt:
    pass
