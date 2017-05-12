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

'''
	List records

	Records can be listed and filtered via search().
	search() takes a mandatory domain filter (possibly empty), and returns the database
 	identifiers of all records matching the filter. To list customer companies for instance:
 	expected results:
 	[7, 18, 12, 14, 17, 19, 8, 31, 26, 16, 13, 20, 30, 22, 29, 15, 23, 28, 74]
'''
results = models.execute_kw(db, uid, password,
    'res.partner', 'search',
    [[['is_company', '=', True], ['customer', '=', True]]])

print results
'''
  print list of ids
'''