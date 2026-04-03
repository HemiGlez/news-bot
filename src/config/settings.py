from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    def __init__(self):
        self.news_api_key = os.getenv("NEWS_API_KEY")

        if not self.news_api_key:
            raise ValueError("NEWS_API_KEY is not set")
