from gtts import gTTS

text= " Dojyo! Hi! Bonjour!"

tts = gTTS(text=text, lang='ko')
tts.save(r"C:\Users\user\Desktop\Pyprojectsforme\hi.mp3")
