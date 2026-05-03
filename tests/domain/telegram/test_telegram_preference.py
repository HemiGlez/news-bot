from src.domain.telegram.telegram_preference import TelegramPreference
import pytest

def test_should_create_valid_telegram_preference():
    pref = TelegramPreference(
        chat_id="12345",
        category="technology"
    )

    assert pref.chat_id == "12345"
    assert pref.category == "technology"

def test_should_raise_error_for_invalid_category():
    with pytest.raises(ValueError):
        TelegramPreference(
            chat_id="12345",
            category="crypto"
        )
