from fastapi import APIRouter, File
from services.gemini import process_image_with_gemini
from services.firestore import get_nendoroid_by_id


router = APIRouter(
    prefix="/api/photo",
)

@router.post('/process')
async def process_photo(content_type: str, image: bytes = File()):
    nendoroids_found =  process_image_with_gemini(image, content_type)
    all_nendoroids = []

    for res in nendoroids_found:

        nendoroid_object = {}

        if not res.get('id'):
            return {"error": "Failed to process image"}
        
        nendoroid_doc = get_nendoroid_by_id(res.get('id'))

        if not nendoroid_doc:
            all_nendoroids.append(res)
        else:
            all_nendoroids.append(nendoroid_doc)
        
    return all_nendoroids