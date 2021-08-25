import os, hmac, hashlib, time, requests, json
from requests.auth import AuthBase
from dotenv import load_dotenv

load_dotenv()

# Before implementation, set environmental variables with the names API_KEY and API_SECRET
API_KEY = os.getenv('COINBASE_KEY')
API_SECRET = os.getenv('COINBASE_SECRET')


# Create custom authentication for Coinbase API
class CoinbaseWalletAuth(AuthBase):
    def __init__(self, api_key, secret_key):
        self.api_key = api_key
        self.secret_key = secret_key

    def __call__(self, request):
        timestamp = str(int(time.time()))

        # https://stackoverflow.com/questions/66619124/coinbase-api-standard-python-example-returns-invalid-signature
        try:
            body = request.body.decode()
            if body == "{}":
                request.body = b""
                body = ''
        except AttributeError:
             request.body = b""
             body = ''

        message = timestamp + request.method + request.path_url + body
        signature = hmac.new(self.secret_key.encode(), message.encode(), hashlib.sha256).hexdigest()
        request.headers.update({
                'CB-ACCESS-SIGN': signature,
                'CB-ACCESS-TIMESTAMP': timestamp,
                'CB-ACCESS-KEY': self.api_key
        })
        return request

params = {'limit': 100, 'order': 'asc'}
# only working with http NOT https for some reason...
api_url = 'https://api.coinbase.com/v2/'
auth = CoinbaseWalletAuth(API_KEY, API_SECRET)

# Get data on wallets in ascending order
r = requests.get(api_url + 'accounts', auth=auth, params=params)
json = json.loads(r.text)
data = json['data']
for wallet in data:
    balance = float(wallet['balance']['amount'])
    if balance > 0:
        print(wallet['name'])
        print(wallet['currency']['code'])
        print(f'You have ${balance}')

print(data)