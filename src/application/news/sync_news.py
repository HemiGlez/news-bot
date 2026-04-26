class SyncNews:

    def __init__(self, news_provider, news_repository):
        self.news_provider = news_provider
        self.news_repository = news_repository

    def execute(self, country: str, category: str, page_size: int = 100):
        articles = self.news_provider.get_top_headlines(country, category, page_size)

        for news in articles:
            self.news_repository.save(news)
