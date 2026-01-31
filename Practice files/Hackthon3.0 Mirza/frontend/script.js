document.addEventListener('DOMContentLoaded', () => {
    // === DOM Elements ===
    const form = document.getElementById('loanForm');
    const formMessages = document.getElementById('formMessages');
    const purposeSelect = document.getElementById('purposeSelect');
    const purposeOthersInput = document.getElementById('purposeOthersInput');
    const amountRadios = document.getElementsByName('loanAmount');
    const amountOthersInput = document.getElementById('amountOthersInput');
    const debtTableBody = document.getElementById('debtTableBody');
    const addDebtRowBtn = document.getElementById('addDebtRowBtn');
    const empTypeSelect = document.getElementById('empType');
    const employmentDetails = document.getElementById('employmentDetails');
    const incomeTypeRadios = document.getElementsByName('incomeType');
    const incomeLabel = document.getElementById('incomeLabel');

    // === Helper Functions ===
    function preventNegative(e) {
        if (e.key === '-' || e.key === 'e') {
            e.preventDefault();
        }
    }

    function clearErrors() {
        document.querySelectorAll('.error-message').forEach(el => el.remove());
        document.querySelectorAll('.is-invalid').forEach(el => el.classList.remove('is-invalid'));
        formMessages.innerHTML = '';
    }

    function showError(message) {
        formMessages.innerHTML = `<div class="error-banner">${message}</div>`;
        formMessages.scrollIntoView({ behavior: 'smooth' });
    }

    // === Purpose Others Logic ===
    purposeSelect.addEventListener('change', () => {
        if (purposeSelect.value === 'Others') {
            purposeOthersInput.classList.add('active');
            purposeOthersInput.required = true;
        } else {
            purposeOthersInput.classList.remove('active');
            purposeOthersInput.required = false;
            purposeOthersInput.value = '';
        }
    });

    // === Loan Amount Others Logic ===
    function toggleAmountOthers() {
        const othersRadio = document.getElementById('amountOthersRadio');
        if (othersRadio && othersRadio.checked) {
            amountOthersInput.required = true;
        } else {
            amountOthersInput.required = false;
            amountOthersInput.value = '';
        }
    }

    amountRadios.forEach(radio => radio.addEventListener('change', toggleAmountOthers));

    // === Employment Type Visibility Logic ===
    function toggleEmploymentDetails() {
        const val = empTypeSelect.value;
        // Show details only for employed types (not Unemployed, Retiree, or unselected)
        const isEmployed = val && val !== 'Unemployed' && val !== 'Retiree';
        employmentDetails.style.display = isEmployed ? 'grid' : 'none';
    }

    empTypeSelect.addEventListener('change', toggleEmploymentDetails);
    toggleEmploymentDetails(); // Initial state (hidden by default)

    // === Income Label Toggle ===
    function updateIncomeLabel() {
        const checked = document.querySelector('input[name="incomeType"]:checked');
        const empVal = empTypeSelect.value;
        const isUnemployedOrRetiree = (empVal === 'Unemployed' || empVal === 'Retiree');

        if (checked && checked.value === 'monthly') {
            incomeLabel.textContent = isUnemployedOrRetiree ? 'Monthly Income/Funds (RM)' : 'Monthly Income (RM)';
        } else {
            incomeLabel.textContent = isUnemployedOrRetiree ? 'Annual Income/Funds (RM)' : 'Annual Income (RM)';
        }
    }

    incomeTypeRadios.forEach(radio => radio.addEventListener('change', updateIncomeLabel));
    empTypeSelect.addEventListener('change', updateIncomeLabel); // Also update on employment change

    // === Dynamic Debt Table ===
    function addDebtRow() {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td><input type="text" class="debt-type" placeholder="e.g. Car Loan"></td>
            <td><input type="text" class="debt-bank" placeholder="e.g. Maybank"></td>
            <td><input type="number" class="debt-amount" placeholder="0" min="0"></td>
            <td><input type="number" class="debt-monthly" placeholder="0" min="0"></td>
            <td><button type="button" class="btn btn-danger remove-btn">Remove</button></td>
        `;
        row.querySelector('.remove-btn').addEventListener('click', () => row.remove());
        debtTableBody.appendChild(row);
    }

    addDebtRowBtn.addEventListener('click', addDebtRow);
    addDebtRow(); // Add initial row

    // === Touched State for Validation ===
    form.addEventListener('focusout', (e) => {
        if (e.target.tagName === 'INPUT' || e.target.tagName === 'SELECT') {
            e.target.classList.add('touched');
        }
    });

    form.addEventListener('change', (e) => {
        if (e.target.tagName === 'SELECT' || e.target.type === 'date') {
            e.target.classList.add('touched');
        }
    });

    // === Prevent Negative Numbers ===
    form.addEventListener('keydown', (e) => {
        if (e.target.type === 'number') {
            preventNegative(e);
        }
    });

    // === Form Submission ===
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        clearErrors();

        // Mark all as touched for visual feedback
        form.querySelectorAll('input, select').forEach(el => el.classList.add('touched'));

        // Gather Data
        const formData = new FormData(form);
        const data = {};

        // Purpose
        data.purpose = formData.get('purpose');
        if (data.purpose === 'Others') {
            data.purpose_others = purposeOthersInput.value;
        }

        // Loan Amount
        const amountVal = formData.get('loanAmount');
        if (amountVal === 'Others') {
            data.loan_amount = parseFloat(amountOthersInput.value);
        } else {
            data.loan_amount = parseFloat(amountVal);
        }

        data.tenure_months = parseInt(formData.get('tenure'));

        // Personal
        data.full_name = formData.get('fullName');
        data.ic_no = formData.get('icNo');
        data.dob = formData.get('dob');
        data.mobile_no = formData.get('mobileNo');
        data.email = formData.get('email');
        data.marital_status = formData.get('maritalStatus');
        data.gender = formData.get('gender');
        data.education = formData.get('education');
        data.dependents = parseInt(formData.get('dependents')) || 0;

        // Employment
        const empValue = formData.get('empType');
        data.is_contracted = empValue.includes('(Contracted)');
        data.employment_type = empValue.replace(' (Contracted)', '').replace(' (Permanent)', '');

        // Only include occupation/years if not Unemployed/Retiree
        if (empValue !== 'Unemployed' && empValue !== 'Retiree') {
            data.occupation = formData.get('occupation');
            data.years_of_employment = parseFloat(formData.get('yearsEmployment')) || null;
        }

        // Income is always collected
        data.income = parseFloat(formData.get('income')) || null;
        data.income_type = formData.get('incomeType');

        // Debts
        const rows = debtTableBody.querySelectorAll('tr');
        data.debts = [];
        rows.forEach(row => {
            const type = row.querySelector('.debt-type').value.trim();
            const bank = row.querySelector('.debt-bank').value.trim();
            const amount = row.querySelector('.debt-amount').value;
            const monthly = row.querySelector('.debt-monthly').value;

            if (type && bank && amount && monthly) {
                data.debts.push({
                    type_of_loan: type,
                    bank: bank,
                    loan_amount: parseFloat(amount),
                    monthly_installment: parseFloat(monthly)
                });
            }
        });

        // Submit to Backend
        try {
            const response = await fetch('/api/submit', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });

            const result = await response.json();

            if (response.ok) {
                // Download JSON file
                const jsonStr = JSON.stringify(result.data, null, 2);
                const blob = new Blob([jsonStr], { type: 'application/json' });
                const url = URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = 'loan_application.json';
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
                URL.revokeObjectURL(url);

                // Reset form
                form.reset();
                form.querySelectorAll('.touched').forEach(el => el.classList.remove('touched'));
                purposeOthersInput.classList.remove('active');
                amountOthersInput.classList.remove('active');
                debtTableBody.innerHTML = '';
                addDebtRow();

                formMessages.innerHTML = '<div class="error-banner" style="background:#D4EDDA;border-color:#28A745;color:#155724;">Application submitted successfully! Your JSON file has been downloaded.</div>';
            } else {
                // Handle backend validation errors
                if (result.detail && Array.isArray(result.detail)) {
                    const fieldMap = {
                        'full_name': 'fullName', 'ic_no': 'icNo', 'dob': 'dob',
                        'mobile_no': 'mobileNo', 'email': 'email', 'loan_amount': 'loanAmount',
                        'tenure_months': 'tenure', 'purpose': 'purpose', 'employment_type': 'empType',
                        'occupation': 'occupation', 'years_of_employment': 'yearsEmployment',
                        'annual_income': 'annualIncome'
                    };

                    result.detail.forEach(err => {
                        const fieldName = err.loc[err.loc.length - 1];
                        const inputName = fieldMap[fieldName] || fieldName;
                        const input = form.querySelector(`[name="${inputName}"]`);

                        if (input) {
                            input.classList.add('is-invalid');
                            const errorDiv = document.createElement('div');
                            errorDiv.className = 'error-message';
                            errorDiv.innerText = err.msg;
                            input.closest('.form-group')?.appendChild(errorDiv);
                        }
                    });

                    showError('Please correct the errors highlighted below.');
                } else {
                    showError('Submission failed: ' + JSON.stringify(result));
                }
            }
        } catch (error) {
            console.error('Network Error:', error);
            showError('Network error. Please check if the backend is running.');
        }
    });
});
