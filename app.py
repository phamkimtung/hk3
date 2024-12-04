from flask import Flask
from flask_migrate import Migrate
from database import db
from routes.book import book_routes
from routes.auth import auth_bp
# Khởi tạo Flask app
app = Flask(__name__)

# Cấu hình cơ sở dữ liệu
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:02032005@localhost/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Khởi tạo SQLAlchemy và Migrate
db.init_app(app)
migrate = Migrate(app, db)

# Đăng ký blueprint cho routes
app.register_blueprint(book_routes)
app.register_blueprint(auth_bp)

# Chạy ứng dụng
if __name__ == "__main__":
    app.run(debug=True)
