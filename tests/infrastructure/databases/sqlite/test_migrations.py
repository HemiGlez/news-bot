import sqlite3
from src.infrastructure.databases.sqlite.migrations import apply_migrations
import pytest

@pytest.fixture
def sqlite_connection():
    conn = sqlite3.connect(":memory:")
    yield conn
    conn.close()

def test_migrations_create_news_table(sqlite_connection):
    apply_migrations(sqlite_connection)

    cursor = sqlite_connection.cursor()
    cursor.execute(
        """
            SELECT name FROM sqlite_master
            WHERE type='table' AND name='news'
        """
    )

    assert cursor.fetchone() is not None

def test_migration_is_registered(sqlite_connection):
    apply_migrations(sqlite_connection)

    cursor = sqlite_connection.cursor()
    cursor.execute("SELECT id FROM migrations")

    result = cursor.fetchone()
    assert result[0] == "0001_create_news_table"

def test_migrations_are_idempotent(sqlite_connection):
    # We apply migrations first time to apply all the migrations
    apply_migrations(sqlite_connection)

    cursor = sqlite_connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM migrations")

    count_first_time = cursor.fetchone()[0]

    assert count_first_time == 1

    # We apply the migrations a second time, this time should not migrate anything
    apply_migrations(sqlite_connection)

    cursor = sqlite_connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM migrations")

    count_second_time = cursor.fetchone()[0]

    assert count_second_time == 1
