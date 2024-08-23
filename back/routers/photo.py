from fastapi import APIRouter, File
from services.gemini import process_image_with_gemini
from services import playasia
from services import ninnin
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
        
        if nendoroid_doc:
            nendoroid_object = nendoroid_doc
            name = f"Nendoroid no {nendoroid_doc.get('id')} - {nendoroid_doc.get('name')}"
        else:
            nendoroid_object = res
            name = f"Nendoroid no {res.get('id')} - {res.get('name')}"

        nendoroid_object['prices'] = {
            'playasia': {
                'prices': playasia.search_prices(name),
                'currency': 'EUR'
            },
            'ninnin': {
                'prices': ninnin.search_prices(f"Nendoroid {res.get('name')}"),
                'currency': 'EUR'
            }
        }

        all_nendoroids.append(nendoroid_object)
        
    return all_nendoroids