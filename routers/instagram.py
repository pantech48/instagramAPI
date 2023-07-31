from fastapi import HTTPException, APIRouter

from dependencies import (
    get_instagram_photos
)
from config import Config


router = APIRouter()


@router.get("/getPhotos/{username}")
async def get_photos(username: str, max_count: int = 5):
    try:
        image_urls = get_instagram_photos(Config.INSTAGRAM_USERNAME, Config.INSTAGRAM_PASSWORD, username, max_count)
        return {"urls": image_urls}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/postPhotos")
async def upload_photos():
    pass


@router.get("/")
async def root():
    return {"message": "Hello World"}
