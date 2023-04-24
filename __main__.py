from flask import Flask, render_template, redirect

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return redirect(location='/home', code=302)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
