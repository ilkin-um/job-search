from decouple import config


class Settings:

    PROJECT_NAME: str = "Job Search"
    PROJECT_VERSION: str = "0.1.0"
    DB_NAME: str = config("DB_NAME")
    DB_USER: str = config("DB_USER")
    DB_HOST: str = config("DB_HOST")
    DB_PORT: str = config("DB_PORT")
    DB_PASSWORD: str = config("DB_PASSWORD")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    SECRET_KEY: str = config("SECRET_KEY")
    ALGORITHM: str = "HS256"


settings = Settings()
