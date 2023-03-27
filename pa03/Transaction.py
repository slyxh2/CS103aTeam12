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
def toDict(t):
    ''' t is a tuple (item_id, amount, category, date, description)'''
    transactions = {'item_id':t[0], 'amount':t[1], 'category':t[2], 'date':t[3], 'description': t[4]}
    return transactions

class Transaction():
    def __init__(self, dbName):
        self.dbName = dbName;
        self.runQuery('''CREATE TABLE IF NOT EXISTS transactions
                    (
                    item_id INTEGER  PRIMARY KEY AUTOINCREMENT,
                    amount INT,
                    category TEXT,
                    date DATE,
                    description TEXT)''',())
        
        
    def show_categories(self):
        ''' Ting Xu''' 
        ''' return all the categories '''
        return self.runQuery("SELECT DISTINCT category FROM transactions",())
    
    def add_categories(self,item):
        ''' Ting Xu'''
        ''' add a new category '''
        return self.runQuery("INSERT INTO transactions (amount, category, date, description) VALUES(?,?,?,?)",(item[None],item['category'],item[None], item[None]))
    
    def modify_categories(self, old_category, new_category):
        ''' Ting Xu'''
        ''' replace a existed category by a new category '''
        return self.runQuery("UPDATE transactions SET category=(?) WHERE category=(?);",(old_category, new_category))
 
    def show_all(self):
        # return all the transactions Ge Gao
        return self.runQuery("SELECT * FROM transactions",())

    def show_one(self,item_id):
        # return just one designated transaction Ge Gao
        return self.runQuery("SELECT * FROM transactions WHERE item_id=(?)",(item_id))

    def add_transaction(self,item):
        # add one transaction based on the input and today's date Ge Gao
        print(item['amount']);
        return self.runQuery("INSERT INTO transactions (amount, category, date, description) VALUES(?,?,?,?)",(item['amount'],item['category'],item['date'], item['description']))

    def delete(self,item_id):
        #delete a transaction item Ge Gao
        return self.runQuery("DELETE FROM transactions WHERE item_id=(?)",(item_id))

    def delete_all(self):
        # return all the transactions Ge Gao
        self.runQuery("DELETE FROM transactions",())
        self.runQuery("VACUUM", ())
        
    def setComplete(self,rowid):
        ''' mark a todo item as completed '''
        return self.runQuery("UPDATE todo SET completed=1 WHERE rowid=(?)",(rowid,))
    
    def selectYear(self, year):
        ''' Xueyan Huang '''
        ''' select all transaction in terms of date '''
        return self.runQuery("SELECT * FROM transactions WHERE strftime('%Y', date) = (?)", (year,))
    
    def selectMonth(self, month):
        ''' Xueyan Huang '''
        ''' select all transaction in terms of date '''
        return self.runQuery("SELECT * FROM transactions WHERE strftime('%m', date) = (?)", (month,))
    
    def selectDate(self, date):
        ''' Xueyan Huang '''
        ''' select all transaction in terms of date '''
        return self.runQuery("SELECT * FROM transactions WHERE strftime('%d', date) = (?)", (date,))

    def select_category(self,category):
        ''' Xiangchi Yuan '''
        ''' select all transaction in terms of transactions '''
        return self.runQuery("SELECT * FROM transactions WHERE category = (?)", (category,))

    def runQuery(self,query,tuple):
        ''' return all of the transaction as a list of dicts.'''
        con= sqlite3.connect(os.getenv('HOME')+'/'+self.dbName)
        cur = con.cursor() 
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [toDict(t) for t in tuples]

    
        
