from pytube import YouTube

url = input(str('Digite o link do Vídeo: '))
yt = YouTube(url)

yt.streams.first().download()