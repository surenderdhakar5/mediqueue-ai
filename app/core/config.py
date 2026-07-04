import os
from dotenv import load_dotenv

# .env load karega
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "change_this_to_a_long_random_secret_key"
)

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60