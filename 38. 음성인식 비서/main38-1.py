# SpeechRecognition  = 음성을 텍스트로 변환하여 주기 위한 라이브러리.
import pyaudio
# 오디오를 입력받기 위해 쓰는 라이브러리
import wave
from playsound import playsound
# 음악파일을 파이썬에서 재생하기 위한 라이브러리
CHUNK = 1024
#녹음파일의 형식 1024?
FORMAT = pyaudio.paInt16
#녹음파일의 형식 paInt16?
CHANNELS = 1
# 녹음파일의 형식 ?
RATE = 44100
# 녹음파일의 비트샘플링?
RECORD_SECONDS = 5
# 녹음파일의 초 ?
WAVE_OUTPUT_FILENMAE = r"38. 음성인식 비서\output.wav"
# 녹음파일의 위치

p = pyaudio.PyAudio()
# p라는 객체를 pyaudio 받아오도록 해줌
stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
# p객체를 열어 위의 설정 녹음파일의 형식적용
print("음성녹음을 시작합니다.")

frames = []
# frames 라는 리스트를 해놓음
for i in range(0, int(RATE/ CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("음성 녹음을 완료")