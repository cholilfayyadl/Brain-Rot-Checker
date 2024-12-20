from flask import render_template, request, flash, redirect, url_for

class RecommendationModel:
    def __init__(self, db):
        self.db = db

    def manage_recommendations(self):
        if request.method == 'POST':
            category = request.form['category']
            recommendation_text = request.form['recommendation_text']
            self.db.recommendations.insert_one({'category': category, 'recommendation_text': recommendation_text})
            flash('Recommendation added successfully')
            return redirect(url_for('manage_recommendations'))

        recommendations = self.db.recommendations.find()
        return render_template('manage_recommendations.html', recommendations=recommendations)
