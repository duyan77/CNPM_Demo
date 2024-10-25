from flask import Flask, render_template, request
import dao

app = Flask(__name__)


@app.route('/')
def index():
    q = request.args.get("q")
    products = dao.load_products(q)
    categories = dao.load_categories(products, q)
    return render_template('index.html', categories=categories, products=products)


if __name__ == '__main__':
    app.run(debug=True)
