from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # App
    app_name: str = "FortiBank Secure Platform"
    environment: str = "development"
    debug: bool = True
    
    # Database
    database_url: str
    
    # Redis
    redis_url: str
    
    # Security
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 15
    refresh_token_expire_days: int = 7
    
    # Email
    smtp_host: str = "localhost"
    smtp_port: int = 1025
    smtp_username: str| None = None
    smtp_password: str| None = None
    
    class Config:
        env_file =".env"
        case_sensitive = False
@lru_cache
def get_settings()-> Settings:
    return Settings()