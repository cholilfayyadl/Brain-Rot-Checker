from functools import wraps
from flask import session, redirect, url_for, render_template, request, flash
from models.user import User

def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.authenticate(username, password)
        if user:
            session["username"] = user["username"]
            session["role"] = user["role"]
            return redirect(url_for("index"))
        flash("Login gagal, username atau password salah", "danger")
    return render_template("login.html")

def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        role = request.form.get("role", "user")
        if User.create_user(username, password, role):
            flash("Registrasi berhasil, silakan login", "success")
            return redirect(url_for("login"))
        flash("Username sudah digunakan", "danger")
    return render_template("register.html")

def logout():
    session.clear()
    return redirect(url_for("login"))

def login_required(role=None):
    def decorator(f):
        @wraps(f)
        def wrapped_function(*args, **kwargs):
            if "username" not in session:
                flash("Silakan login terlebih dahulu.", "warning")
                return redirect(url_for("login"))
            if role and session.get("role") != role:
                flash("Anda tidak memiliki akses ke halaman ini.", "danger")
                return redirect(url_for("index"))
            return f(*args, **kwargs)
        return wrapped_function
    return decorator
