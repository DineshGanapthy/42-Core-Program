from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, EmailStr, Field

class AccountPurpose(str, Enum):
    RENOVATION = "House Renovation"
    HOLIDAY = "Holiday"
    SETTLEMENT = "Settlement of Another Loan/Credit Card"
    MEDICAL = "Medical Fee"
    EDUCATION = "Education"
    OTHERS = "Others"

class EmploymentCategory(str, Enum):
    SELF_EMPLOYED = "Self-Employed"
    PRIVATE_EMPLOYEE = "Private Employee"
    GOVERNMENT_EMPLOYEE = "Government Employee"
    UNEMPLOYED = "Unemployed"
    RETIREE = "Retiree"

class DebtItem(BaseModel):
    type_of_loan: str
    bank: str
    loan_amount: float
    monthly_installment: float

class LoanApplication(BaseModel):
    # Purpose
    purpose: AccountPurpose
    purpose_others: Optional[str] = None

    # Loan Details
    loan_amount: float  # Changed to float for proper validation
    tenure_months: int

    # Personal Details
    full_name: str
    ic_no: str
    dob: str # DD/MM/YY
    mobile_no: str
    email: EmailStr
    marital_status: str  # Single, Married, Widowed, Divorced
    gender: str  # Male, Female
    education: str  # Highest education level
    dependents: int  # Number of dependents

    # Employment
    employment_type: EmploymentCategory
    is_contracted: bool = False # Applies to Private/Government
    occupation: Optional[str] = None  # Optional for Unemployed/Retiree
    years_of_employment: Optional[float] = None  # Optional for Unemployed/Retiree
    income: Optional[float] = None  # Changed from annual_income
    income_type: Optional[str] = None  # "annual" or "monthly"

    # Declaration of Debt
    debts: List[DebtItem] = []

