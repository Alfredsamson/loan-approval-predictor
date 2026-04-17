# Loan Approval Predictor - HTML/CSS/JS Website

This is a converted version of the Streamlit app that uses Flask as the backend and plain HTML/CSS/JavaScript for the frontend.

## Project Structure

```
loan_web_app/
├── flask_app.py              # Flask backend application
├── requirements.txt           # Python dependencies
├── decision_tree_model.pkl   # Trained ML model
├── templates/
│   └── index.html           # HTML template
└── static/
    ├── style.css            # CSS styling
    └── script.js            # JavaScript interactivity
```

## Installation

### 1. Install Dependencies

Make sure you have a virtual environment activated, then install the required packages:

```bash
pip install -r requirements.txt
```

### 2. Run the Application

Start the Flask server:

```bash
python flask_app.py
```

The application will be available at `http://localhost:5000`

## Features

- **Welcome Page**: Introduction to the application with a call-to-action button
- **Prediction Form**: User-friendly form to input loan details
- **Real-time Validation**: Form validation and error handling
- **Instant Predictions**: ML-based loan approval predictions
- **Smart Suggestions**: Personalized improvement suggestions for rejected applications
- **Responsive Design**: Works on desktop, tablet, and mobile devices

## Input Fields

The prediction form requires the following information:

- **Number of Dependents**: 0-10 (slider)
- **Education**: Graduate or Not Graduate
- **Self Employed**: Yes or No
- **Annual Income**: In dollars
- **Loan Amount**: In dollars
- **Loan Term**: In years (1-50)
- **CIBIL Score**: 300-900
- **Residential Assets Value**: In dollars
- **Commercial Assets Value**: In dollars
- **Luxury Assets Value**: In dollars
- **Bank Asset Value**: In dollars

## Model

The application uses a trained Decision Tree model (`decision_tree_model.pkl`) for predictions. The model requires:

- Specific input features in a defined format
- Label encoders for categorical variables (education, self-employed status)

## Files Description

### flask_app.py
- Flask application server
- Loads the trained model and label encoders
- Provides API endpoint `/api/predict` for predictions
- Generates personalized suggestions based on input

### templates/index.html
- Single-page application with two views: Welcome and Prediction
- Responsive layout with form inputs
- Result display with styling based on approval/rejection

### static/style.css
- Modern styling with gradient background
- Responsive grid layout for form
- Smooth animations and transitions
- Mobile-friendly breakpoints

### static/script.js
- Page navigation functions
- Form handling and validation
- API communication with Flask backend
- Dynamic result display and suggestion rendering

## How It Works

1. User starts on the Welcome page
2. Clicks "Go to Prediction" to access the prediction form
3. Fills in loan details
4. Submits the form via the "Predict Loan Status" button
5. Flask processes the input and makes a prediction
6. Results are displayed with:
   - **Approved**: Congratulations message
   - **Rejected**: Personalized improvement suggestions

## API Endpoint

### POST /api/predict

**Request Body:**
```json
{
    "no_of_dependents": 2,
    "education": " Graduate",
    "self_employed": " No",
    "income_annum": 50000,
    "loan_amount": 100000,
    "loan_term": 5,
    "cibil_score": 750,
    "residential_assets_value": 200000,
    "commercial_assets_value": 0,
    "luxury_assets_value": 50000,
    "bank_asset_value": 25000
}
```

**Response (Success):**
```json
{
    "success": true,
    "loan_status": "Approved",
    "suggestions": []
}
```

**Response (Rejected):**
```json
{
    "success": true,
    "loan_status": "Rejected",
    "suggestions": [
        "Improve your CIBIL Score: ...",
        "Increase your Assets: ..."
    ]
}
```

## Browser Compatibility

- Chrome/Chromium (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers

## Notes

- The model file `decision_tree_model.pkl` must be in the same directory as `flask_app.py`
- The application uses Flask's development server (not suitable for production)
- For production deployment, use a WSGI server like Gunicorn or uWSGI
- The CSS uses a fixed port (5000), modify in `flask_app.py` if needed

## Troubleshooting

**Model not found error:**
- Ensure `decision_tree_model.pkl` is in the project directory

**Port already in use:**
- Change the port in `flask_app.py`: `app.run(debug=True, port=5001)`

**Template not found error:**
- Ensure `templates` folder exists with `index.html` inside
- Ensure `static` folder exists with `style.css` and `script.js`

## Future Enhancements

- Add data persistence (save past predictions)
- Implement user authentication
- Add data visualization and charts
- Deploy to cloud platforms (Heroku, AWS, Google Cloud)
- Add API documentation (Swagger/OpenAPI)
