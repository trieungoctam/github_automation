import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Application settings
    APP_NAME: str = "GitHub Classroom Assistant"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False

    # GitHub settings
    GITHUB_TOKEN: str
    GITHUB_ORG: str

    # Database settings
    DATABASE_URL: str

    # API settings
    API_PREFIX: str = "/api/v1"
    DOCS_URL: str = "/docs"
    OPENAPI_URL: str = "/openapi.json"

    # CORS settings
    CORS_ORIGINS: list = ["*"]
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: list = ["*"]
    CORS_ALLOW_HEADERS: list = ["*"]

    # Email settings
    EMAIL_HOST: str
    EMAIL_PORT: int
    EMAIL_USERNAME: str
    EMAIL_PASSWORD: str

    # Slack settings
    SLACK_TOKEN: str

    # Canvas settings
    CANVAS_URL: str
    CANVAS_TOKEN: str

    class Config:
        env_file = ".env"
        case_sensitive = True

def get_settings():
    env = os.getenv("ENV", "development")
    if env == "production":
        return ProductionSettings()
    return DevelopmentSettings()

class DevelopmentSettings(Settings):
    DEBUG: bool = True

class ProductionSettings(Settings):
    # Add any production-specific settings here
    pass

settings = get_settings()