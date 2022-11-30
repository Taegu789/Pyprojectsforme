import speech_recognition as sr
from gtts import gTTS
import time
from playsound import playsound
import os 

def speak(text):

    tts = gTTS(text=text, lang='ko')
    filename='voice.mp3'
    tts.save(filename)
    playsound(filename)


ice = ["아이스","아이스아메리카노","아아주세요","아이스아","이스아메"]
hot = ["뜨거운","따뜻한","핫","뜨거운 아메리카노","따신거","뜨순거","따뜻한 아메리카노","핫 커피"]
try:
    while True :          
        r = sr.Recognizer()
        
        with sr.Microphone() as source:
            print("음성을 입력하세요.")
            audio = r.record(source, offset=1, duration=2)
        try:
            stt = r.recognize_google_cloud(audio, language='ko-KR',single_utterance=True)
            print("음성변환  : " + stt)
            if stt in ice:
                speak("아이스 아메리카노를 주문하시겠습니까?")
            elif "날씨" in stt:
                speak("오늘 날씨가 좋아요! 아이스 아메리카노를 드세요.")
            elif stt in hot:
                speak("뜨거운 아메리카노를 주문하시겠습니까?")
                
        except sr.UnknownValueError:
            print("오디오를 이해할 수 없습니다.")
        except sr.RequestError as e:
            print(f"에러가 발생하였습니다. 에러원인 : {e}")
            
except KeyboardInterrupt:
    pass
  