from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..repository import Chip
from ..schemas import Schemas_Chip



router = APIRouter(
    prefix="/chip",
    tags=['Chip']
)

@router.get('/', status_code=status.HTTP_200_OK, response_model=list[Schemas_Chip.Chip])
async def get_chip(db: Session = Depends(get_db)):
    return Chip.get_chip_all(db)




