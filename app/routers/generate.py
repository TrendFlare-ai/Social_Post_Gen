from fastapi import APIRouter, HTTPException
from app.services.image_generator import generate_image

router = APIRouter()

@router.get("/generate-image/")
async def generate_image_endpoint(prompt: str):
    try:
        image_path = generate_image(prompt)
        return {"image_path": image_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
