import requests
import time
import hashlib
import hmac
import sys

access_id = sys.argv[1]
access_key = sys.argv[2]
device_id = sys.argv[3]
region = sys.argv[4]

def get_token():
    t = str(int(time.time()*1000))
    sign_str = access_id + t
    sign = hmac.new(access_key.encode(), sign_str.encode(), hashlib.sha256).hexdigest().upper()
    headers = {
        'client_id': access_id,
        'sign': sign,
        't': t,
        'sign_method': 'HMAC-SHA256'
    }
    url = f'https://openapi.{region}.com/v1.0/token?grant_type=1'
    res = requests.get(url, headers=headers)
    return res.json()['result']['access_token']

def unlock_device():
    token = get_token()
    headers = {
        'Authorization': f'Bearer {token}',
        'client_id': access_id,
        'sign_method': 'HMAC-SHA256',
        'Content-Type': 'application/json'
    }
    url = f'https://openapi.{region}.com/v1.0/devices/{device_id}/commands'
    payload = {
        "commands": [
            {
                "code": "unlock_request",
                "value": 1
            }
        ]
    }
    res = requests.post(url, headers=headers, json=payload)
    print(res.text)

unlock_device()
