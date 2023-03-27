'''
Transaction.py is an Object Relational Mapping to the transactions database

The ORM will work map SQL rows with the schema
    (item_id, amount, category, date, description)
    
    ######待补充

In place of SQL queries, we will have method calls.

This app will store the data in a SQLite database ~/transactions.db

'''
import sqlite3
import os
def to_dict(item):
    ''' t is a tuple (item_id, amount, category, date, description)'''
    transactions = {
        'item_id': item[0],
        'amount': item[1],
        'category': item[2],
        'date': item[3],
        'description': item[4]
    }
    return transactions

class Transaction:
    ''' Transaction class '''
    def __init__(self, db_name):
        self.db_name = db_name
        self.run_query('''CREATE TABLE IF NOT EXISTS transactions
                    (
                    item_id INTEGER  PRIMARY KEY AUTOINCREMENT,
                    amount INT,
                    category TEXT,
                    date DATE,
                    description TEXT)''',())

    def show_categories(self):
        ''' return all the categories '''
        return self.run_query("SELECT DISTINCT category FROM transactions",())

    def add_categories(self,item):
        ''' add a new category '''
        return self.run_query(
            "INSERT INTO transactions (amount, category, date, description) VALUES(?,?,?,?)",
            (item[None], item['category'], item[None], item[None])
        )
    def modify_categories(self, old_category, new_category):
        ''' replace a existed category by a new category '''
        return self.run_query(
            "UPDATE transactions SET category=(?) WHERE category=(?);",
            (old_category, new_category)
        )

    def show_all(self):
        '''Ge Gao
        return all the transactions '''
        return self.run_query("SELECT * FROM transactions",())

    def show_one(self,item_id):
        '''return just one designated transaction Ge Gao'''
        return self.run_query("SELECT * FROM transactions WHERE item_id=(?)",(item_id,))

    def add_transaction(self,item):
        '''Ge Gao 
        add one transaction based on the input and today's date '''
        print(item['amount'])
        return self.run_query(
            "INSERT INTO transactions (amount, category, date, description) VALUES(?,?,?,?)",
            (item['amount'],item['category'],item['date'], item['description'])
        )

    def delete(self,item_id):
        '''delete a transaction item Ge Gao'''
        return self.run_query("DELETE FROM transactions WHERE item_id=(?)",(item_id,))

    def delete_all(self):
        '''Ge Gao 
        return all the transactions '''
        self.run_query("DELETE FROM transactions",())
        self.run_query("VACUUM", ())
    def select_year(self, year):
        ''' Xueyan Huang
        select all transaction in terms of year '''
        return self.run_query("SELECT * FROM transactions WHERE strftime('%Y', date) = (?)", (year,))

    def select_month(self, month):
        ''' Xueyan Huang
        select all transaction in terms of mouth '''
        return self.run_query(
            "SELECT * FROM transactions WHERE strftime('%m', date) = (?)",
            (month,)
        )

    def select_date(self, date):
        ''' Xueyan Huang
        select all transaction in terms of date '''
        return self.run_query("SELECT * FROM transactions WHERE strftime('%d', date) = (?)", (date,))

    def select_category(self,category):
        ''' Xiangchi Yuan
        select all transaction in terms of transactions '''
        return self.run_query("SELECT * FROM transactions WHERE category = (?)", (category,))

    def run_query(self,query,item_tuple):
        ''' return all of the transaction as a list of dicts.'''
        con= sqlite3.connect(os.getenv('HOME')+'/'+self.db_name)
        cur = con.cursor()
        cur.execute(query,item_tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [to_dict(t) for t in tuples]
