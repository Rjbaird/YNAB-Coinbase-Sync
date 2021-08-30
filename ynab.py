import os, requests
from datetime import date
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('YNAB_TOKEN')
BUDGET_ID = os.getenv('BUDGET_ID')
ACCOUNT_ID = os.getenv('ACCOUNT_ID')

today = date.today()
transactionDate = today.strftime('%Y-%m-%d')

def get_ynab_account_balance(TOKEN, BUDGET_ID, ACCOUNT_ID):
    """
    Makes a GET request to the YNAB API to retrive the current balance of an account
    Args:
        BASE_URL [str]: The base URL for the YNAB API.
        TOKEN [str]: YNAB token used for API authentication.
        BUDGET_ID [str]: ID for the YNAB Budget containing the Account you want the budget for.
        ACCOUNT_ID [str]: ID for the specific YNAB Account you need the balance for.
    Returns:
        [int]: Returns an integer from the current account balance
    """
    headers = {
        'Authorization': 'Bearer ' + TOKEN
    }
    params = {
        'method': 'GET',
        'headers': headers,
        'contentType': 'application/json'
    }

    response = requests.get(f'http://api.youneedabudget.com/v1/budgets/{BUDGET_ID}/accounts/{ACCOUNT_ID}', headers=headers, params=params)
    data = response.json()
    accountData = data['data']['account']
    accountBalance = accountData['balance']
    print(f'Account balance: ${accountBalance}')
    return accountBalance

def update_account_balance(TOKEN, BUDGET_ID, ACCOUNT_ID, AMOUNT, DATE):
    """
    Makes a POST request to the YNAB API 

    Args:
        BASE_URL [str]: The base URL for the YNAB API.
        TOKEN [str]: YNAB token used for API authentication.
        BUDGET_ID [str]: ID for the YNAB Budget containing the Account you want the budget for.
        ACCOUNT_ID [str]: ID for the specific YNAB Account you need the balance for.
        AMOUNT ([int]): The amount for the transactions as an interger. 
        DATE ([str]): Transaction date in the following format: 'Year-Month-Day' ie 2021-10-03

    Returns:
        [dir]: YNAB API response data from the POST request
    """    
    transactionData = { 
        'transaction': {
        'account_id': ACCOUNT_ID,
        'date': DATE,
        'amount': AMOUNT,
        'payee_name': 'Coinbase',
        'cleared': 'cleared',
        # 'flag_color': 'green',
        }
    }
    
    headers = {'Authorization': 'Bearer ' + TOKEN}
    response = requests.post(f'http://api.youneedabudget.com/v1/budgets/{BUDGET_ID}/transactions', json=transactionData, headers=headers)
    data = response.json()
    return data

