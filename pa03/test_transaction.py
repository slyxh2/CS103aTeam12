import pytest
import os
from Transaction import Transaction

def test_show_one():
    test_db = 'test_show_one.db'
    transaction = Transaction(test_db)  
    item1 = {'amount': 50, 'category': 'Food', 'date': '2023-03-26', 'description': 'Delicious Food'}
    item2 = {'amount': 100, 'category': 'Gas', 'date': '2023-02-28', 'description': 'Filled up gas tank'}
    transaction.add_transaction(item1)
    transaction.add_transaction(item2)
    t1=transaction.show_one(1)
    t2=transaction.show_one(2)
    assert t1[0]['amount']==item1['amount']

def test_show_all():
    test_db = 'test_show_all.db'
    transaction = Transaction(test_db)  
    item1 = {'amount': 50, 'category': 'Food', 'date': '2023-03-26', 'description': 'Delicious Food'}
    item2 = {'amount': 100, 'category': 'Gas', 'date': '2023-02-28', 'description': 'Filled up gas tank'}
    transaction.add_transaction(item1)
    transaction.add_transaction(item2)
    t=transaction.show_all()
    assert t[0]['amount']==item1['amount']
    assert t[1]['amount']==item2['amount']


def test_add_transaction():
    test_db = 'test_add_transaction.db'
    transaction = Transaction(test_db)
    transaction.delete_all()
    item1 = {'amount': 50, 'category': 'Food', 'date': '2023-03-26', 'description': 'Delicious Food'}
    item2 = {'amount': 100, 'category': 'Gas', 'date': '2023-02-28', 'description': 'Filled up gas tank'}
    transaction.add_transaction(item1)
    transaction.add_transaction(item2)
    all_transactions = transaction.show_all()
    assert len(all_transactions) == 2
    assert all_transactions[0]['amount'] == item1['amount']
    assert all_transactions[1]['category'] == item2['category']

def test_delete():
    test_db = 'test_deleted.db'
    transaction = Transaction(test_db)  
    item1 = {'amount': 50, 'category': 'Food', 'date': '2023-03-26', 'description': 'Delicious Food'}
    item2 = {'amount': 100, 'category': 'Gas', 'date': '2023-02-28', 'description': 'Filled up gas tank'}
    transaction.add_transaction(item1)
    transaction.add_transaction(item2)
    transaction.delete(1)
    supposed = transaction.show_one(1)
    assert len(supposed) == 0

def test_delete_all():
    test_db = 'test_deleted_all.db'
    transaction = Transaction(test_db)  
    item1 = {'amount': 50, 'category': 'Food', 'date': '2023-03-26', 'description': 'Delicious Food'}
    item2 = {'amount': 100, 'category': 'Gas', 'date': '2023-02-28', 'description': 'Filled up gas tank'}
    transaction.add_transaction(item1)
    transaction.add_transaction(item2)
    transaction.delete_all()
    supposed = transaction.show_all()
    assert len(supposed) == 0

def test_selectYearMonthDate():
    test_db = 'test_selectYearMonthDate.db'
    transaction = Transaction(test_db)  
    item1 = {'amount': 50, 'category': 'Food', 'date': '2023-03-26', 'description': 'Delicious Food'}
    item2 = {'amount': 100, 'category': 'Gas', 'date': '2023-02-28', 'description': 'Filled up gas tank'}
    transaction.add_transaction(item1)
    transaction.add_transaction(item2)
    transactions = transaction.select_year('2023')

    assert transactions[0]['amount'] == item1['amount']
    assert transactions[1]['category'] == item2['category']

    t1 = transaction.select_month('03');
    t2 = transaction.select_month('02');
    assert t1[0]['amount'] == item1['amount']
    assert t2[0]['category'] == item2['category']

    t3 = transaction.select_date('26');
    t4 = transaction.select_date('28');
    assert t3[0]['amount'] == item1['amount']
    assert t4[0]['category'] == item2['category']
    transaction.run_query("DELETE FROM transactions", ())

def test_select_category():
    ''' Xiangchi Yuan '''
    test_db = 'test_select_category.db'
    transaction = Transaction(test_db)
    item1 = {
        'amount': 50, 
        'category': 'Food', 
        'date': '2023-03-26',
        'description': 'Delicious Food'
        }
    item2 = {
        'amount': 100, 
        'category': 'Gas', 
        'date': '2023-02-28', 
        'description': 'Filled up gas tank'
        }
    transaction.add_transaction(item1)
    transaction.add_transaction(item2)
    transactions = transaction.select_category('Food')
    assert transactions[0]['amount'] == item1['amount']
    transactions = transaction.select_category('Gas')
    assert transactions[1]['amount'] == item2['amount']

def test_add_category():
    ''' Ting Xu''' 
    test_db = 'test_category.db'
    transaction = Transaction(test_db) 
    transaction.add_categories('test')
    categories = transaction.show_categories()
    assert categories[0] == 'test'

def test_show_categories():
    ''' Ting Xu''' 
    test_db = 'test_show_category.db'
    transaction = Transaction(test_db) 
    item1 = {'amount': 50, 'category': 'Food', 'date': '2023-03-26', 'description': 'Delicious Food'}
    item2 = {'amount': 100, 'category': 'Gas', 'date': '2023-02-28', 'description': 'Filled up gas tank'}
    transaction.add_transaction(item1)
    transaction.add_transaction(item2)
    categories = transaction.show_categories()
    assert categories[2]== 'Food'
    
def test_modify_category():
    ''' Ting Xu''' 
    test_db = 'test_modify_category.db'
    transaction = Transaction(test_db) 
    item1 = {'amount': 50, 'category': 'Food', 'date': '2023-03-26', 'description': 'Delicious Food'}
    transaction.add_transaction(item1)
    transaction.modify_categories('Food', 'test')
    categories = transaction.show_categories()
    assert categories[2] == 'test'
    


