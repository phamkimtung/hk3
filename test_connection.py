from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

# Thay đổi chuỗi kết nối theo thông tin của bạn
DATABASE_URI = "postgresql://postgres:02032005@localhost:5432/hk3"

try:
    engine = create_engine(DATABASE_URI)
    connection = engine.connect()
    print("Kết nối thành công với cơ sở dữ liệu!")
    connection.close()
except OperationalError as e:
    print("Lỗi kết nối với cơ sở dữ liệu:", e)
