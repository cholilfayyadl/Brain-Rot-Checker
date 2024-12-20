from flask import render_template, request, redirect, url_for, session, flash

class AuthModel:
    def __init__(self, db):
        self.db = db

    def login(self):
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            user = self.db.users.find_one({'username': username, 'password': password})
            if user:
                session['username'] = username
                session['role'] = user.get('role', 'user')
                if session['role'] == 'admin':
                    return redirect(url_for('admin_dashboard'))
                return redirect(url_for('index'))
            flash('Invalid credentials')
        return render_template('login.html')

    def register(self):
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            self.db.users.insert_one({'username': username, 'password': password, 'role': 'user'})
            flash('Registration successful, please log in')
            return redirect(url_for('login_view'))
        return render_template('register.html')

    def logout(self):
        session.clear()
        return redirect(url_for('login_view'))
