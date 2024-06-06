from starlette.config import Config
from starlette.datastructures import Secret

config = Config(".env")

APP_VERSION: str = config("APP_VERSION", cast=str)
APP_NAME: str = config("APP_NAME", cast=str)
API_PREFIX: str = config("APP_API_PREFIX", cast=str)


API_KEY: Secret = config("API_KEY", cast=Secret)
IS_DEBUG: bool = config("IS_DEBUG", cast=bool, default=False)


DEFAULT_MODEL_PATH: str = config("DEFAULT_MODEL_PATH", cast=str)
