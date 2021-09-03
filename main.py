import os
from datetime import date
from dotenv import load_dotenv
from ynab import get_ynab_account_balance, update_account_balance, get_account_change
from coinbase import get_wallet_data, get_coinbase_account_balance
from bot import send_message, create_update_message, start_discord_bot

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
wallet_data = get_wallet_data(COIN_KEY, COIN_SECRET)
portfolio_balance = get_coinbase_account_balance(EXCHANGE_KEY, wallet_data)
account_change = get_account_change(portfolio_balance, ynab_balance)
update_account_balance(YNAB_TOKEN, BUDGET_ID, ACCOUNT_ID, account_change, YNAB_transaction_date)
bot_message = create_update_message(account_change, portfolio_balance)

