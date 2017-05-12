url = 'http://localhost:8069'
db = 'mydb15'
username = 'pkinuthia10@gmail.com'
password = 'password'

import xmlrpclib
common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))
#login in using authenticate function
uid = common.authenticate(db, username, password, {})

connecting = '''
Connecting to odoo server and using...'''
print(connecting)
print('Query the first 5 products')
print('#'*100)
print(models.execute_kw(db, uid, password,'product.template','search_read',[[]],{'fields':['name','description','type'],'limit':5}))
print('#'*100)
print('Query to filter by id')
print('*'*100)
print(models.execute_kw(db, uid, password,'product.template','search_read',[[['id','=','6']]],{'fields':['name','categ_id']}))
print('*'*100)
print('Filter products by category')
print(models.execute_kw(db, uid, password,'product.template','search_read',[[['categ_id','=',6]]],{'fields':['name','categ_id'], 'limit':5}))