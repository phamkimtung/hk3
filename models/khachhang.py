# models/khachhang.py
from database import db
class KhachHang(db.Model):
    __tablename__ = "khachhang"
    id = db.Column(db.Integer, primary_key=True)
    ten = db.Column(db.String(255), nullable=False)
    dia_chi = db.Column(db.String(255), nullable=True)
    sdt = db.Column(db.String(15), nullable=True)
    tai_khoan = db.Column(db.String(50), db.ForeignKey('Tai_khoan.tai_khoan'), nullable=False)
    mat_khau = db.Column(db.String(255), nullable=False)
