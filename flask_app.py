import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
from flask import Flask, render_template, request, jsonify
import traceback

app = Flask(__name__)

# Load the trained model
try:
    model = joblib.load('decision_tree_model.pkl')
except FileNotFoundError:
    model = None
    print("Warning: Model file 'decision_tree_model.pkl' not found.")

# Initialize label encoders
try:
    dummy_df = pd.DataFrame({
        ' education': [' Graduate', ' Not Graduate', ' Graduate'],
        ' self_employed': [' Yes', ' No', ' Yes'],
        ' loan_status': [' Approved', ' Rejected', ' Approved']
    })
    le_education = LabelEncoder()
    le_self_employed = LabelEncoder()

    le_education.fit(dummy_df[' education'])
    le_self_employed.fit(dummy_df[' self_employed'])

except Exception as e:
    print(f"Error initializing label encoders: {e}")


@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')


@app.route('/api/predict', methods=['POST'])
def predict():
    """Handle prediction requests"""
    try:
        if model is None:
            return jsonify({
                'success': False,
                'error': 'Model not loaded. Please ensure decision_tree_model.pkl is available.'
            }), 500

        data = request.json

        # Extract and convert input data
        no_of_dependents = int(data.get('no_of_dependents', 0))
        education = data.get('education', ' Graduate')
        self_employed = data.get('self_employed', ' Yes')
        income_annum = float(data.get('income_annum', 0))
        loan_amount = float(data.get('loan_amount', 0))
        loan_term = int(data.get('loan_term', 1))
        cibil_score = int(data.get('cibil_score', 700))
        residential_assets_value = float(data.get('residential_assets_value', 0))
        commercial_assets_value = float(data.get('commercial_assets_value', 0))
        luxury_assets_value = float(data.get('luxury_assets_value', 0))
        bank_asset_value = float(data.get('bank_asset_value', 0))

        # Prepare input data for prediction
        input_data = pd.DataFrame([{
            ' no_of_dependents': no_of_dependents,
            ' education': le_education.transform([education])[0],
            ' self_employed': le_self_employed.transform([self_employed])[0],
            ' income_annum': income_annum,
            ' loan_amount': loan_amount,
            ' loan_term': loan_term,
            ' cibil_score': cibil_score,
            ' residential_assets_value': residential_assets_value,
            ' commercial_assets_value': commercial_assets_value,
            ' luxury_assets_value': luxury_assets_value,
            ' bank_asset_value': bank_asset_value
        }])

        # Make prediction
        prediction = model.predict(input_data)
        loan_status = "Approved" if prediction[0] == 0 else "Rejected"

        # Generate suggestions if rejected
        suggestions = []
        if loan_status == "Rejected":
            if cibil_score < 700:
                suggestions.append(
                    "Improve your CIBIL Score: Pay bills on time, reduce credit utilization, "
                    "and avoid opening too many new credit accounts."
                )
            monetary_installment = loan_amount / (loan_term * 12)
            if income_annum < monetary_installment * 2:
                suggestions.append(
                    "Increase your Income: Consider increasing your income or applying for "
                    "a lower loan amount."
                )
            total_assets = (residential_assets_value + commercial_assets_value +
                            luxury_assets_value + bank_asset_value)
            if total_assets < loan_amount * 1.5:
                suggestions.append(
                    "Increase your Assets: Building up your assets can demonstrate "
                    "financial stability."
                )
            suggestions.append(
                "Reduce Existing Debt: Lowering your existing debt can improve your "
                "debt-to-income ratio."
            )
            suggestions.append(
                "Consider a Co-applicant: Applying with a co-applicant with a good credit "
                "history and stable income can increase approval chances."
            )
            suggestions.append(
                "Review Loan Terms: Explore different loan products and terms that might be "
                "a better fit for your financial situation."
            )

        return jsonify({
            'success': True,
            'loan_status': loan_status,
            'suggestions': suggestions
        })

    except Exception as e:
        error_traceback = traceback.format_exc()
        print(f"Error during prediction: {error_traceback}")
        return jsonify({
            'success': False,
            'error': f'An error occurred during prediction: {str(e)}'
        }), 500


if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
