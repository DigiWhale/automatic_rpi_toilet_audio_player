from youtube_dl import YoutubeDL

link = "https://www.youtube.com/watch?v=J3Gy2Mikr1s"
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '/home/pi/latest.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
audio_downloader = YoutubeDL(ydl_opts)

audio_downloader.download([link])