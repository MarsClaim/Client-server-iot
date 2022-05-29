from ast import Return
from http import client
from wsgiref import headers
from iiot_device import Sensor 
import json
import time

_conn = client.HTTPConnection(host='localhost', port=5000)

s = Sensor()

h={'content-type':'application/json'}

while True:
    data={
    'id':1,
    'name': 'Proximity Sensor', 
    'value': s.get_random_number() 
    }
    json_data = json.dumps(data)
	
    if [{s.get_random_number() > 15}]:
        print (data)
    
    else:
        print(s.get_random_number())	

    _conn.request('POST', '/devices', json_data, headers=h)
    _conn.close(
    )
    
    
    time.sleep(1)