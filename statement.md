Problem Statement
In the early stages of learning programming, students often struggle to connect theoretical concepts like conditional logic, loops, and mathematical operations with real-world applications. The problem is to create a practical, self-contained console application that is easy to understand, relevant to daily life, and effective for demonstrating these core programming structures in a functional manner. Specifically, the project addresses the need for a simplified simulation environment that models common banking services to calculate interest and final amounts based on user inputs and predefined business rules (e.g., variable interest rates based on age or principal).

● Scope of the Project
The scope of the VITyarthi Banking Console Application is strictly limited to the following functionalities:

Input and Output: Gathering essential customer demographic and financial data, and presenting clear, calculated results back to the user via the console.

Four Service Modules: Implementing the logic for a Savings Account, a Recurring Deposit (RD) Account, a Fixed Deposit (FD) Account, and a Loan Service.

Core Calculations: Performing Simple Interest (SI) and Compound Interest (CI) calculations based on established financial formulas.

Business Logic Implementation: Applying conditional rules (e.g., if/elif/else) to determine variable interest rates based on criteria like principal amount, time period, customer age (for FD), and loan purpose.

Data Persistence: Out of scope. The application does not save, store, or retrieve customer data or transaction history to any external file or database. All data is volatile and exists only during the current runtime session.

Real-time Transactions: Out of scope. The application does not connect to any real banking APIs or process actual financial transactions.

● Target Users
The primary target users for this project are:

College Students / Beginners in Programming: Individuals learning Python who need a tangible, manageable project to practice control flow (if/else), loops (while), and basic arithmetic operations.

Instructors/Tutors: Educators seeking a straightforward, working example to illustrate how programming concepts can model simple business logic and financial calculations.

General Users: Anyone interested in performing quick, simulated calculations for bank deposits (Savings, FD, RD) or loans without using a complex spreadsheet or a formal banking portal.

● High-Level Features
User Registration Flow: Collects basic identifying information from the customer.

Input Validation: Ensures the mobile number meets a basic length requirement before proceeding.

Menu System: Provides a clear numerical choice selection for the four banking services.

Interest Rate Tiering: Implements rate changes dynamically for FD and RD based on specific criteria (age/principal).

Savings Account Transaction Simulation: Allows the principal to be manually adjusted within the simulation to test the impact of deposits or withdrawals.

Amortization Detail: For loans, provides the final total payment amount and the estimated per-month payment.
