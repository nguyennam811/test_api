from sqlalchemy.orm import Session
from ..models import Models_DeviceGroupsType
from sqlalchemy import or_, func
import math
from ..schemas import Schemas
def get_device_groups_type_all(
        db: Session,
        filters: str,
        search: str,
        sort: str,
        page: int,
        limit: int
):

    # device_groups_type = db.query(Models_DeviceGroupsType.DeviceGroupsType).all()
    query = db.query(Models_DeviceGroupsType.DeviceGroupsType)

    if filters is not None and filters != 'null':
        criteria = dict(x.split("*") for x in filters.split('--'))
        criteria_list = []
        for attr, value in criteria.items():
            _attr = getattr(Models_DeviceGroupsType.DeviceGroupsType, attr)
            filter = f"%{value}%"
            criteria_list.append(_attr.like(filter))

        query = query.filter(or_(*criteria_list))

    if search is not None and search != 'null':
        query = query.filter(
            Models_DeviceGroupsType.DeviceGroupsType.name.ilike(f"%{search}%")
        )

    if sort is not None and sort != 'null':
        query = query.order_by(','.join(sort.split('--')))

    # offset = (page - 1) * limit
    # device_groups_type = query.offset(offset).limit(limit).all()
    # return device_groups_type


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



