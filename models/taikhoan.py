from database import db

class tai_khoan(db.Model):
    __tablename__ = "tai_khoan"
    tai_khoan = db.Column(db.String(50), primary_key=True)
    mat_khau = db.Column(db.String(255), nullable=False)
    quyen = db.Column(db.Integer, nullable=False)  # 0: khách hàng, 1: nhân viên
