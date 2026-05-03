from dataclasses import dataclass
from typing import Optional
from datetime import datetime


ALLOWED_CATEGORIES = {
    "business",
    "entertainment",
    "general",
    "health",
    "science",
    "sports",
    "technology"
}


@dataclass
class TelegramPreference:
    chat_id: str
    category: str
    id: Optional[int] = None
    updated_at: Optional[datetime] = None

    def __post_init__(self):
        if self.category not in ALLOWED_CATEGORIES:
            raise ValueError(
                f"Invalid category '{self.category}'"
            )