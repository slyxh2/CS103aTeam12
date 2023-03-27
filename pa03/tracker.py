#! /usr/local/bin/python3


from Transaction import Transaction
import sys
import sqlite3
from datetime import datetime


# here are some helper functions ...

def print_usage():
    ''' print an explanation of how to use this command '''
    print('''usage:
            quit
            showcategories
            add amount category description
            modify item_id name
            show
            delete item_id
           
            '''
            )

def print_transactions(transaction):
    ''' print the items '''
    if len(transaction)==0:
        print('no tasks to print')
        return
    print('\n')
    print("%-10s %-10s %-10s %-10s %-20s"%('item_id','amount','category','date', 'description'))
    print('-'*60)
    for item in transaction:
        values = tuple(item.values()) #(rowid,title,desc,completed)
        print("%-10s %-10s %-10s %10s %-20s"%values)

def process_args(arglist):
    ''' examine args and make appropriate calls to TodoList'''
    transaction = Transaction('transsss.db')
    if arglist==[]:
        print_usage()
    elif arglist[0]=="show":
        print_transactions(transaction.show_transactions())
    elif arglist[0]=='add':
        print(arglist)
        if len(arglist)!=4:
            print_usage()
        else:
            current_year = datetime.now().year
            current_month = datetime.now().month
            current_day = datetime.now().day
            item = {'amount':int(arglist[1]),'category':arglist[2],'date':sqlite3.Date(current_year, current_month, current_day),'description':arglist[3] }
            print(item)
            transaction.add_transaction(item)
    elif arglist[0]=='findyear':
        if len(arglist)!= 2:
            print_usage()
        else:
            print_transactions(transaction.selectYear(arglist[1]))
    elif arglist[0]=='findmonth':
        if len(arglist)!= 2:
            print_usage()
        else:
            month = str(arglist[1]).zfill(2)
            print_transactions(transaction.selectMonth(month))   
    elif arglist[0]=='finddate':
        if len(arglist)!= 2:
            print_usage()
        else:
            date = str(arglist[1]).zfill(2)
            print_transactions(transaction.selectDate(date))      
    else:
        print(arglist,"is not implemented")
        print_usage()


def toplevel():
    ''' read the command args and process them'''
    if len(sys.argv)==1:
        # they didn't pass any arguments, 
        # so prompt for them in a loop
        print_usage()
        args = []
        while args!=['']:
            args = input("command> ").split(' ')
            if args[0]=='add':
                # join everyting after the name as a string
                args = ['add', args[1],args[2]," ".join(args[3:])]
            process_args(args)
            print('-'*60+'\n'*3)
    else:
        # read the args and process them
        args = sys.argv[1:]
        process_args(args)
        print('-'*40+'\n'*3)

    

toplevel()