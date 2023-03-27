# Team12

### member
+ Xueyan Huang
+ Ting Xu
+ Xiangchi Yuan
+ Ge Gao


# Pylint
## Transaction.py
************* Module Transaction
Transaction.py:1:0: C0103: Module name "Transaction" doesn't conform to snake_case naming style (invalid-name)
Transaction.py:108:4: C0103: Method name "runQuery" doesn't conform to snake_case naming style (invalid-name)

------------------------------------------------------------------
Your code has been rated at 9.55/10 (previous run: 9.55/10, +0.00)
## tracker.py
************* Module tracker
tracker.py:31:0: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:40:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:44:14: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:46:0: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:46:0: R0912: Too many branches (34/12) (too-many-branches)
tracker.py:46:0: R0915: Too many statements (72/50) (too-many-statements)

------------------------------------------------------------------
Your code has been rated at 9.36/10 (previous run: 9.36/10, +0.00)


# Pytest

tingxu@Tings-MacBook-Pro pa03 % pytest -vv
======================================================================== test session starts ========================================================================
platform darwin -- Python 3.10.10, pytest-7.2.1, pluggy-1.0.0 -- /opt/homebrew/opt/python@3.10/bin/python3.10
cachedir: .pytest_cache
rootdir: /Users/tingxu/Documents/courses/103a Fundamentals of Software Engineering/CS103aTeam12/pa03
plugins: anyio-3.6.2
collected 10 items                                                                                                                                                  

+ test_transaction.py::test_show_one PASSED                                                                                                                     [ 10%]
+ test_transaction.py::test_show_all PASSED                                                                                                                     [ 20%]
+ test_transaction.py::test_add_transaction PASSED                                                                                                              [ 30%]
+ test_transaction.py::test_delete PASSED                                                                                                                       [ 40%]
+ test_transaction.py::test_delete_all PASSED                                                                                                                   [ 50%]
+ test_transaction.py::test_selectYearMonthDate PASSED                                                                                                          [ 60%]
+ test_transaction.py::test_select_category PASSED                                                                                                              [ 70%]
+ test_transaction.py::test_add_category PASSED                                                                                                                 [ 80%]
+ test_transaction.py::test_show_categories PASSED                                                                                                              [ 90%]
+ test_transaction.py::test_modify_category PASSED                                                                                                              [100%]

======================================================================== 10 passed in 0.03s =========================================================================

# Tracker.py

tingxu@Tings-MacBook-Pro pa03 % python3 tracker.py
usage:
+ quit
+ showcategories
+ addcategories
+ modifycategories
+ add amount category description
+ modify item_id name
+ showall
+ show item_id
+ deleteall
+ delete item_id
+ indyear year
+ findmonth month
+ findday day
+ findcategory category
+ printmenu


# the transcript
=========================================================================           
command> 

gegao@GeGaos-MacBook-Pro pa03 % python3 tracker.py
usage:
            quit
            showcategories
            addcategories
            modifycategories
            add amount category description
            modify item_id name
            showall
            show item_id
            deleteall
            delete item_id
            findyear year
            findmonth month
            findday day
            findcategory category
            printmenu
            
command> add 17 pet snake
['add', '17', 'pet', 'snake']
17
------------------------------------------------------------



command> showall


item_id    amount     category   date       description         
------------------------------------------------------------
6          122        food       2023-03-27 bread               
7          18         food       2023-03-27 lobster             
8          8          pets       2023-03-27 cat                 
9          None       appliance        None None                
10         31         appliance  2023-03-27 fridge              
11         200        pets       2023-03-27 rat                 
13         None       shop             None None                
14         17         pet        2023-03-27 snake               
------------------------------------------------------------



command> delete 17
------------------------------------------------------------



command> showall


item_id    amount     category   date       description         
------------------------------------------------------------
6          122        food       2023-03-27 bread               
7          18         food       2023-03-27 lobster             
8          8          pets       2023-03-27 cat                 
9          None       appliance        None None                
10         31         appliance  2023-03-27 fridge              
11         200        pets       2023-03-27 rat                 
13         None       shop             None None                
14         17         pet        2023-03-27 snake               
------------------------------------------------------------



