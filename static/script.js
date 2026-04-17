// Page navigation functions
function goToPrediction() {
    document.getElementById('welcomePage').classList.remove('active');
    document.getElementById('predictionPage').classList.add('active');
    // Reset form
    document.getElementById('predictionForm').reset();
    document.getElementById('dependentsValue').textContent = '0';
    document.getElementById('resultSection').classList.add('hidden');
    document.getElementById('loadingIndicator').classList.add('hidden');
}

function goToWelcome() {
    document.getElementById('predictionPage').classList.remove('active');
    document.getElementById('welcomePage').classList.add('active');
    // Reset result section
    document.getElementById('resultSection').classList.add('hidden');
    document.getElementById('loadingIndicator').classList.add('hidden');
}

// Update dependents slider display
document.addEventListener('DOMContentLoaded', function() {
    const slider = document.getElementById('no_of_dependents');
    const valueDisplay = document.getElementById('dependentsValue');

    if (slider) {
        slider.addEventListener('input', function() {
            valueDisplay.textContent = this.value;
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
            residential_assets_value: document.getElementById('residential_assets_value').value,
            commercial_assets_value: document.getElementById('commercial_assets_value').value,
            luxury_assets_value: document.getElementById('luxury_assets_value').value,
            bank_asset_value: document.getElementById('bank_asset_value').value
        };

        // Validate required fields
        if (!formData.income_annum || !formData.loan_amount || !formData.loan_term) {
            alert('Please fill in all required fields (Income, Loan Amount, and Loan Term)');
            return;
        }

        // Show loading indicator
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
    const resultText = document.getElementById('resultText');
    const successMessage = document.getElementById('successMessage');
    const suggestionsSection = document.getElementById('suggestionsSection');
    const suggestionsList = document.getElementById('suggestionsList');

    // Clear previous results
    resultBox.className = 'result-box';
    suggestionsList.innerHTML = '';

    if (loanStatus === 'Approved') {
        // Show approved result
        resultBox.classList.add('approved');
        resultText.innerHTML = 'Loan Status: <strong>Approved</strong> 🎉';
        successMessage.classList.remove('hidden');
        suggestionsSection.classList.add('hidden');
    } else {
        // Show rejected result
        resultBox.classList.add('rejected');
        resultText.innerHTML = 'Loan Status: <strong>Rejected</strong> 😞';
        successMessage.classList.add('hidden');

        // Display suggestions
        if (suggestions && suggestions.length > 0) {
            suggestionsSection.classList.remove('hidden');
            suggestions.forEach(suggestion => {
                const suggestionItem = document.createElement('div');
                suggestionItem.className = 'suggestion-item';
                suggestionItem.textContent = suggestion;
                suggestionsList.appendChild(suggestionItem);
            });
        } else {
            suggestionsSection.classList.add('hidden');
        }
    }

    // Show result section
    resultSection.classList.remove('hidden');

    // Scroll to result
    setTimeout(() => {
        resultSection.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }, 100);
}

// Allow Enter key to submit form
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('predictionForm');
    if (form) {
        form.addEventListener('keypress', function(event) {
            if (event.key === 'Enter') {
                event.preventDefault();
                predictLoanStatus();
            }
        });
    }
});
