import pytest
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

def test_select_category():
    test_db = 'test_select_category.db'
    transaction = Transaction(test_db)
    item1 = {'amount': 50, 'category': 'Food', 'date': '2023-03-26', 'description': 'Delicious Food'}
    item2 = {'amount': 100, 'category': 'Gas', 'date': '2023-02-28', 'description': 'Filled up gas tank'}
    transaction.add_transaction(item1)
    transaction.add_transaction(item2)
    transactions = transaction.select_category('Food')
    assert transactions[0]['amount'] == item1['amount']
    transactions = transaction.select_category('Gas')
    assert transactions[1]['amount'] == item2['amount']


