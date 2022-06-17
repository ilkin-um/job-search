from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings


engine = create_engine(
    f"postgresql+psycopg2://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
