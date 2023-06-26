from fastapi import FastAPI

from .database import engine, Base
from fastapi.middleware.cors import CORSMiddleware
from .routers import user, DeviceGroupsType, Chip, DeviceTypes, Device

# from fastapi_pagination import add_pagination

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title='User + DeviceTypes',
    description='Greet uses with a nice message'
)

app.include_router(user.router)
app.include_router(Chip.router)
app.include_router(DeviceTypes.router)
app.include_router(DeviceGroupsType.router)
app.include_router(Device.router)

# add_pagination(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#CHUYỂN FILE JSON -> CSDL POSTGRESQL
#
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# import json
# from . import schemas, models
#
# # Tạo engine và session
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:081102@localhost:5432/test"
# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# db = SessionLocal()
#
# app = FastAPI(
#     title='User',
#     description='Greet uses with a nice message'
# )
#
# # Đường dẫn tới file JSON
# json_file_path = 'app/devicetypes.json'
#
# # Đọc dữ liệu từ file JSON
# with open(json_file_path, encoding='utf-8') as f:
#     data = json.load(f)
#
# # f = open("app/devicetypes.json", encoding='utf-8')
# # data = json.load(f)
# # Thêm dữ liệu vào cơ sở dữ liệu
# for user_data in data['data']:
#     for device_types in user_data['device_types']:
#         print(device_types)
#         user = models.DeviceTypes(
#             # sub=user_data.get('sub'),
#             # last_requested_time=user_data.get('last_requested_time'),
#             # email_verified=user_data.get('email_verified'),
#             # phone_number_verified=user_data.get('phone_number_verified'),
#             # old_sub=user_data.get('old_sub'),
#             # name=user_data.get('name'),
#             # phone_number=user_data.get('phone_number'),
#             # nd_requests=user_data.get('nd_requests'),
#             # nm_requests=user_data.get('nm_requests'),
#             # app_key=user_data.get('app_key'),
#             # email=user_data.get('email'),
#             # enabled=user_data.get('enabled'),
#             # status=user_data.get('status'),
#             # created=user_data.get('created'),
#             # updated=user_data.get('updated')
#
#             # name=user_data['name'],
#             # group_type_number=user_data['group_type_number'],
#             # id = user_data['id'],
#             # image_uri =user_data['image_uri'],
#             # created =user_data['created'],
#             # updated =user_data['updated']
#
#             id = device_types['id'],
#             name =device_types['name'],
#             description =device_types['description'],
#             type_number =device_types['type_number'],
#             chip_id =device_types['chip_id'],
#             device_group_type_id =device_types['device_group_type_id'],
#             model_name =device_types['model_name'],
#             manufacturer_name =device_types['manufacturer_name'],
#             created =device_types['created'],
#             updated =device_types['updated']
#
#             # id=device_types['chip_id'],
#             # name=device_types['chip']['name'],
#             # module=device_types['chip']['module'],
#
#             # id=user_data.device_types['chip_id'],
#             # name=user_data.device_types.chip.name,
#             # module=user_data.device_types.chip.module
#         )
#         db.add(user)
#
# # Lưu các thay đổi vào cơ sở dữ liệu
# db.commit()
# print("ok")
# # Đóng kết nối
# db.close()