from src.infrastructure.databases.sqlite.migrations import apply_migrations
from src.infrastructure.databases.sqlite.connection import get_connection

from src.infrastructure.external.news_api.news_api_client import NewsApiClient
from src.infrastructure.databases.sqlite.news.sqlite_news_repository import SqliteNewsRepository

from src.application.news.sync_news import SyncNews
from src.config.settings import NEWS_API_KEY


def main():
    connection = get_connection()

    try:
        apply_migrations(connection)
        print("BotNews correctly initiated.")

        news_provider = NewsApiClient(api_key=NEWS_API_KEY)
        news_repository = SqliteNewsRepository(connection)

        use_case = SyncNews(news_provider, news_repository)
        use_case.execute(country="es", category="general")
          
    finally:
        connection.close()

if __name__ == "__main__":
    main()
