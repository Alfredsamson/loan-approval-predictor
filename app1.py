
import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

# Load the trained model (Decision Tree as it seems to have the highest accuracy based on the plot)
# Ensure 'decision_tree_model.pkl' is available in the environment
# or adjust the path.
try:
    model = joblib.load('decision_tree_model.pkl')
except FileNotFoundError:
    st.error("Model file 'decision_tree_model.pkl' not found. Please train and save the model first.")
    st.stop()

# Load the label encoders fitted during the training phase
# We need to recreate and fit the label encoders as done in the training script
try:
    # Recreate dummy data to fit label encoders for consistent transformation
    # In a real application, you'd save the fitted encoders
    # or the mapping
    dummy_df = pd.DataFrame({
        ' education': [' Graduate', ' Not Graduate', ' Graduate'],
        ' self_employed': [' Yes', ' No', ' Yes'],
        ' loan_status': [' Approved', ' Rejected', ' Approved']
    })
    le_education = LabelEncoder()
    le_self_employed = LabelEncoder()
    le_loan_status = LabelEncoder()  # Although not used for prediction input, good practice to have

    le_education.fit(dummy_df[' education'])
    le_self_employed.fit(dummy_df[' self_employed'])
    le_loan_status.fit(dummy_df[' loan_status'])

except Exception as e:
    st.error(f"Error initializing label encoders: {e}")
    st.stop()



