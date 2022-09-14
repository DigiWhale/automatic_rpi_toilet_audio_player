from pyyoutube import Api
import os
from dotenv import load_dotenv

load_dotenv()

api = Api(api_key=os.getenv("YOUTUBE_API_KEY"))

channel_by_id = api.get_channel_info(channel_id="UC_x5XG1OV2P6uZZ5FSM9Ttw")
print(channel_by_id.items)