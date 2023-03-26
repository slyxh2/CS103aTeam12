'''
Transaction.py is an Object Relational Mapping to the transactions database

The ORM will work map SQL rows with the schema
    (item #, amount, category, date, description)
    
    ######待补充

In place of SQL queries, we will have method calls.

This app will store the data in a SQLite database ~/transactions.db

'''
import sqlite3
import os
from datetime import date
def toDict(t):
    ''' t is a tuple (item #, amount, category, date, description)'''
    print('t='+str(t))
    transactions = {'item #':t[0], 'amount':t[1], 'category':t[2], 'date':t[3], 'description': t[4]}
    return transactions

class Transaction():
    def __init__(self, dbName):
        self.dbName = dbName;
        self.runQuery('''CREATE TABLE IF NOT EXISTS transactions
                    (
                    item_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    amount int,
                    category text,
                    date DATE,
                    description text)''',())

    def selectAll(self):
        ''' return all of the transactions as a list of dicts.'''
        return self.runQuery("SELECT rowid,* from transactions",())

    def selectCompleted(self):
        ''' return all of the completed tasks as a list of dicts.'''
        return self.runQuery("SELECT rowid,* from todo where completed=1",())

    def show_transactions(self):
        # return all the transactions
        return self.runQuery("SELECT * FROM transactions",())

    def add_transaction(self,item):
        # add one transaction based on the input and today's date
        return self.runQuery("INSERT INTO transactions VALUES(?,?,?,?)",(item['amount'],item['category'],date.today(), item['description']))

    def delete(self,item_id):
        #delete a transaction item ›
        return self.runQuery("DELETE FROM transaction WHERE item_id=(?)",(item_id,))

    def setComplete(self,rowid):
        ''' mark a todo item as completed '''
        return self.runQuery("UPDATE todo SET completed=1 WHERE rowid=(?)",(rowid,))

    def runQuery(self,query,tuple):
        ''' return all of the transaction as a list of dicts.'''
        con= sqlite3.connect(os.getenv('HOME')+'/'+self.dbName)
        cur = con.cursor() 
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [toDict(t) for t in tuples]

    
        
