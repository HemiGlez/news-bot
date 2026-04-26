import sqlite3
import pytest

from src.infrastructure.databases.sqlite.news.sqlite_news_repository import SqliteNewsRepository
from src.domain.news.models import News
from src.infrastructure.databases.sqlite.migrations import apply_migrations
from datetime import datetime


@pytest.fixture
def sqlite_connection():
    conn = sqlite3.connect(":memory:")
    apply_migrations(conn)
    yield conn
    conn.close()


def test_save_persists_news(sqlite_connection):
    """
    Test that insert_news correctly persists a News record in the database.
    """
    repository = SqliteNewsRepository(sqlite_connection)

    news = News(
        title="Test news",
        url="https://example.com",
        source="TestSource",
        published_at=datetime(2026, 3, 12)
    )

    repository.save(news)

    cursor = sqlite_connection.cursor()
    cursor.execute("SELECT title, url, source FROM news")

    result = cursor.fetchone()

    assert result[0] == "Test news"
    assert result[1] == "https://example.com"
    assert result[2] == "TestSource"
