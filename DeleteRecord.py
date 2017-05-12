url = 'http://localhost:8069'
db = 'mydb15'
username = 'pkinuthia10@gmail.com'
password = 'password'

import xmlrpclib
common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))

connecting = '''
Connecting to odoo server and using...'''
print(connecting)

#login in using authenticate function
uid = common.authenticate(db, username, password, {})
# create a new partner
id = models.execute_kw(db, uid, password, 'res.partner', 'create', [{
    'name': "Another New Partner",
}]) 

models.execute_kw(db, uid, password, 'res.partner', 'unlink', [[id]])
# check if the deleted record is still in the database
result = models.execute_kw(db, uid, password,
    'res.partner', 'search', [[['id', '=', id]]])
print(result)

'''
Delete records

Records can be deleted in bulk by providing their ids to unlink().
expected result []
empty list 

'''