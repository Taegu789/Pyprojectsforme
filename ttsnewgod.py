from gtts import gTTS
from playsound import playsound


file_path = r"C:\Users\user\Desktop\Pyprojectsforme\autmn.txt"
with open(file_path,'rt',encoding='UTF-8')as f:
    read_file = f.read()

tts = gTTS(text=read_file, lang='ko')
tts.save(r"C:\Users\user\Desktop\Pyprojectsforme\helsslo.mp3")

playsound(r"C:\Users\user\Desktop\Pyprojectsforme\helsslo.mp3")