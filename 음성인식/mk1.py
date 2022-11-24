from gtts import gTTS
from playsound import playsound
import os 

os.chdir(os.path.dirname(os.path.abspath(__file__)))
text = "아이스 아메리카노를 주문하시겠습니까?"

tts = gTTS(text=text, lang='ko')
tts.save("order.mp3")
playsound("order.mp3")