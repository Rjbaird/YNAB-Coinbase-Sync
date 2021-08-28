import os, requests
from dotenv import load_dotenv

load_dotenv()

EXCHANGE_KEY = os.getenv('EXCHANGE_KEY')

def get_exchange_rate(TOKEN, ASSET_ID):
    
    headers = {'X-CoinAPI-Key': TOKEN}
    response = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{ASSET_ID}/USD', headers=headers)
    data = response.json()
    current_rate = data['rate']
    print(f'{ASSET_ID} is currently valued at ${current_rate}')
    return current_rate