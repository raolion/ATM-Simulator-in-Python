
# ATM-Simulator-in-Python

A simple ATM simulator implemented in Python with multi-user support.

## 📜 Description

This program simulates a basic ATM system that supports multiple users. Each user can create an account, deposit and withdraw funds, check their balance, and view their transaction history. The program uses the `Decimal` class for precise financial calculations and includes robust error handling for invalid inputs.

## ✨ Features

- **👤 Multi-User Support**: Create and manage multiple users with unique names and balances.
- **💳 Check Balance**: View the current balance of any user.
- **💰 Deposit Money**: Deposit funds into a user's account (positive amounts only).
- **💸 Withdraw Money**: Withdraw funds from a user's account (positive amounts, with insufficient funds check).
- **📜 Transaction History**: View the history of deposits and withdrawals for any user.
- **🖥️ Interactive Menu**: User-friendly menu-driven interface for easy navigation.
- **❌ Error Handling**: Handles invalid inputs and edge cases gracefully.

## ⚒️ How to Use

1. Make sure you have Python 3 installed.
2. Clone the repository:
   ```bash
   git clone https://github.com/raolion/ATM-Simulator-in-Python.git
   ```
3. Navigate to the project folder:
   ```bash
   cd ATM-Simulator-in-Python
   ```
4. Run the program:
   - For the original version:
     ```bash
     python ATM.py
     ```
   - For the new version with multi-user support:
     ```bash
     python ATM_2_0.py
     ```

## 🚀 New in Version 2.0

- **Multi-User System**: Now supports multiple users with unique accounts.
- **Transaction History**: Each user has a record of their deposits and withdrawals.
- **Improved Error Handling**: Better handling of invalid inputs and edge cases.
- **Enhanced User Interface**: More intuitive menu options and feedback.

## 📂 File Structure

- **ATM.py**: The original version of the ATM simulator (single-user).
- **ATM_2_0.py**: The updated version with multi-user support and transaction history.
