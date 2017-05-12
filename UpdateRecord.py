nurl = 'http://localhost:8069'
db = 'mydb15'
username = 'email@gmail.com'
password = 'password'

import xmlrpclib
common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))

connecting = '''
Connecting to odoo server and using...'''
print(connecting)

# create a new partner
id = models.execute_kw(db, uid, password, 'res.partner', 'create', [{
    'name': "Another New Partner",
}]) 

models.execute_kw(db, uid, password, 'res.partner', 'write', [[id], {
    'name': "Another Newer partner"
}])
# get record name after having changed it
result = models.execute_kw(db, uid, password, 'res.partner', 'name_get', [[id]])
print(esult)

'''
Update records

Records can be updated using write(), it takes a list of records 
to update and a mapping of updated fields to values similar to create().
expected results: [[78, "Newer partner"]]

'''