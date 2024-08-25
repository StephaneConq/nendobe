from fastapi import APIRouter
from services.firestore import get_nendoroid_by_id


router = APIRouter(
    prefix="/api/nendoroids",
)

@router.get('/{nendoroid_id}')
def get_by_id(nendoroid_id: str):
    return [get_nendoroid_by_id(nendoroid_id)]