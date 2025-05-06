import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "${DATABASE_URL}")

    if not SQLALCHEMY_DATABASE_URI:
        raise ValueError("DATABASE_URL not set in environment variables")

    SQLALCHEMY_TRACK_MODIFICATIONS = False
