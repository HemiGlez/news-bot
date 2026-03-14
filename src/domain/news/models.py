from dataclasses import dataclass
from typing import Optional
from datetime import datetime
import validators

class InvalidNewsURL(ValueError):
    """Raised when a News instance has an invalid URL"""
    pass

# Dataclass that represents the complete news in the database
@dataclass
class News:
    title: str
    url: str
    source: str
    published_at: datetime
    description: Optional[str] = None
    id: Optional[int] = None
    is_sent: bool = False
    created_at: Optional[datetime] = None

    def __post_init__(self):
        # Validate the URL format
        if not validators.url(self.url):
            raise InvalidNewsURL(f"Invalid URL format: '{self.url}'")

