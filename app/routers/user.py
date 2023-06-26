from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.orm import Session
from ..schemas import Schemas_Users, Schemas
from ..database import get_db
from ..repository import user

# from fastapi_pagination import Page, paginate


router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

# @router.get('/', status_code=status.HTTP_200_OK, response_model=Page[Schemas_Users.ShowUser])
# async def get_user(db: Session = Depends(get_db)):
#     return paginate(user.get_user_all(db))

@router.get('/', status_code=status.HTTP_200_OK, response_model=Schemas.ResponseSchema)
async def get_user(
        db: Session = Depends(get_db),
        columns: str = Query(None, min_length=1, max_length=100),
        filters: str = Query(None, min_length=1, max_length=100),
        search: str = Query(None, min_length=1, max_length=100),
        sort: str = Query(None, min_length=1, max_length=100),
        page: int = Query(1, ge=1),
        limit: int = Query(5, ge=1, le=100)
):
    result = user.get_user_all(db,columns, filters, search, sort, page, limit)
    return Schemas.ResponseSchema(result=result)

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_user(request: Schemas_Users.User, db: Session = Depends(get_db)):
    return user.create_user(request, db)

@router.delete('/{sub}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(sub: str, db: Session = Depends(get_db)):
    return user.delete_user(sub, db)

@router.put('/{sub}', status_code=status.HTTP_202_ACCEPTED)
async def update_user(sub: str, request: Schemas_Users.User, db: Session = Depends(get_db)):
    return user.update_user(sub, request, db)

@router.get('/{sub}',status_code=status.HTTP_200_OK)
async def get_user_by_id(sub:str, db: Session = Depends(get_db)):
    return user.get_user_by_id(sub, db)