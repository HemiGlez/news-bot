from src.infrastructure.databases.sqlite.migrations import apply_migrations
from src.infrastructure.databases.sqlite.connection import get_connection

def main():
    connection = get_connection()

    apply_migrations(connection)

    print("BotNews correctly initiated.")

if __name__ == "__main__":
    main()
