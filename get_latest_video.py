from pyyoutube import Api
import os
from dotenv import load_dotenv

load_dotenv()

api = Api(api_key=os.getenv("YOUTUBE_API_KEY"))

print(api)