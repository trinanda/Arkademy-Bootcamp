from flask import Flask, render_template
import pymysql

db = pymysql.connect("localhost", "tri", "#Admin123", "Arkademy")

app = Flask(__name__)

@app.route('/')
def index():
    cursor = db.cursor()
    sql = "select product_categories.id, product_categories.name, products.name FROM products INNER JOIN product_categories ON products.category_id=product_categories.id LIMIT 3;"

    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)