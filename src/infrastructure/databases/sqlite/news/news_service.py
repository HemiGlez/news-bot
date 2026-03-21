from src.domain.news.models import News
from src.infrastructure.databases.sqlite.mappers import dt_to_str

def insert_news(news: News, connection) -> None:
    """
    Persist a News entity in the database.

    This function receives a News object and inserts it into the `news` table.
    Fields such as `id`, `created_at`, and `is_sent` are automatically generated
    by the database.

    Args:
        news (News): The news entity to store.
        connection: Active database connection.
    """
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO news (title, url, source, description, published_at)
        VALUES (?, ?, ?, ?, ?)
    """, (
        news.title,
        news.url,
        news.source,
        news.description,
        dt_to_str(news.published_at)
    ))

    connection.commit()

