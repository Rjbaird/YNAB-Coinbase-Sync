import os, requests, hmac, hashlib, time, requests, base64 
from dotenv import load_dotenv
import cbpro
public_client = cbpro.PublicClient()

load_dotenv()

KEY = os.getenv('COINBASE_API_KEY')
SECRET = os.getenv('COINBASE_API_SECRET')
PASSPHRASE = os.getenv('COINBASE_PASSPHRASE')


def get_coinbase_account_balance(KEY, SECRET, PASSPHRASE):
     
    auth_client = cbpro.AuthenticatedClient(KEY, SECRET, PASSPHRASE)

    response = auth_client.get_accounts()

    print(response)

get_coinbase_account_balance(KEY, SECRET, PASSPHRASE)