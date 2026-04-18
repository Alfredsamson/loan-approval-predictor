// Page navigation functions
function goToPrediction() {
    document.getElementById('landingPage').classList.remove('active');
    document.getElementById('predictionPage').classList.add('active');
    // Reset form and results
    document.getElementById('predictionForm').reset();
    document.getElementById('resultSection').classList.add('hidden');
    document.getElementById('loadingIndicator').classList.add('hidden');
}

function goToLanding() {
    document.getElementById('predictionPage').classList.remove('active');
    document.getElementById('landingPage').classList.add('active');
    // Reset result section
    document.getElementById('resultSection').classList.add('hidden');
    document.getElementById('loadingIndicator').classList.add('hidden');
}

// Form submission handler
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('predictionForm');
    if (form) {
        form.addEventListener('submit', function(event) {
            event.preventDefault();
            predictLoanStatus();
        });
    }
});

// Prediction function
async function predictLoanStatus() {
    try {
        // Get form values
        const formData = {
            no_of_dependents: document.getElementById('no_of_dependents').value,
            education: document.getElementById('education').value,
            self_employed: document.getElementById('self_employed').value,
            income_annum: document.getElementById('income_annum').value,
            loan_amount: document.getElementById('loan_amount').value,
            loan_term: document.getElementById('loan_term').value,
            cibil_score: document.getElementById('cibil_score').value,
            // Set default values for removed fields
            residential_assets_value: 0,
            commercial_assets_value: 0,
            luxury_assets_value: 0,
            bank_asset_value: 0
        };

        // Validate required fields
        if (!formData.income_annum || !formData.loan_amount || !formData.loan_term) {
            alert('Please fill in all required fields (Income, Loan Amount, and Loan Term)');
            return;
        }

        // Show loading indicator and hide results
        document.getElementById('loadingIndicator').classList.remove('hidden');
        document.getElementById('resultSection').classList.add('hidden');

        // Make API request
        const response = await fetch('/api/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });

        const result = await response.json();

        // Hide loading indicator
        document.getElementById('loadingIndicator').classList.add('hidden');

        if (result.success) {
            displayResult(result.loan_status, result.suggestions);
        } else {
            alert('Error: ' + result.error);
        }
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('loadingIndicator').classList.add('hidden');
        alert('An error occurred while processing your request: ' + error.message);
    }
}

// Display prediction result
function displayResult(loanStatus, suggestions) {
    const resultSection = document.getElementById('resultSection');
    const resultBox = document.getElementById('resultBox');
    const resultIcon = document.getElementById('resultIcon');
    const resultTitle = document.getElementById('resultTitle');
    const resultMessage = document.getElementById('resultMessage');
    const suggestionsSection = document.getElementById('suggestionsSection');
    const suggestionsList = document.getElementById('suggestionsList');

    // Clear previous results
    resultBox.className = 'result-box';
    suggestionsList.innerHTML = '';

    if (loanStatus === 'Approved') {
        // Show approved result
        resultBox.classList.add('approved');
        resultIcon.innerHTML = '✅';
        resultTitle.textContent = 'Loan Approved!';
        resultMessage.textContent = 'Congratulations! Your loan application is likely to be approved based on the provided information.';
        suggestionsSection.classList.add('hidden');
    } else {
        // Show rejected result
        resultBox.classList.add('rejected');
        resultIcon.innerHTML = '❌';
        resultTitle.textContent = 'Loan Rejected';
        resultMessage.textContent = 'Your loan application is likely to be rejected. Here are some suggestions to improve your chances:';

        // Display suggestions
        if (suggestions && suggestions.length > 0) {
            suggestionsSection.classList.remove('hidden');
            suggestions.forEach(suggestion => {
                const suggestionItem = document.createElement('li');
                suggestionItem.textContent = suggestion;
                suggestionsList.appendChild(suggestionItem);
            });
        } else {
            suggestionsSection.classList.add('hidden');
        }
    }

    // Show result section and scroll to it
    resultSection.classList.remove('hidden');
    setTimeout(() => {
        resultSection.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }, 100);
}
