# app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# dbのインスタンスを作成（後でmodels.pyで使います）
db = SQLAlchemy()

def create_app():
    # Flaskアプリケーションのインスタンス作成
    app = Flask(__name__)

    # アプリケーションの設定
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # dbをアプリに関連付け
    db.init_app(app)

    # models.pyのインポート
    from models import User, Inventory, Transaction

    # ルートの定義（例）
    @app.route('/')
    def index():
        return "Hello, Flask Inventory App!"

    return app

# Flaskアプリケーションを作成
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
