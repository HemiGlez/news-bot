from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    def __init__(self):
        self.news_api_key = os.getenv("NEWS_API_KEY")

        if not self.news_api_key:
            raise ValueError("NEWS_API_KEY is not set")

        # Telegram
        self.telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
        if not self.telegram_bot_token:
            raise ValueError("TELEGRAM_BOT_TOKEN is not set")

        self.telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID")
        if not self.telegram_chat_id:
            raise ValueError("TELEGRAM_CHAT_ID is not set")
