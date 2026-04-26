from src.application.news.sync_news import SyncNews


class FakeProvider:
    def get_top_headlines(self, country, category, page_size):
        return ["news1", "news2"]


class FakeRepository:
    def __init__(self):
        self.saved = []

    def save(self, news):
        self.saved.append(news)


def test_sync_news_saves_articles():
    provider = FakeProvider()
    repository = FakeRepository()

    use_case = SyncNews(provider, repository)
    use_case.execute(country="es", category="general")

    assert len(repository.saved) == 2
