from fastapi import APIRouter

from services import ebay
from services import ninnin
from services import playasia


router = APIRouter(
    prefix="/api/prices",
)

price_method = {
    "ebay": ebay.search_prices,
    "ninnin": ninnin.search_prices,
    "playasia":  playasia.search_prices
}

@router.get('')
def get_prices(name: str, source: str):
    return  price_method[source](name)