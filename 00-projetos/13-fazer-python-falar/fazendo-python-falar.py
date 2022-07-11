#pip install playsound
#pip install gTTS
import gtts
from playsound import playsound

with open('frase.txt', 'r') as arquivo:
    for linha in arquivo:
        frase = gtts.gTTS(linha, lang='pt-br')
        #transformar texto em audio
        frase.save('frase.mp3')
        playsound('frase.mp3')