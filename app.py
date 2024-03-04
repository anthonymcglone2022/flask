from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'sha256_prototype'

# In-memory database
users = {'admin':'password'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            return 'Username already exists!'
        users[username] = password
        return redirect('/login')
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['login']
        password = request.form['secret']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect('/dashboard')
        else:
            return 'Invalid username or password!'
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        #return f'Welcome {session["username"]}! This is your dashboard.'
        return render_template('dashboard.html', username=session["username"])
    return redirect('/login')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/login')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
