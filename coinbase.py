import os, hmac, hashlib, time, requests
from requests.auth import AuthBase
from dotenv import load_dotenv
from exchange import get_exchange_rate

load_dotenv()

# Before implementation, set environmental variables with the names API_KEY and API_SECRET
API_KEY = os.getenv('COINBASE_KEY')
API_SECRET = os.getenv('COINBASE_SECRET')
EXCHANGE_KEY = os.getenv('EXCHANGE_KEY')


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

def get_wallet_data(API_KEY, API_SECRET):
    # Get data on wallets in ascending order
    auth = CoinbaseWalletAuth(API_KEY, API_SECRET)
    params = {'limit': 100, 'order': 'asc'}
    r = requests.get(f'https://api.coinbase.com/v2/accounts', auth=auth, params=params)
    json = r.json()
    data = json['data']
    return data

def get_coinbase_account_balance(data):
    portfolio_total = 0
    for wallet in data:
        name = wallet['name']
        balance = float(wallet['balance']['amount'])
        asset_id = wallet['currency']['code']
        if balance > 0:
            exchange_rate = get_exchange_rate(EXCHANGE_KEY, asset_id)
            balance_in_usd = balance * exchange_rate
            portfolio_total = portfolio_total + balance_in_usd
            print(f'You have ${balance_in_usd} in your {name}({asset_id})') 
    print(f'You currently have ${portfolio_total} in your Coinbase account!')
    return portfolio_total
