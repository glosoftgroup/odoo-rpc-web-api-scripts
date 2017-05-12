url = 'http://192.168.0.18:8069'
db = 'mydb15'
username = 'pkinuthia10@gmail.com'
password = 'password'

import xmlrpclib
common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
connecting = '''
Connecting to odoo server and using...'''
'''
Expected results
common.version() function
ask for the server's version
result
{
    "server_version": "8.0",
    "server_version_info": [8, 0, 0, "final", 0],
    "server_serie": "8.0",
    "protocol_version": 1,
}

'''
print(connecting)
print(common.version())
