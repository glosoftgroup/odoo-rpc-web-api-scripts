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

id = models.execute_kw(db, uid, password, 'res.partner', 'create', 
	[{'name': "New Partner",}])
print(id)
'''
Create records

Records of a model are created using create(). The method will create a single record and return 
its database identifier.

create() takes a mapping of fields to values, used to initialize the record. For any field which
 has a default value and is not set through the mapping argument, the default value will be used.
 
'''