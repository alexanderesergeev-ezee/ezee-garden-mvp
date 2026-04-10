import os


def get_database_url() -> str:
    return os.getenv("DATABASE_URL", "postgresql+psycopg://app:app@db:5432/ezee_garden")
