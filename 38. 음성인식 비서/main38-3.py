import speech_recognition as sr

try:
    while True :
        r = sr.Recognizer()
        
        with sr.Microphone() as source:
            print("음성을 입력하세요.")
            audio = r.record(source, offset=1, duration=3)
        try:
            stt = r.recognize_google(audio, language='ko-KR')
            print("음성변환  : " + stt)
            if "안녕" in stt:
                print(" 답변 : 네 안녕하세요.. Willy")
            elif "날씨" in stt:
                print(" 답변 : 그렇죠? 정말 날씨가 좋아요 Willy!")
                
        except sr.UnknownValueError:
            print("오디오를 이해할 수 없습니다.")
        except sr.RequestError as e:
            print(f"에러가 발생하였습니다. 에러원인 : {e}")
            
except KeyboardInterrupt:
    pass
