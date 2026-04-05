from datetime import datetime, timedelta
import itertools

_counter = itertools.count(1)


def make_article(
    title=None,
    url=None,
    source_id=None,
    source_name=None,
    author="Test Author",
    description="Test description",
    url_to_image="https://example.com/image.jpg",
    content="Test content...",
    published_at=None
):
    i = next(_counter)

    return {
        "source": {
            "id": source_id,
            "name": source_name or f"Source {i}"
        },
        "author": author,
        "title": title or f"Test title {i}",
        "description": description,
        "url": url or f"https://example{i}.com",
        "urlToImage": url_to_image,
        "publishedAt": published_at or (
            datetime(2026, 4, 2, 10, 0, 0) + timedelta(minutes=i)
        ).isoformat() + "Z",
        "content": content
    }
    

# Creates a list of individual fake articles.
def make_articles(n):
    return [make_article() for _ in range(n)]


# Wraps that list into a mock API response like the real NewsAPI would return.
def make_news_api_response(articles=None, n=1, total_results=None):
    if articles is None:
        articles = make_articles(n)
    return {
        "status": "ok",
        "totalResults": total_results if total_results is not None else len(articles),
        "articles": articles
    }
