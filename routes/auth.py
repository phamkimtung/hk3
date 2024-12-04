from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from models.khachhang import KhachHang
from models.nhanvien import NhanVien
from models.taikhoan import tai_khoan
from database import db  # Import db từ database.py

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    tai_khoan = data.get('tai_khoan')
    mat_khau = data.get('mat_khau')

    if not tai_khoan or not mat_khau:
        return jsonify({"message": "Tài khoản hoặc mật khẩu không chính xác"}), 400

    # Kiểm tra tài khoản khách hàng
    khachhang = KhachHang.query.filter_by(tai_khoan=tai_khoan, mat_khau=mat_khau).first()
    if khachhang:
        return jsonify({"status": 0, "khach_hang": {"id": khachhang.id, "ten": khachhang.ten, "sdt": khachhang.sdt}})

    # Kiểm tra tài khoản nhân viên
    nhanvien = NhanVien.query.filter_by(tai_khoan=tai_khoan, mat_khau=mat_khau).first()
    if nhanvien:
        return jsonify({"status": 1, "nhan_vien": {"id": nhanvien.id_nhan_vien, "ten": nhanvien.ten, "sdt": nhanvien.sdt}})

    return jsonify({"message": "NOT FOUND"}), 404


@auth_bp.route('/register', methods=['POST'])
def register():
    # Lấy dữ liệu từ request
    data = request.get_json()
    ten = data.get('ten')
    dia_chi = data.get('dia_chi')
    sdt = data.get('sdt')
    tai_khoan = data.get('tai_khoan')  # Liên kết với tài khoản
    mat_khau = data.get('mat_khau')  # Mật khẩu của khách hàng

    # Kiểm tra xem tất cả các trường có được điền đầy đủ không
    if not all([ten, dia_chi, sdt, tai_khoan, mat_khau]):
        return jsonify({"message": "Thiếu thông tin khách hàng"}), 400

    # Mã hóa mật khẩu trước khi lưu vào cơ sở dữ liệu
    hashed_password = generate_password_hash(mat_khau)

    # Tạo mới đối tượng KhachHang và thêm vào cơ sở dữ liệu
    khachhang = KhachHang(
        ten=ten,
        dia_chi=dia_chi,
        sdt=sdt,
        tai_khoan=tai_khoan,  # Liên kết với tài khoản của khách hàng
        mat_khau=hashed_password  # Lưu mật khẩu đã được mã hóa
    )

    db.session.add(khachhang)
    db.session.commit()

    # Trả về thông tin khách hàng mới được thêm vào
    return jsonify({
        "message": "Thêm khách hàng thành công",
        "khach_hang": {
            "id": khachhang.id,
            "ten": khachhang.ten,
            "dia_chi": khachhang.dia_chi,
            "sdt": khachhang.sdt,
            "tai_khoan": khachhang.tai_khoan
        }
    }), 201