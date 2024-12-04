from database import db

class NhanVien(db.Model):
    __tablename__ = "nhan_vien"
    id_nhan_vien = db.Column(db.Integer, primary_key=True)
    ten = db.Column(db.String(255), nullable=False)
    sdt = db.Column(db.String(15), nullable=False)
    tai_khoan = db.Column(db.String(50), db.ForeignKey("tai_khoan.tai_khoan"), nullable=False)
    mat_khau = db.Column(db.String(50), nullable=False)

