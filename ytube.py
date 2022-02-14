from __future__ import unicode_literals
import youtube_dl as cuneyt_tanrisever
tekurlmiz="https://www.youtube.com/watch?v=bzLYh6uxfgc"
oynatmalistemiz = "https://www.youtube.com/watch?v=UtA1Xiu455E&list=PLkX3iD3uN0HZzGoRWnyVu1-oMuTP-Jbc8"

#Tek bir videoyu Mp4 video indirme ayarı
#ayarlar = {'format':'mp4'}
# Oynatma listesini mp4 olarak indime ayarı 
ayarlar = {
    '--playlist-start':'1',
    '--playlist-end':'5',
    'format':'mp4'
}
#Tek videoyu mp3 olarak indirme ayarı 
"""ayarlar = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
}
"""
#Oynatma lstesini Mp3 olarak indirme ayarı
"""ayarlar = {
    '--playlist-start':'3',
    '--playlist-end':'5',
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
}"""
with cuneyt_tanrisever.YoutubeDL(ayarlar) as indir:
    indir.download([oynatmalistemiz])