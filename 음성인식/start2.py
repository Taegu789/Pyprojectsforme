from gtts import gTTS
text = "안녕하세요 주문 도와드릴게요"

tts = gTTS(text = text, lang = 'ko')
tts.save(r'C:\Users\user\Downloads\helloKO.mp3')
import speech_recognition as sr
import time
import pyaudio

def speak(text):
    tts = gTTS(text = text, lang = 'ko')
    tts.save(r"C:\Users\user\Downloads\helloKO.mp3")
    time.sleep(3)
    
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
            audio = r.listen(source)
            said = " "
            
            try:
                said = r.recognize_google(audio, language = "ko-KR")
                print(said)
            
            except Exception as e:
                print("Exception:" + str(e))
                
                
    return said                    
speak("안녕하세요 주문 도와드릴게요")
get_menu = get_audio()
# 주문확인 전 문자열 전처리 함수
def nlp_menu(get_menu):
    for i in range(len(get_menu)):
        if get_menu[i] == '개':
            return get_menu[:i+1]
    return get_menu    
        
    
# 주문을 확인하는 함수    
def check_order(get_menu):
    
    speak(nlp_menu(get_menu) + ".  맞으세요?")


    check = get_audio()

    if '아니' in check:
        
        speak( "주문을 다시 말씀해주세요")

        get_menu = get_audio()
        check_order(get_menu)
        
    else:    
        speak("15000원 입니다. 카드를 꽂아주세요")

        
        

def order():
    # 기본 인사
    speak("안녕하세요 주문 도와드릴게요")
    
    #주문 받기
    get_menu = get_audio()
    
    #주문 체크
    
    check_order(get_menu)
    