command> delete 14
------------------------------------------------------------



command> showall


item_id    amount     category   date       description         
------------------------------------------------------------
6          122        food       2023-03-27 bread               
7          18         food       2023-03-27 lobster             
8          8          pets       2023-03-27 cat                 
9          None       appliance        None None                
10         31         appliance  2023-03-27 fridge              
11         200        pets       2023-03-27 rat                 
13         None       shop             None None                
------------------------------------------------------------



command> show 11


item_id    amount     category   date       description         
------------------------------------------------------------
11         200        pets       2023-03-27 rat                 
------------------------------------------------------------



command> showcategories
['food', 'food', 'pets', 'appliance', 'appliance', 'pets', 'shop']
------------------------------------------------------------



command> addcategories drink
['addcategories', 'drink']
[]
------------------------------------------------------------



command> showcategories
['food', 'food', 'pets', 'appliance', 'appliance', 'pets', 'shop', 'drink']
------------------------------------------------------------



command> modifycategories shop shops
['modifycategories', 'shop', 'shops']
[]
------------------------------------------------------------



command> showcategories
['food', 'food', 'pets', 'appliance', 'appliance', 'pets', 'shops', 'drink']
------------------------------------------------------------



command> printmenu
usage:
            quit
            showcategories
            addcategories
            modifycategories
            add amount category description
            modify item_id name
            showall
            show item_id
            deleteall
            delete item_id
            findyear year
            findmonth month
            findday day
            findcategory category
            printmenu
            
------------------------------------------------------------



command> findcategory pets


item_id    amount     category   date       description         
------------------------------------------------------------
8          8          pets       2023-03-27 cat                 
11         200        pets       2023-03-27 rat                 
------------------------------------------------------------



command> findday 26
no tasks to print
------------------------------------------------------------



command> showall


item_id    amount     category   date       description         
------------------------------------------------------------
6          122        food       2023-03-27 bread               
7          18         food       2023-03-27 lobster             
8          8          pets       2023-03-27 cat                 
9          None       appliance        None None                
10         31         appliance  2023-03-27 fridge              
11         200        pets       2023-03-27 rat                 
13         None       shops            None None                
15         None       drink            None None                
------------------------------------------------------------



command> findday 27


item_id    amount     category   date       description         
------------------------------------------------------------
6          122        food       2023-03-27 bread               
7          18         food       2023-03-27 lobster             
8          8          pets       2023-03-27 cat                 
10         31         appliance  2023-03-27 fridge              
11         200        pets       2023-03-27 rat                 
------------------------------------------------------------



command> findmonth 3


item_id    amount     category   date       description         
------------------------------------------------------------
6          122        food       2023-03-27 bread               
7          18         food       2023-03-27 lobster             
8          8          pets       2023-03-27 cat                 
10         31         appliance  2023-03-27 fridge              
11         200        pets       2023-03-27 rat                 
------------------------------------------------------------



command> findyear 1998
no tasks to print
------------------------------------------------------------



command> findyear 2023


item_id    amount     category   date       description         
------------------------------------------------------------
6          122        food       2023-03-27 bread               
7          18         food       2023-03-27 lobster             
8          8          pets       2023-03-27 cat                 
10         31         appliance  2023-03-27 fridge              
11         200        pets       2023-03-27 rat                 
------------------------------------------------------------



command> printmenu 
usage:
            quit
            showcategories
            addcategories
            modifycategories
            add amount category description
            modify item_id name
            showall
            show item_id
            deleteall
            delete item_id
            findyear year
            findmonth month
            findday day
            findcategory category
            printmenu
            
------------------------------------------------------------



command> findcategory pets


item_id    amount     category   date       description         
------------------------------------------------------------
8          8          pets       2023-03-27 cat                 
11         200        pets       2023-03-27 rat                 
------------------------------------------------------------



command> deleteall
------------------------------------------------------------



command> showall
no tasks to print
------------------------------------------------------------



command> quit