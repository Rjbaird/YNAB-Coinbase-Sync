import os
import requests
from datetime import date
from dotenv import load_dotenv


load_dotenv()

YNAB_URL = 'http://api.youneedabudget.com/v1'
YNAB_TOKEN = os.getenv('YNAB_TOKEN')
BUDGET_ID = os.getenv('BUDGET_ID')
ACCOUNT_ID = os.getenv('ACCOUNT_ID')

COIN_URL = 'https://api.coinbase.com/v2'
COIN_KEY = os.getenv('COINBASE_KEY')
COIN_SECRET = os.getenv('COINBASE_SECRET')

BOT_TOKEN = os.getenv('DISCORD_TOKEN')

today = date.today()
transactionDate = today.strftime('%Y-%m-%d')


def create_message(account_change, current_value):
    if account_change >= 0:
        return f'Coinbase adjustment created! Your Coinbase account is now at ${current_value}, up ${account_change} from last week 🥳'
    else:
        account_change = account_change * -1
        return f'Coinbase adjustment created! Your Coinbase account is now at ${current_value}, down -${account_change} from last week 💩'

message = create_message(75, 1250)
print(message)