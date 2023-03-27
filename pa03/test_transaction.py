import pytest
import os
from Transaction import Transaction

def test_selectYearMonthDate():
    test_db = 'test_selectYearMonthDate.db'
    transaction = Transaction(test_db)  
    item1 = {'amount': 50, 'category': 'Food', 'date': '2023-03-26', 'description': 'Delicious Food'}
    item2 = {'amount': 100, 'category': 'Gas', 'date': '2023-02-28', 'description': 'Filled up gas tank'}
    transaction.add_transaction(item1)
    transaction.add_transaction(item2)
    transactions = transaction.selectYear('2023')

    assert transactions[0]['amount'] == item1['amount']
    assert transactions[1]['category'] == item2['category']

    t1 = transaction.selectMonth('03');
    t2 = transaction.selectMonth('02');
    assert t1[0]['amount'] == item1['amount']
    assert t2[0]['category'] == item2['category']

    t3 = transaction.selectDate('26');
    t4 = transaction.selectDate('28');
    assert t3[0]['amount'] == item1['amount']
    assert t4[0]['category'] == item2['category']
    transaction.runQuery("DELETE FROM transactions", ())

def test_add_category():
    test_db = 'test_category.db'
    transaction = Transaction(test_db) 
    transaction.add_categories(None, 'test', None, None)
    categories = transaction.show_categories()
    assert len(categories) == 1
    assert categories[0] == 'test'

def test_show_categories():
    test_db = 'test_show_category.db'
    transaction = Transaction(test_db) 
    item1 = {'amount': 50, 'category': 'Food', 'date': '2023-03-26', 'description': 'Delicious Food'}
    item2 = {'amount': 100, 'category': 'Gas', 'date': '2023-02-28', 'description': 'Filled up gas tank'}
    transaction.add_transaction(item1)
    transaction.add_transaction(item2)
    categories = transaction.show_categories()
    assert len(categories) == 2
    assert 'Food' in categories
    assert 'Gas' in categories
    
def test_modify_category():
    test_db = 'test_modify_category.db'
    transaction = Transaction(test_db) 
    item1 = {'amount': 50, 'category': 'Food', 'date': '2023-03-26', 'description': 'Delicious Food'}
    transaction.add_transaction(item1)
    transaction.modify_categories('Food', 'test')
    categories = transaction.show_categories()
    assert categories[0] == 'test'
    


