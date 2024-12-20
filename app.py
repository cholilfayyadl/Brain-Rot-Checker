import os
from flask import Flask, render_template, redirect, url_for, request, session, flash
from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv
from models.auth_model import AuthModel
from models.symptom_model import SymptomModel
from models.recommendation_model import RecommendationModel

# Load .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'default_secret_key')

# Database setup using environment variable for MongoDB URI
mongo_uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017')
client = MongoClient(mongo_uri)
db = client['brain_rot_checker']

auth_model = AuthModel(db)
symptom_model = SymptomModel(db)
recommendation_model = RecommendationModel(db)

@app.route('/')
def index():
    return render_template('dashboard.html')

# Authentication routes
@app.route('/login', methods=['GET', 'POST'])
def login_view():
    return auth_model.login()

@app.route('/register', methods=['GET', 'POST'])
def register_view():
    return auth_model.register()

@app.route('/logout')
def logout_view():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login_view'))

# Admin dashboard
@app.route('/admin', methods=['GET', 'POST'])
def admin_dashboard():
    if 'username' not in session or session.get('role') != 'admin':
        flash('You must be an admin to access this page.', 'warning')
        return redirect(url_for('login_view'))
    return render_template('admin_dashboard.html')

@app.route('/admin/symptoms', methods=['GET', 'POST'])
def manage_symptoms():
    if 'username' not in session or session.get('role') != 'admin':
        flash('You must be an admin to access this page.', 'warning')
        return redirect(url_for('login_view'))
    return symptom_model.manage_symptoms()

@app.route('/admin/symptoms/edit/<symptom_id>', methods=['GET', 'POST'])
def edit_symptom(symptom_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('You must be an admin to access this page.', 'warning')
        return redirect(url_for('login_view'))
    
    symptom = db.symptoms.find_one({'_id': ObjectId(symptom_id)})
    if not symptom:
        flash('Symptom not found.', 'danger')
        return redirect(url_for('manage_symptoms'))

    if request.method == 'POST':
        symptom_name = request.form.get('symptom_name', '').strip()
        weight = request.form.get('weight', '').strip()
        risk_category = request.form.get('risk_category', '').strip()

        # Validasi input
        if not symptom_name or not weight.isdigit() or not risk_category:
            flash('Invalid input. Please check your data.', 'danger')
        else:
            symptom_model.update_symptom(symptom_id, symptom_name, int(weight), risk_category)
            flash('Symptom updated successfully.', 'success')
            return redirect(url_for('manage_symptoms'))

    return render_template('edit_symptom.html', symptom=symptom)

@app.route('/admin/symptoms/delete/<symptom_id>')
def delete_symptom(symptom_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('You must be an admin to access this page.', 'warning')
        return redirect(url_for('login_view'))
    
    result = symptom_model.delete_symptom(symptom_id)
    if result:
        flash('Symptom deleted successfully.', 'success')
    else:
        flash('Failed to delete symptom. It might not exist.', 'danger')
    return redirect(url_for('manage_symptoms'))

@app.route('/admin/recommendations', methods=['GET', 'POST'])
def manage_recommendations():
    if 'username' not in session or session.get('role') != 'admin':
        flash('You must be an admin to access this page.', 'warning')
        return redirect(url_for('login_view'))
    return recommendation_model.manage_recommendations()

@app.route('/admin/recommendations/edit/<recommendation_id>', methods=['GET', 'POST'])
def edit_recommendation(recommendation_id):
    if 'username' not in session or session.get('role') != 'admin':
        flash('You must be an admin to access this page.', 'warning')
        return redirect(url_for('login_view'))
    
    recommendation = db.recommendations.find_one({'_id': ObjectId(recommendation_id)})
    if not recommendation:
        flash('Recommendation not found.', 'danger')
        return redirect(url_for('manage_recommendations'))

    if request.method == 'POST':
        category = request.form.get('category', '').strip()
        recommendation_text = request.form.get('recommendation_text', '').strip()

        if not category or not recommendation_text:
            flash('Invalid input. Please check your data.', 'danger')
        else:
            db.recommendations.update_one(
                {'_id': ObjectId(recommendation_id)},
                {'$set': {'category': category, 'recommendation_text': recommendation_text}}
            )
            flash('Recommendation updated successfully.', 'success')
            return redirect(url_for('manage_recommendations'))

    return render_template('edit_recommendation.html', recommendation=recommendation)

# User routes
@app.route('/check', methods=['GET', 'POST'])
def check_brain_rot():
    if 'username' not in session:
        flash('You must be logged in to access this page.', 'warning')
        return redirect(url_for('login_view'))

    if request.method == 'POST':
        return symptom_model.check_symptoms(request.form)

    symptoms = db.symptoms.find()
    return render_template('check.html', symptoms=symptoms)

@app.route('/history')
def history():
    if 'username' not in session:
        flash('You must be logged in to access this page.', 'warning')
        return redirect(url_for('login_view'))
    return render_template('history.html')

if __name__ == '__main__':
    app.run(debug=True)
