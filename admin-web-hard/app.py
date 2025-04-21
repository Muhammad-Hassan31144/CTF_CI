
from flask import Flask, request, render_template_string, redirect, url_for, make_response
import jwt
import os
import random
import string

app = Flask(__name__)

# Insecure on purpose!
SECRET_KEY = "superinsecurekey"
USERS = {"user": "pass123"}

# Random flag file
FLAG_FILENAME = f"flag_{''.join(random.choices(string.ascii_lowercase + string.digits, k=6))}.txt"
FLAG_PATH = os.path.join(os.getcwd(), FLAG_FILENAME)
FLAG = "CIR{L0G_BR0K3N_4U7H_BR0K3N}"

# Write flag to file at startup
if not os.path.exists(FLAG_PATH):
    with open(FLAG_PATH, 'w') as f:
        f.write(FLAG)

@app.route('/')
def index():
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Login</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
    </head>
    <body>
        <div class="container">
            <h1>Login</h1>
            <form method="POST" action="/login">
                <label>Username:</label>
                <input type="text" name="username" required>
                
                <!-- Dev is forgetful, Please dont mind looking at this! V2hhdCB5b3UgYXJlIGxvb2tpbmcgZm9yIGlzICIyZiA3MiA2ZiA2MiA2ZiA3NCA3MyAyZSA3NCA3OCA3NCI= -->

                <label>Password:</label>
                <input type="password" name="password" required>
                <input type="submit" value="Login">
            </form>
        </div>
    </body>
    </html>
    ''')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if USERS.get(username) == password:
        token = jwt.encode({"username": username, "role": "user"}, SECRET_KEY, algorithm="HS256")
        resp = make_response(redirect(url_for('dashboard')))
        resp.set_cookie('jwt', token)
        return resp
    return "Invalid credentials", 401


@app.route('/dashboard')
def dashboard():
    token = request.cookies.get('jwt')
    if not token:
        return redirect(url_for('index'))

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except Exception as e:
        return f"Invalid token: {e}", 403

    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Dashboard</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
    </head>
    <body>
        <div class="container">
            <h1>Dashboard</h1>
            <p>Welcome, {{ username }} (Role: {{ role }})</p>
            <h2>Search Logs</h2>
            <form method="GET" action="/search_logs">
                <label>Search term:</label>
                <input type="text" name="term" required>
                <input type="submit" value="Search">
            </form>
        </div>
    </body>
    </html>
    ''', username=payload['username'], role=payload['role'])


@app.route('/search_logs')
def search_logs():
    token = request.cookies.get('jwt')
    if not token:
        return redirect(url_for('index'))

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except Exception as e:
        return f"Invalid token: {e}", 403

    role = payload.get('role', 'user')
    term = request.args.get('term', '')
    command = f"grep '{term}' /app/logs.txt"
    output = os.popen(command).read()

    if role == "admin":
        output += f"\n[+] Admin Access: Flag file is at {FLAG_PATH}"

    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Search Results</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
    </head>
    <body>
        <div class="container">
            <h1>Log Search Results</h1>
            <p>Role: {{ role }}</p>
            <pre>{{ output }}</pre>
            <a href="/dashboard">Back to Dashboard</a>
        </div>
    </body>
    </html>
    ''', output=output, role=role)


@app.route('/robots.txt')
def displayrobo():
    return "User-agent: *\nDisallow: /admin/\n\nCredentials: user:pass123\nSecretKey: superinsecurekey", 200, {'Content-Type': 'text/plain'}


if __name__ == '__main__':
    app.run(debug=True)
