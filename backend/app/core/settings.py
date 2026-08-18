import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    KEY = os.getenv("API_KEY")
    MODEL = os.getenv("MODEL")

settings = Settings()