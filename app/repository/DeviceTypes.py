from sqlalchemy.orm import Session, load_only
from ..models import Models_DeviceTypes
from ..schemas import Schemas
import math
from sqlalchemy import func, or_, text


# def get_device_types_all(db: Session):
#     device_types = db.query(Models_DeviceTypes.DeviceTypes).all()
#     return device_types

def get_device_types_all(
        db: Session,
        columns: str,
        search: str,
        filters: str,
        sort: str,
        page: int,
        limit: int
):
    query = db.query(Models_DeviceTypes.DeviceTypes)

    if columns is not None and columns != 'null':
        new_columns = columns.split('--')
        column_list = []
        for data in new_columns:
            column_list.append(getattr(Models_DeviceTypes.DeviceTypes, data))

        query = query.options(load_only(*column_list))

    if search is not None and search != 'null':
        query = query.filter(
            (
                Models_DeviceTypes.DeviceTypes.name.ilike(f"%{search}%") |
                Models_DeviceTypes.DeviceTypes.model_name.ilike(f"%{search}%")
            )
        )

    if filters is not None and filters != 'null':
        criteria = dict(x.split("*") for x in filters.split('--'))
        criteria_list = []
        for attr, value in criteria.items():
            _attr = getattr(Models_DeviceTypes.DeviceTypes, attr)
            filters = f"%{value}%"
            criteria_list.append(_attr.like(filters))

        query = query.filter(or_(*criteria_list))

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
        page_number=page, #trang hiện tại
        page_size=limit, #số mục trong trang
        total_pages=total_page, #tổng số trang
        total_record=total_record, # tổng số mục
        content=result
    )


# Phân trang
    # offset = (page - 1) * limit
    # device_types = query.offset(offset).limit(limit).all()
    # # device_types = query.all()
    # return device_types