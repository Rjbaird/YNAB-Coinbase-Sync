import os, requests, json, coinbase
from datetime import date
from dotenv import load_dotenv

from ynab import get_ynab_account_balance, update_account_balance
from coinbase import CoinbaseWalletAuth, get_wallet_data
from exchange import get_exchange_rate
from bot import send_message

load_dotenv()

YNAB_TOKEN = os.getenv('YNAB_TOKEN')
BUDGET_ID = os.getenv('BUDGET_ID')
ACCOUNT_ID = os.getenv('ACCOUNT_ID')

COIN_KEY = os.getenv('COINBASE_KEY')
COIN_SECRET = os.getenv('COINBASE_SECRET')

EXCHANGE_KEY = os.getenv('EXCHANGE_KEY')

BOT_TOKEN = os.getenv('DISCORD_TOKEN')

today = date.today()
YNAB_transaction_date = today.strftime('%Y-%m-%d')

ynab_balance = get_ynab_account_balance(YNAB_TOKEN, BUDGET_ID, ACCOUNT_ID)
wallet_data = coinbase.get_wallet_data(COIN_KEY, COIN_SECRET)
portfolio_balance = coinbase.get_coinbase_account_balance(wallet_data)


def create_update_message(account_change, current_value):
    if account_change >= 0:
        return f'Coinbase adjustment created! Your Coinbase account is now at ${current_value}, up ${account_change} from last week 🥳'
    else:
        account_change = account_change * -1
        return f'Coinbase adjustment created! Your Coinbase account is now at ${current_value}, down -${account_change} from last week 💩'
