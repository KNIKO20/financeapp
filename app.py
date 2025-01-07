from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime 

app = Flask(__name__)

# BBDD Conection
def get_db_connection():
    conn = sqlite3.connect('db/database.db')
    conn.row_factory = sqlite3.Row  # Enables accessing rows as dictionaries.
    return conn
 

# If doesn't exist, create the table
def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            description TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = get_db_connection()
    transactions = conn.execute('SELECT * FROM transactions').fetchall()
    conn.close()
    return render_template('index.html', transactions=transactions)


@app.route('/add', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        date = request.form['date']
        category = request.form['category']
        amount = request.form['amount']
        description = request.form['description']

        conn = get_db_connection()
        conn.execute('INSERT INTO transactions (date, category, amount, description) VALUES (?, ?, ?, ?)',
                     (date, category, float(amount), description))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET'])
def edit(id):
    conn = get_db_connection()
    transactions = conn.execute('SELECT * FROM transactions').fetchall()
    conn.close()
    return render_template('index.html', transactions=transactions, edit_id=id)

@app.route('/update/<int:id>', methods=['POST'])
def update_transaction(id):
    conn = get_db_connection()
    current_transaction = conn.execute('SELECT * FROM transactions WHERE id = ?', (id,)).fetchone()
    
    # if not current_transaction:
    #     conn.close()
    #     return f"Transaction with ID {id}, not found", 404

#Update only the provided fields, keep others unchanged
    updated_data = {
            "date": request.form.get('date', current_transaction['date']),
            "category": request.form.get('category', current_transaction['category']),
            "amount": float(request.form.get('amount', current_transaction['amount'])),
            "description": request.form.get('description', current_transaction['description']),
            }
# Update the transaction in the database
    conn.execute(
            '''
            UPDATE transactions
            SET date = ?, category = ?, amount = ?, description = ?
            WHERE id = ?
            '''
            , (updated_data['date'], updated_data['category'], updated_data['amount'], updated_data['description'], id))
    conn.commit()
    conn.close()

    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM transactions WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/summary')
def summary():
    conn = get_db_connection()
    total = conn.execute('SELECT amount FROM transactions').fetchall()
    conn.close()
    
    amounts = [row['amount'] for row in total]
    total_amount = sum(amounts)
    formatted_total = f"${total_amount:,.2f}"

    return render_template('summary.html', total=formatted_total)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

