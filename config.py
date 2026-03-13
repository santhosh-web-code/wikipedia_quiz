"""
Configuration management for the application.
Loads environment variables and provides application settings.
"""

from pydantic_settings import BaseSettings
from functools import lru_cache
from typing import Optional


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # Application
    app_name: str = "AI Wiki Quiz Generator"
    debug: bool = True
    api_prefix: str = "/api/v1"
    
    # Database
    database_url: str
    
    # LLM Configuration
    google_api_key: str
    
    # Scraping Settings
    request_timeout: int = 30
    max_content_length: int = 100000  # Maximum characters to process
    
    # Quiz Settings
    min_questions: int = 5
    max_questions: int = 10
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


@lru_cache()
def get_settings() -> Settings:
    """
    Get cached settings instance.
    Uses lru_cache to avoid reading .env file on every request.
    """
    return Settings()


settings = get_settings()