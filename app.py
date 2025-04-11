from flask import Flask, render_template, session, redirect, url_for, request, jsonify

app = Flask(__name__)
app.secret_key = 'mysecretkey'

# Sample product list
products = [
    {"id": 1, "name": "Laptop", "price": 1200, "image": "/static/img/laptop.jpg"},
    {"id": 2, "name": "Smartphone", "price": 800, "image": "/static/img/headphones.webp"},
    {"id": 3, "name": "Headphones", "price": 150, "image": "/static/img/headphones.webp"},
    {"id": 4, "name": "Smartwatch", "price": 200, "image": "/static/img/headphones.webp"},
    {"id": 5, "name": "Camera", "price": 500, "image": "/static/img/smartphone.webp"},
    {"id": 6, "name": "Tablet", "price": 600, "image": "/static/img/smartphone.webp"},
    {"id": 7, "name": "Gaming Mouse", "price": 75, "image": "/static/img/smartphone.webp"},
    {"id": 8, "name": "Keyboard", "price": 90, "image": "/static/img/headphones.webp"},
    {"id": 9, "name": "Monitor", "price": 300, "image": "/static/img/headphones.webp"},
    {"id": 10, "name": "Speaker", "price": 180, "image": "/static/img/smartphone.webp"},
]

def get_cart_count():
    return sum(session.get('cart', {}).values())

@app.route('/')
def index():
    cart_count = get_cart_count()
    return render_template('index.html', products=products, cart_count=cart_count)

@app.route('/cart')
def cart():
    cart = session.get('cart', {})
    cart_items = []
    total = 0
    for product_id, quantity in cart.items():
        for p in products:
            if p['id'] == int(product_id):
                item_total = p['price'] * quantity
                total += item_total
                cart_items.append({
                    'name': p['name'],
                    'price': p['price'],
                    'quantity': quantity,
                    'total': item_total
                })
    cart_count = get_cart_count()
    return render_template('cart.html', cart_items=cart_items, total=total, cart_count=cart_count)

@app.route('/clear_cart')
def clear_cart():
    session.pop('cart', None)
    return redirect(url_for('cart'))

@app.route('/api/add_to_cart', methods=['POST'])
def api_add_to_cart():
    product_id = request.json.get('product_id')
    if not product_id:
        return jsonify({'status': 'error', 'message': 'Missing product_id'}), 400

    if 'cart' not in session:
        session['cart'] = {}
    cart = session['cart']
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    session['cart'] = cart
    return jsonify({'status': 'success', 'cart': cart})

@app.route('/api/confirm_order', methods=['POST'])
def confirm_order():
    cart = session.get('cart', {})
    if not cart:
        return jsonify({'status': 'error', 'message': 'Cart is empty'}), 400

    # 🔧 Example: you could store this in a database or log it
    print("🧾 Order confirmed:", cart)

    # Just return success & QR image URL
    return jsonify({
        'status': 'success',
        'qr_url': 'https://blog.tcea.org/wp-content/uploads/2022/05/qrcode_tcea.org-1.png'
    })


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5005, debug=False) #,debug=False)
