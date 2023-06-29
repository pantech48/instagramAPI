from fastapi import HTTPException

from dependencies import get_instagram_photos
from main import app


@app.get("/getPhotos/{username}")
async def get_photos(username: str, max_count: int = 5):
    try:
        insta_username = "123"
        insta_password = "123"

        image_urls = get_instagram_photos(insta_username, insta_password, username, max_count)
        return {"urls": image_urls}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/postPhotos")
async def upload_photos():
    pass
