from abc import ABC, abstractmethod
from typing import List
from src.domain.news.models import News


class NewsProvider(ABC):

    @abstractmethod
    def get_top_headlines(self, country: str, category: str, page_size: int) -> List[News]:
        pass

