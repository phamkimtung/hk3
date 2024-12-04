# services/auth_service.py

from models import db, KhachHang, TaiKhoan

class AuthService:

    @staticmethod
    def register(data):
        ho_ten = data.get('ho_ten')
        email = data.get('email')
        dien_thoai = data.get('dien_thoai')
        username = data.get('username')
        password = data.get('password')

        if KhachHang.query.filter_by(email=email).first():
            return {"message": "Email đã tồn tại"}, 400

        khachhang = KhachHang(ho_ten=ho_ten, email=email, dien_thoai=dien_thoai)
        db.session.add(khachhang)
        db.session.commit()

        taikhoan = tai_khoan(username=username, password=password, quyen=0, khachhang_id=khachhang.id)
        db.session.add(taikhoan)
        db.session.commit()

        return {"message": "Đăng ký thành công"}, 201

    @staticmethod
    def login(data):
        username = data.get('username')
        password = data.get('password')

        taikhoan = TaiKhoan.query.filter_by(username=username, password=password).first()

        if taikhoan:
            if taikhoan.quyen == 0:
                return {"message": "Chào mừng khách hàng"}, 200  # Khách hàng
            else:
                return {"message": "Chào mừng nhân viên"}, 200  # Nhân viên
        else:
            return {"message": "Thông tin đăng nhập không chính xác"}, 400
