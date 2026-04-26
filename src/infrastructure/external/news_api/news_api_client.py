import requests
from datetime import datetime
from src.domain.news.models import News
from typing import List, Optional
from src.domain.news.providers.news_provider import NewsProvider 
import logging
import math

logger = logging.getLogger(__name__)


POSSIBLE_CATEGORIES: tuple = (
    "business", "entertainment", "general", "health", "science", "sports", "technology",
)


class CategoryDoesNotExists(Exception):
    invalid_category: str

    def __str__(self):
        return f"Invalid category '{self.invalid_category}'. NewsAPI only accept {POSSIBLE_CATEGORIES}"


class NewsApiRequestError(Exception):
    pass


class NewsApiClient(NewsProvider):
    def __init__(self, api_key: str):
        self.api_key = api_key

    def _validate_category(self, category: str):
        if category not in POSSIBLE_CATEGORIES:
            raise CategoryDoesNotExists(invalid_category = category)


    def get_top_headlines(self, country: str, category: str, page_size: int = 100) -> List[News]:

        self._validate_category(category)

        top_headlines: List[News] = []      
        total_results: Optional[int] = None
        page = 1

        while True:
            try:
                response = requests.get(
                    "https://newsapi.org/v2/top-headlines",
                    params={
                        "country": country,
                        "category": category,
                        "page": page,
                        "pageSize": page_size,
                        "apiKey": self.api_key,
                    },
                )
                response.raise_for_status()

            except requests.exceptions.RequestException as e:
                raise NewsApiRequestError(e)

            data = response.json()

            if total_results is None:
                total_results = data.get("totalResults", 0)
                max_pages = math.ceil(total_results / page_size)

            articles = data.get("articles", [])

            for article in articles:
                news = News(
                    title=article["title"],
                    url=article["url"],
                    source=article["source"]["name"],
                    description=article.get("description"),
                    published_at=datetime.fromisoformat(
                        article["publishedAt"].replace("Z", "+00:00")
                    )
                )
                top_headlines.append(news)
             
            if page >= max_pages:
                break

            page += 1
        
        return top_headlines
