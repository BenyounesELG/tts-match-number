from gtts import gTTS
import time

for i in range(1,65):
    text = f'match {i}'
    result = gTTS(text=text, lang="en-uk", tld='com.au')
    result.save(f"audio_files/m{i}.mp3")