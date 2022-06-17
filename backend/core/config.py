from decouple import config


class Settings:

    PROJECT_NAME: str = "Job Search"
    PROJECT_VERSION: str = "0.1.0"
    DB_NAME = config("DB_NAME")
    DB_USER = config("DB_USER")
    DB_HOST = config("DB_HOST")
    DB_PORT = config("DB_PORT")
    DB_PASSWORD = config("DB_PASSWORD")


settings = Settings()
