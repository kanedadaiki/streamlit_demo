from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

# データベースの作成（存在しない場合）と接続
conn = sqlite3.connect('real_estate.db')
c = conn.cursor()

# 物件テーブルの作成
c.execute('''CREATE TABLE IF NOT EXISTS properties (
                id INTEGER PRIMARY KEY,
                address TEXT,
                size INTEGER,
                rent INTEGER
            )''')

# テナントテーブルの作成
c.execute('''CREATE TABLE IF NOT EXISTS tenants (
                id INTEGER PRIMARY KEY,
                name TEXT,
                contact TEXT,
                property_id INTEGER,
                FOREIGN KEY(property_id) REFERENCES properties(id)
            )''')

# 物件追加エンドポイント
@app.route('/add_property', methods=['POST'])
def add_property():
    address = request.form['address']
    size = request.form['size']
    rent = request.form['rent']
    c.execute('''INSERT INTO properties (address, size, rent) VALUES (?, ?, ?)''', (address, size, rent))
    conn.commit()
    return '物件が追加されました'

# テナント追加エンドポイント
@app.route('/add_tenant', methods=['POST'])
def add_tenant():
    name = request.form['name']
    contact = request.form['contact']
    property_id = request.form['property_id']
    c.execute('''INSERT INTO tenants (name, contact, property_id) VALUES (?, ?, ?)''', (name, contact, property_id))
    conn.commit()
    return 'テナントが追加されました'

if __name__ == '__main__':
    app.run(debug=True)