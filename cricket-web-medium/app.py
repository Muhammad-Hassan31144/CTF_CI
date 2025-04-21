from flask import Flask, request, render_template_string
import hashlib

app = Flask(__name__)
FLAG = "CIR{SN34KY_71CK37_7H13F_BU5T3D}"

# Public ticket DB
TICKETS = {
    41: "Ali - PSL Match 1",
    43: "Zara - PSL Match 3",
}

# Secret ticket
SECRET_ID = 42
SECRET_NAME = "PSL Match 2"

# Token formula
def generate_token(ticket_id):
    return hashlib.md5(f"psl{ticket_id}_secret".encode()).hexdigest()[:8]

@app.route('/')
def index():
    return render_template_string('''
    <html>
    <head>
        <title>PSL Ticket Viewer</title>
        <style>
            body {
                font-family: monospace;
                background: #0f0f0f;
                color: #00ffcc;
                text-align: center;
                padding-top: 40px;
            }
            input[type="number"], input[type="text"] {
                padding: 8px;
                border: none;
                border-radius: 5px;
                margin-bottom: 10px;
            }
            input[type="submit"] {
                padding: 10px 20px;
                background-color: #00ffcc;
                color: black;
                border: none;
                border-radius: 6px;
                cursor: pointer;
            }
            .note {
                color: #888;
                font-size: 0.9em;
                margin-top: 15px;
            }
        </style>
    </head>
    <body>
        <h1>🎟️ PSL Ticket Viewer</h1>
        <p>Enter your Ticket ID:</p>
        <form method="GET" action="/ticket">
            <input type="number" name="id" required><br>
            <input type="text" name="token" placeholder="Optional token"><br>
            <input type="submit" value="View Ticket">
        </form>
        <div class="note">
            
            <!-- Some tickets require secret tokens. Check internal tools. -->
        </div>
    </body>
    </html>
    ''')

@app.route('/ticket')
def ticket():
    try:
        ticket_id = int(request.args.get('id', 0))
        token = request.args.get('token', '').strip()

        if ticket_id == SECRET_ID:
            expected = generate_token(ticket_id)
            if token == expected:
                return render_template_string(f'''
                    <h1>Your Ticket</h1>
                    <p>ID: {ticket_id}</p>
                    <p>VIP Access: {SECRET_NAME}</p>
                    <p>🎉 Flag: <code>{FLAG}</code></p>
                ''')
            else:
                return render_template_string(f'''
                    <h1>Restricted Ticket</h1>
                    <p>ID: {ticket_id}</p>
                    <p>This ticket requires a valid access token.</p>
                ''')
        else:
            ticket = TICKETS.get(ticket_id, "Ticket not found")
            return render_template_string(f'''
                <h1>Your Ticket</h1>
                <p>ID: {ticket_id}</p>
                <p>{ticket}</p>
            ''')
    except:
        return "Invalid request."

@app.route('/debug')
def debug():
    test_id = 99
    formula = f'"psl" + str(ticket_id) + "_secret"'
    code = 'hashlib.md5(f"psl{ticket_id}_secret".encode()).hexdigest()[:8]'
    token = generate_token(test_id)

    return f'''
    <pre>
    DEBUG MODE - Dev Token Tester

    Sample ID: {test_id}
    Token: {token}

    Token Formula (Python):
    ------------------------
    import hashlib

    def generate_token(ticket_id):
        return hashlib.md5(f"psl{{ticket_id}}_secret".encode()).hexdigest()[:8]

    # Example:
    generate_token({test_id}) → {token}
    </pre>
    '''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
