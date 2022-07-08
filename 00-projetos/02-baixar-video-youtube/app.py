#BIBLIOTECA PYTUBE -> pip install pytube

from pytube import YouTube
url = input('Digite o link do video:')
youtube = YouTube(url)
print('Iniciando o Download... \n')
print('Título: '+youtube.title)
video = youtube.streams.get_highest_resolution()
video.download()
print('Download Realizado com sucesso.')

