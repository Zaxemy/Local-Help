from pydantic_settings import BaseSettings


class DataBaseSettings(BaseSettings):
    db_url: str = "sqlite+aiosqlite:///db.sqlite3"
    echo: bool = True

settings = DataBaseSettings()

