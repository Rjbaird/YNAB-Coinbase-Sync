import os, requests, hmac, hashlib, time, requests, base64
from dotenv import load_dotenv

load_dotenv()

BASE_URL = 'https://api.coinbase.com/v2'
KEY = os.getenv('COINBASE_KEY')
SECRET = os.getenv('COINBASE_SECRET')


def get_coinbase_account_balance(BASE_URL, KEY, SECRET):
    auth = get_auth()
    response = requests.get(f'{BASE_URL}/accounts', auth=auth)
    data = response.json()
    print(data)

def get_auth():

    timestamp = str(int(time.time()))
    path = '/accounts'
    method = 'GET'
    body = b""
    headers = {}
    message = f'{timestamp}{method}{path}{body}'.encode()
    hmac_key = bytes(SECRET, 'UTF-8')
    signature = hmac.new(hmac_key, message, hashlib.sha256).hexdigest()
    request = {
        body: body,
        method: method,
        path: path,
        headers: {
            'CB-ACCESS-TIMESTAMP': timestamp,
            'CB-ACCESS-KEY': KEY,
            'CB-ACCESS-SIGN': signature,
        }
    }

    try:
        body = request.body.decode()
        if body == "{}":
            request.body = b""
        body = ''
    except AttributeError:
        request.body = b""
        body = ''

        message = timestamp + request.method + request.path_url + body
        signature = hmac.new(
            SECRET.encode(), message.encode(), hashlib.sha256).hexdigest()
        request.headers.update({
            'CB-ACCESS-SIGN': signature,
            'CB-ACCESS-TIMESTAMP': timestamp,
            'CB-ACCESS-KEY': KEY,
        })
        return request

get_coinbase_account_balance(BASE_URL, KEY, SECRET)