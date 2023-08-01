import os


class Config:
    # instagram settings
    INSTAGRAM_URL = "https://www.instagram.com/"

    INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME", "default_username")
    INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD", "default_password")
