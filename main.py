from src.infrastructure.databases.sqlite.migrations import apply_migrations
from src.infrastructure.databases.sqlite.connection import get_connection

from src.infrastructure.external.news_api.news_api_client import NewsApiClient
from src.infrastructure.databases.sqlite.news.sqlite_news_repository import SqliteNewsRepository

from src.application.news.sync_news import SyncNews

from src.infrastructure.external.telegram.telegram_notifier import TelegramNotifier
from src.config.settings import Settings

def main():
    connection = get_connection()
    settings = Settings()

    try:
        apply_migrations(connection)
        print("BotNews correctly initiated.")

        news_provider = NewsApiClient(api_key=settings.news_api_key)
        news_repository = SqliteNewsRepository(connection)

        use_case = SyncNews(news_provider, news_repository)

        try:
            use_case.execute(country="es", category="general")

        except Exception as e:
            print(f"Skipping NewsAPI: {e}")

        telegram_notifier = TelegramNotifier(
            bot_token=settings.telegram_bot_token,
            chat_id=settings.telegram_chat_id
        )

        telegram_notifier.send_message("Telegram integration working correctly")

    finally:
        connection.close()

if __name__ == "__main__":
    main()
