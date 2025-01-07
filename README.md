# FinazApp

**FinazApp** is a personal finance tracking application built using **Flask**, **SQLite**, and **HTML/CSS**. This project is still under construction and aims to allow users to manage and track their financial transactions, categorize expenses, and get a summary of their finances.

## Features
- **Add Transactions**: Users can add new transactions with details such as date, category, amount, and description.
- **Edit Transactions**: Users can update the details of their existing transactions.
- **Delete Transactions**: Users can delete transactions from the database.
- **Transaction Summary**: A page that summarizes the total amount of all transactions.

## Technologies Used
- **Flask**: A micro web framework for Python, used for building the web application.
- **SQLite**: A lightweight database used to store transaction data.
- **HTML/CSS**: Frontend technologies used to build the user interface.

## Project Structure

```
finazapp/ 
├── app.py # Main application file (Flask routes and logic) 
├── db/ # SQLite database file (database.db) 
├── static/ # Static files (CSS, JavaScript, images) 
├── templates/ # HTML files (index.html, add.html, summary.html) 
├── README.md # Project documentation
```


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/finazapp.git
2. Navigate to the project directory:
   ```bash
   cd finazapp
3. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
4. Run the Application:
   ```bash
   python3 app.py
   
