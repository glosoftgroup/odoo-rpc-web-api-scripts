url = 'http://localhost:8069'
db = 'mydb15'
username = 'pkinuthia10@gmail.com'
password = 'password'

import xmlrpclib
common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
common.version()
'''
common.version()
ask for the server's version
result
{
    "server_version": "8.0",
    "server_version_info": [8, 0, 0, "final", 0],
    "server_serie": "8.0",
    "protocol_version": 1,
}

'''

#login in using authenticate function
uid = common.authenticate(db, username, password, {})

'''
	Calling methods
	The second endpoint is xmlrpc/2/object, is used to call methods of odoo models 
	via the execute_kw RPC function.
'''

'''
	read the res.partner model we can call check_access_rights with operation passed 
	by position and raise_exception passed by keyword (in order to get a true/false 
	result rather than true/error):
'''
models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))
models.execute_kw(db, uid, password,
    'res.partner', 'check_access_rights',
    ['read'], {'raise_exception': False})
'''
	List records

	Records can be listed and filtered via search().
	search() takes a mandatory domain filter (possibly empty), and returns the database
 	identifiers of all records matching the filter. To list customer companies for instance:
 	expected results:
 	[7, 18, 12, 14, 17, 19, 8, 31, 26, 16, 13, 20, 30, 22, 29, 15, 23, 28, 74]
'''
models.execute_kw(db, uid, password,
    'res.partner', 'search',
    [[['is_company', '=', True], ['customer', '=', True]]])

'''
	Count records

	Rather than retrieve a possibly gigantic list of records and count them, search_count()
	can be used to retrieve only the number of records matching the query. It takes the same
	domain filter as search() and no other parameter.
	Expected results <num> eg. 19
'''
models.execute_kw(db, uid, password,
    'res.partner', 'search_count',
    [[['is_company', '=', True], ['customer', '=', True]]])
'''
	Read records

	Record data is accessible via the read() method, which takes a list of ids (as returned by search())
	and optionally a list of fields to fetch. By default, it will fetch all the fields the current user
	can read, which tends to be a huge amount.
'''
ids = models.execute_kw(db, uid, password,
    'res.partner', 'search',
    [[['is_company', '=', True], ['customer', '=', True]]],
    {'limit': 1})
[record] = models.execute_kw(db, uid, password,
    'res.partner', 'read', [ids])
# count the number of fields fetched by default
len(record)