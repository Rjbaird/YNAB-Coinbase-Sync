import hmac, hashlib, time, requests
from requests.auth import AuthBase
from exchange import get_exchange_rate

class CoinbaseWalletAuth(AuthBase):
    """ Creates a custom Class for authentication with the Coinbase API
    Taken from https://stackoverflow.com/questions/66619124/coinbase-api-standard-python-example-returns-invalid-signature
    """    
    def __init__(self, api_key, secret_key):
        self.api_key = api_key
        self.secret_key = secret_key

    def __call__(self, request):
        timestamp = str(int(time.time()))
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
    """Makes a GET request to the Coinbase API to retrive the current balance of each wallet in an account

    Args:
        API_KEY [str]: Coinbase API Key
        API_SECRET [str]: Coinbase API Secret

    Returns:
        [dir]: Directory of account data from the Coinbase API GET request in ascending order
    """    
    auth = CoinbaseWalletAuth(API_KEY, API_SECRET)
    params = {'limit': 100, 'order': 'asc'}
    r = requests.get(f'https://api.coinbase.com/v2/accounts', auth=auth, params=params)
    json = r.json()
    data = json['data']
    return data

def get_coinbase_account_balance(EXCHANGE_KEY, data):
    """Calculates total balance in a Coinbase account.
    Loops thru each wallet with data from the Coinbase API, ignores wallets with zero balance and calculates the balance of each wallet into USD.

    Args:
        EXCHANGE_KEY [str]: Coin.io API Key. Used for calcuating the current exchange rate
        data [dir]: Directory of data pulled from the get_wallet_data function and the Coinbase API

    Returns:
        [float]: Returns total portfolio balance as a float
    """   
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
