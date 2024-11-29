# models.py

from app import db  # app.py から db をインポート

# ユーザークラス
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<User {self.name}>"

# 在庫アイテムクラス
class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Inventory {self.item_name} - {self.quantity}>"

# 取引クラス（仕入れや使用の記録）
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('inventory.id'), nullable=False)
    transaction_type = db.Column(db.String(50), nullable=False)  # 'purchase' or 'usage'
    quantity = db.Column(db.Integer, nullable=False)

    # リレーションシップの定義
    user = db.relationship('User', backref='transactions')
    inventory = db.relationship('Inventory', backref='transactions')

    def __repr__(self):
        return f"<Transaction {self.transaction_type} - Item: {self.inventory.item_name} Quantity: {self.quantity}>"
