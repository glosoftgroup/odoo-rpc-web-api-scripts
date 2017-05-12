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
models.execute_kw(db, uid, password,'product.template','search_read',[[]],{'fields':['name','description','type']})