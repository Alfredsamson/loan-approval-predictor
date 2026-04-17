
from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("decision_tree_model.pkl")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=["POST"])
def predict():
    if request.method == 'POST':
        income = float(request.form['income'])
        loan_amount = float(request.form['loan_amount'])
        dependents = int(request.form['dependents'])
        education = int(request.form['education'])
        self_employed = int(request.form['self_employed'])

        features = np.array([[income, loan_amount, dependents, education, self_employed]])
        prediction = model.predict(features)[0]

        result = "✅ Loan Approved" if prediction == 1 else "❌ Loan Rejected"
        return render_template('result.html', prediction=result)
