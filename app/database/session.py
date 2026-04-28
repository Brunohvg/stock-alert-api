from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# engine: O motor que fala com o driver do banco (Postgres/SQLite)
engine = create_engine(settings.DATABASE_URL)

# SessionLocal: A fábrica que gera sessões para cada request
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependência para ser injetada nos routers
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
