ATM Simulator in Python (Multi-User Support)

A Python-based ATM simulator that supports multiple users, allowing them to create accounts, deposit and withdraw funds, check balances, and view transaction history.
📜 Description

This program simulates a basic ATM system with support for multiple users. Each user can create an account with an initial balance, deposit and withdraw funds, check their current balance, and view their transaction history. The program uses the Decimal class for precise financial calculations and includes robust error handling for invalid inputs.
✨ Features

    👤 Multi-User Support: Create and manage multiple users with unique names and balances.

    💳 Check Balance: View the current balance of any user.

    💰 Deposit Money: Deposit funds into a user's account (positive amounts only).

    💸 Withdraw Money: Withdraw funds from a user's account (positive amounts, with insufficient funds check).

    📜 Transaction History: View the history of deposits and withdrawals for any user.

    🖥️ Interactive Menu: User-friendly menu-driven interface for easy navigation.

    ❌ Error Handling: Handles invalid inputs and edge cases gracefully.

⚒️ How to Use

    Install Python 3: Make sure you have Python 3 installed on your system.

    Clone the Repository:
    bash
    Copy

    git clone https://github.com/raolion/ATM-Simulator-in-Python.git

    Navigate to the Project Folder:
    bash
    Copy

    cd ATM-Simulator-in-Python

    Run the Program:

        For the original version:
        bash
        Copy

        python ATM.py

        For the new version with multi-user support:
        bash
        Copy

        python ATM_2_0.py

🚀 New in Version 2.0

    Multi-User System: Now supports multiple users with unique accounts.

    Transaction History: Each user has a record of their deposits and withdrawals.

    Improved Error Handling: Better handling of invalid inputs and edge cases.

    Enhanced User Interface: More intuitive menu options and feedback.

📂 File Structure

    ATM.py: The original version of the ATM simulator (single-user).

    ATM_2_0.py: The updated version with multi-user support and transaction history.
