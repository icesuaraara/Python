from gtts import gTTS
import os

def Sound():
    text = ""
    text = str(input("ใส่ข้อความเสียง :"))
    print("Sound On")
    
    tts = gTTS(text,lang='th')
    tts.save("Output.mp3")
    os.system("start output.mp3")
Sound()
    