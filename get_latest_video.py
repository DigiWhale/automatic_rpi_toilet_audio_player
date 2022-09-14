from pyyoutube import Api
import os
from dotenv import load_dotenv

load_dotenv()

api = Api(api_key=os.getenv("YOUTUBE_API_KEY"))

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
    print(videos[0].snippet.publishedAt, videos[0].snippet.title)

    with open("videos.json", "w+") as f:
        for video in videos:
            f.write(video.to_json())
            f.write("\n")

if __name__ == "__main__":
    processor()