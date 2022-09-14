from pyyoutube import Api
import os
from dotenv import load_dotenv
from youtube_dl import YoutubeDL

load_dotenv()
link = "https://www.youtube.com/watch?v="
api = Api(api_key=os.getenv("YOUTUBE_API_KEY"))

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '/home/pi/latest.mp3',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

audio_downloader = YoutubeDL(ydl_opts)

def get_videos(channel_id):
    channel_info = api.get_channel_info(for_username=channel_id)

    playlist_id = channel_info.items[0].contentDetails.relatedPlaylists.uploads

    uploads_playlist_items = api.get_playlist_items(
        playlist_id=playlist_id, count=10, limit=6
    )

    videos = []
    for item in uploads_playlist_items.items:
        video_id = item.contentDetails.videoId
        video = api.get_video_by_id(video_id=video_id)
        videos.extend(video.items)
    return videos


def processor():
    channel_id = "CNN"
    videos = get_videos(channel_id)
    # print(videos[0].snippet.publishedAt, videos[0].snippet.title, videos[0].id)
    audio_downloader.download([link + videos[0].id])

if __name__ == "__main__":
    processor()