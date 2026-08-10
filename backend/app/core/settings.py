import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    KEY = os.getenv("GEMINI_API_KEY")
    MODEL = os.getenv("GEMINI_MODEL")

settings = Settings()