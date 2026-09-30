from pydantic_settings import BaseSettings, SettingsConfigDict

'''
Fichier de configuration pour l'application FastAPI et la connexion à la base de données Oracle.'''

class Settings(BaseSettings):
    '''
    Classe de configuration pour l'application FastAPI et la connexion à la base de données Oracle.
    Les variables d'environnement sont chargées à partir du fichier .env.
    '''

    ORACLE_USER: str
    ORACLE_PASSWORD: str
    ORACLE_HOST: str = "localhost"
    ORACLE_PORT: int = 1521
    ORACLE_SERVICE: str = "FREEPDB1"
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    @property
    def database_url(self) -> str:
        return (
            f"oracle+oracledb://{self.ORACLE_USER}:{self.ORACLE_PASSWORD}"
            f"@{self.ORACLE_HOST}:{self.ORACLE_PORT}"
            f"/?service_name={self.ORACLE_SERVICE}"
        )

settings = Settings()