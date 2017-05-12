url = 'http://localhost:8069'
db = 'mydb15'
username = 'pkinuthia10@gmail.com'
password = 'password'

import xmlrpclib
common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))

connecting = '''
Connecting to odoo server and using...'''
print(connecting)

#login in using authenticate function
uid = common.authenticate(db, username, password, {})

print(uid)
'''
  if logged in prints 1 else False
'''