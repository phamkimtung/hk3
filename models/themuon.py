from backend.database import db

class TheMuon(db.Model):
    __tablename__ = 'themuon'
    id = db.Column(db.Integer, primary_key=True)
    id_khach_hang = db.Column(db.Integer, db.ForeignKey('khachhang.id'), nullable=False)
    id_sach_muon = db.Column(db.Integer, db.ForeignKey('sach.id'), nullable=False)
    id_nhan_vien = db.Column(db.Integer, db.ForeignKey('nhan_vien.id_nhan_vien'), nullable=False)
    ngay_muon = db.Column(db.Date, nullable=False)
    ngay_tra_du_dinh = db.Column(db.Date, nullable=False)
    ngay_tra_thuc_te = db.Column(db.Date)
