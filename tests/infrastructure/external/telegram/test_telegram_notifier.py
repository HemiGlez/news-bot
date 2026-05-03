import pytest
from unittest.mock import patch, MagicMock
from src.infrastructure.external.telegram.telegram_notifier import TelegramNotifier


class TestTelegramNotifier:

    def test_send_message_success(self):
        with patch("src.infrastructure.external.telegram.telegram_notifier.requests.post") as mock_post:
            mock_response = MagicMock()
            mock_response.ok = True
            mock_post.return_value = mock_response

            notifier = TelegramNotifier("token", "chat_id")
            notifier.send_message("hello")

            mock_post.assert_called_once_with(
                "https://api.telegram.org/bottoken/sendMessage",
                data={
                    "chat_id": "chat_id",
                    "text": "hello",
                    "parse_mode": "HTML"
                }
            )
    
    def test_send_message_failure(self):
        with patch("src.infrastructure.external.telegram.telegram_notifier.requests.post") as mock_post:
            mock_response = MagicMock()
            mock_response.ok = False
            mock_response.text = "error"
            mock_post.return_value = mock_response

            notifier = TelegramNotifier("token", "chat_id")

            with pytest.raises(Exception) as exc:
                notifier.send_message("hello")

            assert "Telegram error" in str(exc.value)
