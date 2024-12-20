from flask import render_template, request, flash, redirect, url_for
from bson.objectid import ObjectId  # Untuk bekerja dengan ObjectId MongoDB

class SymptomModel:
    def __init__(self, db):
        self.db = db

    def manage_symptoms(self):
        if request.method == 'POST':
            # Periksa apakah ini adalah permintaan untuk mengedit gejala
            edit_symptom_id = request.form.get('edit_symptom')
            if edit_symptom_id:
                # Proses update gejala berdasarkan ID
                symptom_name = request.form['symptom_name']
                weight = int(request.form['weight'])
                risk_category = request.form['risk_category']

                self.db.symptoms.update_one(
                    {'_id': ObjectId(edit_symptom_id)},
                    {'$set': {
                        'symptom_name': symptom_name,
                        'weight': weight,
                        'risk_category': risk_category
                    }}
                )
                flash('Gejala berhasil diperbarui.', 'success')
            else:
                # Tambah gejala baru
                symptom_name = request.form['symptom_name']
                weight = int(request.form['weight'])
                risk_category = request.form['risk_category']

                self.db.symptoms.insert_one({
                    'symptom_name': symptom_name,
                    'weight': weight,
                    'risk_category': risk_category
                })
                flash('Gejala berhasil ditambahkan.', 'success')

            return redirect(url_for('manage_symptoms'))

        # Jika metode GET, ambil semua gejala dari database
        symptoms = self.db.symptoms.find()
        return render_template('manage_symptoms.html', symptoms=symptoms)

    def check_symptoms(self, form_data):
        symptoms_data = self.db.symptoms.find()
        total_score = 0
        risk_category = "Rendah"
        recommendations = []

        for symptom in symptoms_data:
            value = form_data.get(symptom['symptom_name'])
            if value == "Ya":  # Cek apakah form data berisi "Ya"
                total_score += symptom['weight']  # Tambahkan bobot gejala
                if symptom['risk_category'] not in recommendations:
                    recommendations.append(symptom['risk_category'])  # Tambahkan kategori risiko

        # Menentukan kategori risiko berdasarkan total skor
        if total_score >= 15:
            risk_category = "Tinggi"
        elif total_score >= 7:
            risk_category = "Sedang"

        # Mendapatkan teks rekomendasi berdasarkan kategori risiko
        recommendations_text = []
        for recommendation in recommendations:
            recommendation_data = self.db.recommendations.find_one({'category': recommendation})
            if recommendation_data:
                recommendations_text.append(recommendation_data['recommendation_text'])

        # Kembalikan hasil pengecekan dengan skor dan rekomendasi
        return render_template('result.html', total_score=total_score, 
                               risk_category=risk_category, recommendations=recommendations_text)
