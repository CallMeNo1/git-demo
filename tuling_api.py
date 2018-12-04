# first git- tuling test

import json
import requests
apikey = 'f575876d96df4419bf8e1dcfc6e94777'  # 贝康apikey'

def get_response(msg):
    key = apikey
    api = 'http://www.tuling123.com/openapi/api?key={}&info={}'.format( key, msg)
    return requests.get(api).json()

while True:
    text= input('User：')
    message = get_response(text)
    print(message)
