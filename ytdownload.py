from os import link
from pytube import YouTube, streams
from pytube.cli import on_progress

link = input('Cole o link aqui: ')

yt = YouTube(link, on_progress_callback = on_progress)

print('Título = ', yt.title)

print('Baixando...')

ys = yt.streams.get_highest_resolution()
ys.download()
