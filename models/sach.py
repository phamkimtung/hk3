from database import db

class Sach(db.Model):
    __tablename__ = 'sach'
    id = db.Column(db.Integer, primary_key=True)
    ten_sach = db.Column(db.String(255), nullable=False)
    mo_ta = db.Column(db.Text, nullable=True)
    tac_gia = db.Column(db.String(255), nullable=False)
    nam_xuat_ban = db.Column(db.Integer, nullable=True)
    trang_thai = db.Column(db.Boolean, default=True)

    def to_dict(self):
        """Chuyển đổi dữ liệu sách thành dictionary."""
        return {
            "id": self.id,
            "ten_sach": self.ten_sach,
            "mo_ta": self.mo_ta,
            "tac_gia": self.tac_gia,
            "nam_xuat_ban": self.nam_xuat_ban,
            "trang_thai": self.trang_thai,
        }
