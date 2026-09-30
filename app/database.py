from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from app.config import settings

'''
Fichier de configuration pour la connexion à la base de données Oracle.
Ce fichier utilise SQLAlchemy pour créer un moteur de base de données et une session locale.
'''

engine = create_engine(settings.DATABASE_URL, echo=False)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


class Base(DeclarativeBase):
    pass


def get_db():
    """Dépendance FastAPI : ouvre une session par requête et la ferme après."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
