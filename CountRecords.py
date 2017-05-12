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
	Count records

	Rather than retrieve a possibly gigantic list of records and count them, search_count()
	can be used to retrieve only the number of records matching the query. It takes the same
	domain filter as search() and no other parameter.
	Expected results <num> eg. 19
'''
results = models.execute_kw(db, uid, password,
    'res.partner', 'search_count',
    [[['is_company', '=', True], ['customer', '=', True]]])
print(results)
'''
  prints number of records
'''