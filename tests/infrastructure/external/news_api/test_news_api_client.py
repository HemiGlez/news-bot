import pytest
from unittest.mock import patch, Mock
from src.infrastructure.external.news_api.news_api_client import NewsApiClient, NewsApiRequestError
from tests.factories.news_factory import make_news_api_response
import requests

@pytest.fixture
def mock_requests_get():
    with patch("src.infrastructure.external.news_api.news_api_client.requests.get") as mock:
        yield mock

def test_get_top_headlines_pagination_correctly(mock_requests_get):
    page_size = 2

    # Prepare the data: 3 total (Page 1: 2, Page 2: 1)
    page_1_data = make_news_api_response(n=2, total_results=3)
    page_2_data = make_news_api_response(n=1, total_results=3)
    
    # Mock for the first response
    mock_response_1 = Mock()
    mock_response_1.json.return_value = page_1_data
    mock_response_1.raise_for_status.return_value = None
    
    # Mock for the second response
    mock_response_2 = Mock()
    mock_response_2.json.return_value = page_2_data
    mock_response_2.raise_for_status.return_value = None
    
    # Assign the side_effect in order
    mock_requests_get.side_effect = [mock_response_1, mock_response_2]
    
    # Execute the client
    client = NewsApiClient(api_key="fake_key")
    news_list = client.get_top_headlines(country="es", category="general", page_size=page_size)

    # Verify that the while loop ran exactly 2 times
    assert mock_requests_get.call_count == 2

    # Verify that it collected all the articles (2 from page 1 + 1 from page 2)
    assert len(news_list) == 3
       
    # Check page 1 parameters
    calls = mock_requests_get.call_args_list
    assert calls[0].kwargs["params"]["page"] == 1
    assert calls[0].kwargs["params"]["pageSize"] == 2
    
    # Check page 2 parameters
    assert calls[1].kwargs["params"]["page"] == 2

def test_get_top_headlines_returns_empty_list_when_no_results(mock_requests_get):
    # Setup mock with 0 results
    empty_response = {"status": "ok", "totalResults": 0, "articles": []}
    
    mock_response = Mock()
    mock_response.json.return_value = empty_response
    mock_response.raise_for_status.return_value = None
    mock_requests_get.return_value = mock_response

    client = NewsApiClient(api_key="fake_key")
    news_list = client.get_top_headlines(country="us", category="general")

    assert len(news_list) == 0
    assert mock_requests_get.call_count == 1

def test_get_top_headlines_raises_error_on_connection_failure(mock_requests_get):
    # Setup: Force a connection error
    mock_requests_get.side_effect = requests.exceptions.ConnectionError("Connection failed")

    client = NewsApiClient(api_key="fake_key")

    # Assert: Check if your custom exception is raised
    with pytest.raises(NewsApiRequestError) as exc_info:
        client.get_top_headlines(country="us", category="general")
