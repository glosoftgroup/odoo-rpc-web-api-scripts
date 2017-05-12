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

partner = {'name':'Web api partner','street':'Ndumberi Road','phone':'072000000000','type':'contact','zip':'00900','city':'Kiambu'}
print('Creating a new partner using details below')
print(partner)
parner_id = models.execute_kw(db,uid,password,'res.partner','create',[partner])

if parner_id:
	print('Partner created successfuly')
	print(parner_id)
else:
	print('Error Creating partner')

'''
returns an integer when users is created successfully
'''