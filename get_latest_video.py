from pyyoutube import Api
import os
from dotenv import load_dotenv

load_dotenv()

api = Api(api_key=os.getenv("YOUTUBE_API_KEY"))

channel_by_id = api.get_channel_info(for_username="CNN")
print(channel_by_id.items[0].to_dict())