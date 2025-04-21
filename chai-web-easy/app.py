from flask import Flask, request, render_template_string

app = Flask(__name__)
FLAG = "CIR{C_F0R_CH34P_X_CH4I}"

@app.route('/')
def index():
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Chai Cart</title>
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Quicksand&display=swap">
        <style>
            body {
                background-color: #fef9e7;
                font-family: 'Quicksand', sans-serif;
                color: #5d4037;
                display: flex;
                flex-direction: column;
                align-items: center;
                padding-top: 50px;
            }
            .cart {
                background: #fff3e0;
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.1);
                width: 350px;
                text-align: center;
            }
            input[type="number"] {
                width: 60px;
                text-align: center;
            }
            input[type="submit"] {
                margin-top: 15px;
                background: #8d6e63;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 10px;
                cursor: pointer;
                transition: 0.3s ease;
            }
            input[type="submit"]:hover {
                background: #6d4c41;
            }
            .note {
                margin-top: 15px;
                color: #a1887f;
                font-size: 0.9em;
            }
        </style>
    </head>
    <body>
        <div class="cart">
            <h1>☕ Chai Cart</h1>
            <p>Order your chai — only <b>100 PKR</b> each!</p>
            <form method="POST" action="/checkout">
                <label>Quantity: <input type="number" name="quantity" min="1" value="1"></label><br>
                <input type="hidden" name="price" value="100">
                <input type="submit" value="Checkout">
            </form>
            <div class="note">
                <!-- No discounts here... or are there? 🤔 -->
                <p>We don't allow chai theft, mind you.</p>
            </div>
        </div>
    </body>
    </html>
    ''')

@app.route('/checkout', methods=['POST'])
def checkout():
    try:
        quantity = int(request.form.get('quantity', 1))
        price = int(request.form.get('price', 100))
        total = quantity * price

        if total <= 10:
            return render_template_string(f'''
                <div class="cart">
                    <h1>🎉 Receipt</h1>
                    <p>Chai x{quantity} = {total} PKR</p>
                    <p><strong>Here’s your special brew: <code>{FLAG}</code></strong></p>
                </div>
            ''')
        else:
            return render_template_string(f'''
                <div class="cart">
                    <h1>🧾 Receipt</h1>
                    <p>Chai x{quantity} = {total} PKR</p>
                    <p>Enjoy your chai! ☕</p>
                </div>
            ''')
    except:
        return "Invalid input. Chai is sacred."

if __name__ == '__main__':
    app.run(debug=True)
