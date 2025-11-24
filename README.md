# VITyarthi Banking Management System

## Project Title
**VITyarthi Banking Management System**

A Python-based command-line banking application that simulates various banking operations and financial services.

## Overview

VITyarthi is an interactive banking management system designed to help users manage different types of bank accounts and loan services. The system collects user information and provides financial calculations for interest earned and payable amounts across multiple account types. This project demonstrates fundamental banking concepts including simple interest, compound interest, and loan management with dynamic interest rates based on account type, principal amount, and customer demographics.

The application is ideal for understanding banking operations, financial calculations, and implementing conditional logic in Python.

## Features

- **User Information Management**: Collects and validates customer details (name, age, gender, address, mobile number)
- **Savings Account**: Tracks savings accounts with 4% annual interest rate and transaction monitoring capability
- **Recurring Deposit Account**: Calculates compound interest with tiered interest rates (4%-7%) based on principal amount
- **Fixed Deposit (FD) Account**: Computes simple interest with age-based interest rate variations (higher rates for senior citizens)
- **Loan Services**: Offers three loan categories:
  - Property Loans (7.5% interest rate)
  - Education Loans (4% interest rate)
  - Business Loans (6% interest rate)
- **Mobile Number Validation**: Ensures users enter a valid 10-digit mobile number
- **Transaction Processing**: For savings accounts, allows users to record transactions and adjust principal amounts
- **Interest Calculation**: Automatically calculates interest based on account type and parameters
- **Personalized Output**: Displays final amount summaries with customer information

## Technologies/Tools Used

- **Language**: Python 3.x
- **Paradigm**: Procedural Programming
- **Key Concepts**: 
  - Conditional statements (if/elif/else)
  - While loops
  - String manipulation
  - Input/Output operations
  - Mathematical calculations
- **No External Libraries**: Pure Python implementation with built-in functions

## Installation & Setup

### Prerequisites
- Python 3.6 or higher installed on your system
- A terminal or command prompt
- Basic knowledge of running Python scripts

### Steps to Install & Run

1. **Download the Project**
   ```bash
   # Clone or download the project file
   git clone <repository-url>
   cd VITyarthi-Banking-System
   ```

2. **Verify Python Installation**
   ```bash
   python --version
   # or
   python3 --version
   ```

3. **Run the Application**
   ```bash
   python VITyarthi-project.py
   ```
   or
   ```bash
   python3 VITyarthi-project.py
   ```

4. **Follow the Interactive Prompts**
   - Enter your personal information when prompted
   - Select the type of account or service you want
   - Provide required financial details
   - View calculated results

## Instructions for Testing

### Test Case 1: Savings Account
**Objective**: Verify savings account interest calculation

**Steps**:
1. Run the program
2. Enter personal details:
   - Name: `John Doe`
   - Age: `35`
   - Gender: `Male`
   - Address: `123 Main Street`
   - Mobile: `9876543210`
3. Select option: `1` (Savings Account)
4. Enter principal amount: `10000`
5. Enter time period: `2`
6. When prompted for transactions:
   - Enter `YES` for transactions
   - Enter transaction value: `5000`
   - Select `increase` to add funds
7. **Expected Output**: Final amount and interest earned should be calculated

### Test Case 2: Recurring Deposit Account
**Objective**: Verify compound interest calculation with tiered rates

**Steps**:
1. Run the program
2. Enter personal details (as above)
3. Select option: `2` (Recurring Deposit Account)
4. Enter principal amount: `75000` (to test 4.5% tier)
5. Enter time period: `3`
6. **Expected Output**: Compound interest calculated and displayed with 4.5% rate

### Test Case 3: Fixed Deposit Account (Senior Citizen)
**Objective**: Verify FD interest calculation with senior citizen premium

**Steps**:
1. Run the program
2. Enter personal details with:
   - Age: `65` (to trigger senior citizen rates)
3. Select option: `3` (FD Account)
4. Enter principal amount: `250000`
5. Enter time period: `5`
6. **Expected Output**: Should show higher interest rate (7%) compared to younger customers

### Test Case 4: Loan Services
**Objective**: Verify loan calculation and monthly payment breakdown

**Steps**:
1. Run the program
2. Enter personal details (as above)
3. Select option: `4` (Loans)
4. Enter monthly income: `50000`
5. Enter mortgage type: `Gold`
6. Enter amount needed: `500000`
7. Enter time period: `5`
8. Select option: `2` (Education Loan)
9. **Expected Output**: Should display:
   - Total interest at 4% rate
   - Total payable amount
   - Monthly installment amount

### Test Case 5: Input Validation
**Objective**: Verify error handling

**Steps**:
1. Run the program
2. For mobile number, enter: `123` (invalid - less than 10 digits)
3. **Expected Output**: "Invalid number" message and prompt to re-enter

### Test Case 6: Negative Input Handling
**Objective**: Verify handling of negative amounts

**Steps**:
1. Run the program
2. Select option: `2` (Recurring Deposit)
3. Enter principal amount: `-5000`
4. **Expected Output**: "Invalid input" message displayed

## Usage Examples

### Example 1: Savings Account with Transaction
```
Enter your name : Alice Kumar
Enter your age : 28
Enter your gender : Female
Enter your address : 456 Oak Avenue
Enter your mobile number : 9123456789
Enter 1 for Savings Account , 2 for Recurring Deposit Account , 3 for FD Account and 4 for loans : 1
Enter the principal amount : 50000
Enter the time period : 2
Transactions made in the or not : YES or NO
: YES
Enter the net value of the transactions : 10000
Principal amount increased or decreased : increase
```

### Example 2: Property Loan Application
```
Enter your name : Rajesh Singh
Enter your age : 45
Enter your gender : Male
Enter your address : 789 Pine Road
Enter your mobile number : 9876543210
Enter 1 for property loans , 2 for Education Loans and 3 for Business related loans : 1
Enter your monthly income : 75000
Enter what will you keep for mortgage : Residential Property
Enter the amount you need : 2000000
Enter the time period for which the loan is needed : 10
```

## Known Limitations & Future Improvements

1. **Current Limitations**:
   - String comparisons for transaction input may be case-sensitive
   - No persistent data storage (data lost after program termination)
   - Limited error handling for unexpected input types
   - Monthly payment calculation for loans assumes equal installments

2. **Suggested Improvements**:
   - Implement a database for storing customer and transaction records
   - Add user authentication and account management
   - Enhance input validation with try-except blocks
   - Create a GUI using Tkinter or PyQt
   - Add more account types and investment options
   - Implement transaction history and statement generation
   - Add file export functionality for account statements

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `python: command not found` | Install Python or use `python3` instead |
| `IndentationError` | Ensure the Python file is properly formatted (no tab/space mixing) |
| Mobile number keeps asking for input | Enter exactly 10 digits without any special characters |
| Interest calculation seems wrong | Verify you're entering correct time period in years |
| Program exits unexpectedly | Check for invalid data types (use numbers for numeric inputs) |

## Notes for Developers

- The code uses simple interest calculations for Savings and FD accounts
- Recurring Deposit uses compound interest formula: CI = P(1 + r/100)^t - P
- Interest rates are hardcoded; consider parameterizing them for flexibility
- The variable naming could be improved for better code readability (e.g., `choise` → `choice`)
- Consider refactoring repetitive code into functions for better maintainability

## License

This project is open-source and available for educational purposes.

## Author/Credit

VITyarthi Banking Management System - Educational Project

---

**Last Updated**: November 2025
