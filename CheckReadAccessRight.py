''' 
	configuration variables

'''
url = 'http://localhost:8069'
db = 'mydb15'
username = 'pkinuthia10@gmail.com'
password = 'password'

#====================================================================
import xmlrpclib
common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))

#====================================================================

connecting = '''
Connecting to odoo server and using...'''
print(connecting)

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

result =  models.execute_kw(db,uid,password,'res.partner', 'check_access_rights',['read'], {'raise_exception':False})

print(result)

'''
 prints true or false if user has access right
'''