# Function to create the welcome page
def welcome_page():
    st.markdown(
        """
        <style>
        .main {
            background-color: #E0F7FA; /* Light Cyan */
            padding: 20px;
            border-radius: 10px;
        }
        .stApp {
            background-color: #E0F7FA; /* Light Cyan background for the entire app */
        }
        h1 {
            color: #00796B; /* Teal */
            text-align: center;
        }
        .stMarkdown p {
            font-size: 1.1em;
            color: #004D40; /* Dark Teal */
        }
        .stButton button {
            background-color: #00796B;
            color: white;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 8px;
            border: none;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.title("Welcome to the Loan Approval Predictor")
    st.markdown("""
    <p>This application helps you predict the likelihood of your loan application being approved
    based on your personal and financial details.
    Get valuable insights and suggestions
    to improve your chances of loan approval.</p>
    """, unsafe_allow_html=True)
    st.image(
        "https://img.freepik.com/free-vector/financial-profit-concept-illustration_114360-2747.jpg",
        use_column_width=True
    )  # Replace with a relevant image URL

    if st.button("Go to Prediction"):
        st.session_state['page'] = 'prediction'
        st.rerun()  # Changed from st.experimental_rerun()

# Function to create the prediction page
def prediction_page():
    st.markdown(
        """
        <style>
        .main {
            background-color: #E0F7FA; /* Light Cyan */
            padding: 20px;
            border-radius: 10px;
        }
         .stApp {
            background-color: #E0F7FA; /* Light Cyan background for the entire app */
        }
        h1 {
            color: #00796B; /* Teal */
            text-align: center;
        }
        .stMarkdown p {
            font-size: 1.1em;
            color: #004D40; /* Dark Teal */
        }
        .stTextInput label, .stSelectbox label, .stSlider label {
            font-weight: bold;
            color: #004D40; /* Dark Teal */
        }
         .stButton button {
            background-color: #00796B;
            color: white;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 8px;
            border: none;
        }
        .prediction-result {
            margin-top: 20px;
            padding: 15px;
            border-radius: 8px;
            font-size: 1.2em;
            text-align: center;
        }
        .approved {
            background-color: #A5D6A7; /* Light Green */
            color: #1B5E20; /* Dark Green */
        }
        .rejected {
            background-color: #FFCDD2; /* Light Red */
            color: #B71C1C; /* Dark Red */
        }
        .suggestion {
            margin-top: 15px;
            padding: 10px;
            background-color: #B2EBF2; /* Light Blue */
            border-left: 5px solid #00BCD4; /* Cyan */
            border-radius: 5px;
            color: #004D40; /* Dark Teal */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Loan Prediction")

    st.header("Enter your details:")

    # Input fields
    no_of_dependents = st.slider("Number of Dependents", 0, 10, 0)
    education = st.selectbox("Education", [' Graduate', ' Not Graduate'])
    self_employed = st.selectbox("Self Employed", [' Yes', ' No'])
    income_annum = st.number_input("Annual Income (in $) ", min_value=0.0, format="%f")
    loan_amount = st.number_input("Loan Amount (in $)", min_value=0.0, format="%f")
    loan_term = st.number_input("Loan Term (in years)", min_value=1, format="%d")
    cibil_score = st.number_input("CIBIL Score", min_value=300, max_value=900, value=700)
    residential_assets_value = st.number_input("Residential Assets Value (in $)", min_value=0.0, format="%f")
    commercial_assets_value = st.number_input("Commercial Assets Value (in $)", min_value=0.0, format="%f")
    luxury_assets_value = st.number_input("Luxury Assets Value (in $)", min_value=0.0, format="%f")
    bank_asset_value = st.number_input("Bank Asset Value (in $)", min_value=0.0, format="%f")


    if st.button("Predict Loan Status"):
        try:
            # Preprocess input data
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

            # Predict
            prediction = model.predict(input_data)

            loan_status = "Approved" if prediction[0] == 0 else "Rejected" # Map back to original labels

            st.subheader("Prediction Result:")
            if loan_status == "Approved":
                status_text = f"Loan Status: {loan_status} 🎉"
                st.markdown(f'<div class="prediction-result approved">{status_text}</div>', unsafe_allow_html=True)
                st.markdown("<p>Congratulations! Your loan is likely to be approved.</p>", unsafe_allow_html=True)
            else:
                status_text = f"Loan Status: {loan_status} 😞"
                st.markdown(f'<div class="prediction-result rejected">{status_text}</div>', unsafe_allow_html=True)
                st.markdown("<p>Your loan application is likely to be rejected. "
                            "Here are some suggestions to improve your chances:</p>", unsafe_allow_html=True)

                st.markdown('<div class="suggestion">', unsafe_allow_html=True)
                if cibil_score < 700:
                    st.write("- **Improve your CIBIL Score:** Pay bills on time, reduce credit utilization, and avoid opening too many new credit accounts.")
                monthly_installment = loan_amount / (loan_term * 12)
                if income_annum < monthly_installment * 2:  # Simple heuristic: income should be at least twice the monthly installment
                     st.write("- **Increase your Income:** Consider increasing your income or applying for a lower loan amount.")
                total_assets = (residential_assets_value + commercial_assets_value +
                                luxury_assets_value + bank_asset_value)
                if total_assets < loan_amount * 1.5:  # Simple heuristic: assets should be more than loan amount
                    st.write("- **Increase your Assets:** Building up your assets can demonstrate financial stability.")
                st.write("- **Reduce Existing Debt:** Lowering your existing debt "
                         "can improve your debt-to-income ratio.")
                st.write("- **Consider a Co-applicant:** Applying with a co-applicant with a good credit history "
                         "and stable income can increase approval chances.")
                st.write("- **Review Loan Terms:** Explore different loan products and terms that might be a better fit "
                         "for your financial situation.")
                st.markdown('</div>', unsafe_allow_html=True)


        except Exception as e:
            error_msg = f"An error occurred during prediction: {e}"
            st.error(error_msg)

    if st.button("Back to Welcome"):
        st.session_state['page'] = 'welcome'
        st.rerun()  # Changed from st.experimental_rerun()


# Main app logic
if 'page' not in st.session_state:
    st.session_state['page'] = 'welcome'

if st.session_state['page'] == 'welcome':
    welcome_page()
elif st.session_state['page'] == 'prediction':
    prediction_page()

