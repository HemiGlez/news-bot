from abc import ABC, abstractmethod
from typing import List
from src.domain.news.models import News


class NewsRepository(ABC):

    @abstractmethod
    def save(self, news: News) -> None:
        pass

    @abstractmethod
    def get_latest(self, limit: int) -> List[News]:
        pass
