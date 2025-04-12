from flask import Flask, render_template, session, redirect, url_for, request, jsonify

app = Flask(__name__)
app.secret_key = 'mysecretkey'

# Sample product list
products = [
    {
    "id": 1,
    "name": "วอลล์ แม็กนั่ม มัทฉะ ครัมบ์เบิ้ล ไอศกรีม 66 ก.",
    "price": 50.00,
    "image": "https://st.bigc-cs.com/cdn-cgi/image/format=webp,quality=85/public/media/catalog/product/05/88/8851932463805/thumbnail/8851932463805_1-20241016085042-.jpg"
  },
  {
    "id": 2,
    "name": "เนสท์เล่ เอ็กซ์ตรีม อาฟเตอร์ ยู ชิบูย่า ฮันนี่ โทสต์ ไอศกรีม 78 ก.",
    "price": 35.00,
    "image": "https://st.bigc-cs.com/cdn-cgi/image/format=webp,quality=85/public/media/catalog/product/94/88/8850124090294/thumbnail/8850124090294_1-20240905111601-.jpg"
  },
  {
    "id": 3,
    "name": "แมกโนเลีย อัลมอนด์ ช็อกโก 58 ก.",
    "price": 20.00,
    "image": "https://st.bigc-cs.com/cdn-cgi/image/format=webp,quality=85/public/media/catalog/product/96/88/8853815008196/thumbnail/8853815008196_1-20240412095856-.jpg"
  },
  {
    "id": 4,
    "name": "แมกโนเลีย อัลมอนด์ วานิลลา 58 ก.",
    "price": 20.00,
    "image": "https://st.bigc-cs.com/cdn-cgi/image/format=webp,quality=85/public/media/catalog/product/02/88/8853815008202/thumbnail/8853815008202_1-20240412095842-.jpg"
  },
  {
    "id": 5,
    "name": "วอลล์ คอร์นเนตโต ไวท์โรส 88 ก.",
    "price": 18.00,
    "image": "https://st.bigc-cs.com/cdn-cgi/image/format=webp,quality=85/public/media/catalog/product/62/88/8851932469562/thumbnail/8851932469562_1-20240412095313-.jpg"
  },
  {
    "id": 6,
    "name": "โอรีโอ ไอศกรีมโคนกลิ่นครีมผสมชิ้นโอริโอคุ้กกี้ 70 ก.",
    "price": 35.00,
    "image": "https://st.bigc-cs.com/cdn-cgi/image/format=webp,quality=85/public/media/catalog/product/29/88/8850124087829/thumbnail/8850124087829_1-20231109232623-.jpg"  
  },
  {
    "id": 7,
    "name": "วอลล์ เอเชี่ยน ดีไลท์ กลิ่นนมฮอกไกโดผสมชิ้นโมจิ 58 ก.",
    "price": 10.00,
    "image": "https://st.bigc-cs.com/cdn-cgi/image/format=webp,quality=85/public/media/catalog/product/62/88/8851932459662/thumbnail/8851932459662_1-20231113090323-.jpeg"
  },
  {
    "id": 8,
    "name": "วอลล์ โอวัลติน ดาร์กช็อก ครันชี่ ไอศกรีม 72 ก.",
    "price": 15.00,
    "image": "https://st.bigc-cs.com/cdn-cgi/image/format=webp,quality=85/public/media/catalog/product/62/88/8851932450362/thumbnail/8851932450362_1-20230913190748-.jpg"
  },
  {
    "id": 9,
    "name": "วอลล์ แม็กนั่ม เบลเจียน ช็อกโกแลต ลักซ์ 70 ก.",
    "price": 50.00,
    "image": "https://st.bigc-cs.com/cdn-cgi/image/format=webp,quality=85/public/media/catalog/product/55/88/8851932442855/thumbnail/8851932442855_1-20240905113024-.jpg"
  },
  {
    "id": 10,
    "name": "แมกโนเลีย ซันเดย์ ไอศกรีม รสช็อกโกแลตและกลิ่นวานิลลามอลต์ 80 ก.",
    "price": 20.00,
    "image": "https://st.bigc-cs.com/cdn-cgi/image/format=webp,quality=85/public/media/catalog/product/89/88/8853815007489/thumbnail/8853815007489_1-20230717142937-.jpg"
  },
  {
    "id": 11,
    "name": "คิงส์ แกรนด์ ไอศกรีม รสทินรูฟบราวนี่ 560 ก.",
    "price": 115.00,
    "image": "https://st.bigc-cs.com/cdn-cgi/image/format=webp,quality=85/public/media/catalog/product/23/95/9556757800123/thumbnail/9556757800123.jpg"
  },
  {
    "id": 12,
    "name": "บิงกือเร เมล่อน ไอศกรีม 80 ก.",
    "price": 25.00,
    "image": "https://st.bigc-cs.com/cdn-cgi/image/format=webp,quality=85/public/media/catalog/product/12/88/8851932421812/thumbnail/8851932421812_1-20230717150557-.jpg"
  },
  {
    "id": 13,
    "name": "วอลล์ ไอศกรีม โอวัลติน ไวท์มอลต์ครั้นชี่ 72 ก.",
    "price": 30.00,
    "image": "https://st.bigc-cs.com/cdn-cgi/image/format=webp,quality=85/public/media/catalog/product/97/88/8851932421997/thumbnail/8851932421997.jpg"
  },
  {
    "id": 14,
    "name": "ครีโม ซันเด สตรอเบอรี่ 160 ก.",
    "price": 40.00,
    "image": "https://st.bigc-cs.com/cdn-cgi/image/format=webp,quality=85/public/media/catalog/product/13/88/8850387006513/thumbnail/8850387006513_1-20241121091316-.jpg"
  },
  {
    "id": 15,
    "name": "คิงส์ ไอศกรีม รสรวมมิตร 587 ก.",
    "price": 80.00,
    "image": "https://st.bigc-cs.com/cdn-cgi/image/format=webp,quality=85/public/media/catalog/product/44/88/8853815007144/thumbnail/8853815007144.jpg"}
]

target_lenge = 33
products_card = products.copy()
for product in products_card:
    if len(product["name"]) > target_lenge:
        product["name"] = product["name"][:target_lenge-3] + "..."

def get_cart_count():
    return sum(session.get('cart', {}).values())

@app.route('/')
def index():
    cart_count = get_cart_count()
    return render_template('index.html', products=products_card, cart_count=cart_count)

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

                name = p['name']

                # target_lenge = 25
                # if len(p['name']) > target_lenge:
                #     name = p['name'][:target_lenge-3] + '...'
                # else:
                    

                cart_items.append({
                    
                    'name': name,
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


# if __name__ == '__main__':
#     # app.run(debug=True)
#     app.run(host='0.0.0.0', port=5007, debug=True) #,debug=False)
