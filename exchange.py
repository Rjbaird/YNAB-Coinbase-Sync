import requests

def get_exchange_rate(TOKEN, ASSET_ID):
    """ Gets the current exchange rate for a cryptocurrency in USD using the CoinAPI. API Key is availble for free but limited to 100 request per day

    Args:
        TOKEN ([str]): API Key to authenticate CoinAPI GET request
        ASSET_ID ([str]): Cryptocurrency asset id string. Example: Bitcoin = BTC

    Returns:
        [float]: Returns current exchange rate as a float
    """    
    headers = {'X-CoinAPI-Key': TOKEN}
    response = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{ASSET_ID}/USD', headers=headers)
    data = response.json()
    current_rate = data['rate']
    current_rate_float = float(current_rate)
    print(f'{ASSET_ID} is currently valued at ${current_rate}')
    return current_rate_float