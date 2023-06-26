from sqlalchemy.orm import Session, load_only
from ..schemas import Schemas_Users, Schemas
from ..models import Models_Users
from fastapi import HTTPException, status
from sqlalchemy import or_, func, text, and_
import math
def get_user_all(
        db: Session,
        columns: str,
        filters: str,
        search: str,
        sort: str,
        page: int,
        limit: int
):
    # users = db.query(Models_Users.User).all()
    # return users
    query = db.query(Models_Users.User)

    if columns is not None and columns != 'null':
        new_columns = columns.split('--')
        column_list = []
        for data in new_columns:
            column_list.append(getattr(Models_Users.User, data))

        query = query.options(load_only(*column_list))

    if filters is not None and filters != 'null':
        criteria = dict(x.split("*") for x in filters.split('--'))
        criteria_list = []
        for attr, value in criteria.items():
            _attr = getattr(Models_Users.User, attr)
            # filters = f"%{value}%"
            # criteria_list.append(_attr.like(filters))
            criteria_list.append(_attr == value)

        query = query.filter(and_(*criteria_list))

    if search is not None and search != 'null':
        query = query.filter(
            (
                Models_Users.User.name.ilike(f"%{search}%") |
                Models_Users.User.phone_number.ilike(f"%{search}%")
            )
        )

    if sort is not None and sort != 'null':
        query = query.order_by(text(','.join(sort.split('--'))))

    # count_query = select(func.count(1)).select_from(query)
    count_query = db.query(func.count()).select_from(query)

    offset = (page - 1) * limit

    # pagination
    query = query.offset(offset).limit(limit)

    # total record
    total_record = db.execute(count_query).scalar() or 0

    # total page
    total_page = math.ceil(total_record / limit)

    # result
    result = query.all()

    return Schemas.PageResponse(
        page_number=page,  # trang hiện tại
        page_size=limit,  # số mục trong trang
        total_pages=total_page,  # tổng số trang
        total_record=total_record,  # tổng số mục
        content=result
    )

    # Phân trang
    # offset = (page - 1) * limit
    # search_results = search_query.offset(offset).limit(limit).all()
    # return search_results

def create_user(request: Schemas_Users.User, db: Session):
    # hashedPassword = pwd_context.hash(request.password)
    # request.password = Hash.brypt(request.password)
    new_user = Models_Users.User(**request.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def delete_user(sub: str, db: Session):
    user = db.query(Models_Users.User).filter(Models_Users.User.sub == sub)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'user with id {sub} not found')
    user.delete(synchronize_session=False)
    db.commit()
    return user

def update_user(sub: str, request: Schemas_Users.User, db: Session):
    user = db.query(Models_Users.User).filter(Models_Users.User.sub == sub)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'not found {sub}')
    user.update(request.dict(), synchronize_session=False)
    db.commit()
    return 'user'

def get_user_by_id(sub:str, db: Session):
    user = db.query(Models_Users.User).filter(Models_Users.User.sub == sub).first()
    if not user:
        raise HTTPException(status_code=404, detail=f'not found {sub}')
    return user