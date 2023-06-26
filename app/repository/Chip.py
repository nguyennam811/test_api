from sqlalchemy.orm import Session
from ..models import Models_Chip
def get_chip_all(db: Session):
    chip = db.query(Models_Chip.Chip).all()
    return chip