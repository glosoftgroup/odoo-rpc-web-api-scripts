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


models.execute_kw(db, uid, password,
    'res.partner', 'search_read',
    [[['is_company', '=', True], ['customer', '=', True]]],
    {'fields': ['name', 'country_id', 'comment'], 'limit': 5})

'''
Odoo provides a search_read() shortcut which as its name suggests is equivalent
to a search() followed by a read(), but avoids having to perform two requests 
and keep ids around.

'''