{% extends "base.html" %}
{% block title %}History{% endblock %}
{% block content %}
<h1 class="text-center">History</h1>
<table class="table table-striped">
    <thead>
        <tr>
            <th>Date</th>
            <th>Symptoms</th>
            <th>Diagnosis</th>
        </tr>
    </thead>
    <tbody>
        {% for record in history %}
        <tr>
            <td>{{ record.date }}</td>
            <td>{{ record.symptoms | join(', ') }}</td>
            <td>{{ record.diagnosis }}</td>
        </tr>
        {% endfor %}
    </tbody>
</table>
{% endblock %}
