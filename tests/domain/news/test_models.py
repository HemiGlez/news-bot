from datetime import datetime
from src.domain.news.models import News, InvalidNewsURL
import pytest

def test_news_creation_happy_path():
    news = News(
        title="Test",
        url="https://example.com",
        source="TestSource",
        published_at=datetime(2026, 3, 12, 15, 30),
        created_at=datetime(2026, 3, 12, 10, 0, 0)
    )
    assert news.title == "Test"
    assert news.is_sent is False
    assert news.id is None
    assert news.created_at.year == 2026
    assert news.created_at.hour == 10
    assert news.published_at.year == 2026
    assert news.published_at.month == 3
    assert news.published_at.day == 12
    assert news.published_at.hour == 15
    assert news.published_at.minute == 30

def test_news_valid_url():
    news = News(
        title="Noticia válida",
        url="https://www.example.com",
        source="Fuente Ejemplo",
        published_at=datetime.now()
    )
    assert news.url == "https://www.example.com"

def test_news_invalid_url():
    with pytest.raises(InvalidNewsURL) as exc_info:
        News(
            title="Noticia inválida",
            url="nota_invalida",
            source="Fuente Ejemplo",
            published_at=datetime.now()
        )
    assert "Invalid URL format" in str(exc_info.value)
