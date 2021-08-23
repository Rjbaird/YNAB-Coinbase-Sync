import os, requests, hmac, hashlib, time, requests, base64 
from dotenv import load_dotenv

load_dotenv()

BASE_URL = 'https://api.coinbase.com/v2'
KEY = os.getenv('COINBASE_KEY')
SECRET = os.getenv('COINBASE_SECRET')


def get_coinbase_account_balance(BASE_URL, KEY, SECRET):
    
    timestamp = str(int(time.time()))
    path = '/accounts'
    method = 'GET'
    message = f'{timestamp}{method}{path}'.encode()
    # hmac_key = base64.b64decode(SECRET)
    hmac_key = bytes(SECRET, 'UTF-8')
    signature = hmac.new(hmac_key, message, hashlib.sha256).hexdigest()
    # signature_b64 = base64.b64encode(signature.hexdigest()).decode('utf-8')
    
    
    headers = {
        'CB-ACCESS-TIMESTAMP': timestamp,
        'CB-ACCESS-KEY': KEY,
        'CB-ACCESS-SIGN': signature,
        'CB-VERSION': '2021-02-13',
        'contentType': 'application/json'
    }

    response = requests.get(f'{BASE_URL}/accounts', headers=headers)
    data = response.json()
    print(data)

get_coinbase_account_balance(BASE_URL, KEY, SECRET)