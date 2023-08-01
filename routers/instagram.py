"""
This module contains the API endpoints for the Instagram application.

The endpoints are:
- /getPhotos/{username}: gets the URLs of a user's Instagram photos.
"""
from fastapi import HTTPException, APIRouter
from fastapi.params import Query
from selenium.common.exceptions import WebDriverException, TimeoutException, NoSuchElementException

from dependencies import (
    get_instagram_photos
)
from config import Config


router = APIRouter()


@router.get("/getPhotos/{username}")
async def get_photos(username: str, max_photo_count: int = Query(5, gt=0)):
    """
    Get the URLs of the user's Instagram photos.

    Args:
        username (str): Instagram username to get photos of.
        max_photo_count (int, optional): Maximum number of photo URLs to return. Defaults to 5.

    Returns:
        dict: A dictionary containing the URLs of the user's Instagram photos.
    """
    try:
        image_urls = get_instagram_photos(
            username=Config.INSTAGRAM_USERNAME,
            password=Config.INSTAGRAM_PASSWORD,
            target_username=username,
            max_count=max_photo_count
        )
        return {"urls": image_urls}
    except (WebDriverException, TimeoutException, NoSuchElementException):
        raise HTTPException(status_code=500, detail="An error occurred while retrieving Instagram photos.")
    except Exception:
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")


