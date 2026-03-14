from src.infrastructure.databases.sqlite.connection import get_connection

MIGRATIONS = [
    {
        "id": "0001_create_news_table",
        "sql": """
            CREATE TABLE IF NOT EXISTS news (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                url TEXT NOT NULL,
                source TEXT NOT NULL,
                description TEXT,
                published_at TEXT NOT NULL,
                is_sent BOOLEAN NOT NULL DEFAULT 0,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(url, source)
            )
        """
    }
]


def apply_migrations(connection):
    cursor = connection.cursor()

    # We create the migrations control table if it does not exist.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS migrations (
            id TEXT PRIMARY KEY,
            applied_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Get migrations that have already been applied.
    cursor.execute("SELECT id FROM migrations")
    applied = {row[0] for row in cursor.fetchall()}

    # Apply pending migrations.
    for migration in MIGRATIONS:
        if migration["id"] not in applied:
            print(f"Applying migration {migration['id']}...")
            cursor.execute(migration["sql"])
            cursor.execute(
                "INSERT INTO migrations (id) VALUES (?)",
                (migration["id"],)
            )

    connection.commit()
    
    print("All migrations applied.")
