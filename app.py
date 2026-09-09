from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'lab-only-secret-key'

USERS = [
    {'id': 1, 'name': 'Uroš Arsić', 'username': 'uros', 'role': 'Administrator'},
    {'id': 2, 'name': 'Ana Jovanović', 'username': 'ana', 'role': 'Security Analyst'},
    {'id': 3, 'name': 'Matija Kostić', 'username': 'matija', 'role': 'Operator'},
    {'id': 4, 'name': 'Milica Savić', 'username': 'milica', 'role': 'Korisnik'}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users')
def users():
    q = request.args.get('q', '').strip().lower()
    filtered = [
        u for u in USERS
        if not q or q in u['name'].lower() or q in u['username'].lower()
    ]
    return render_template('users.html', users=filtered, q=q)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form.get('username') == 'admin' and request.form.get('password') == 'lab123':
            session['user'] = 'admin'
            flash('Uspešno ste prijavljeni.', 'success')
            return redirect(url_for('dashboard'))
        flash('Neispravno korisničko ime ili lozinka.', 'error')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', user=session['user'])

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
