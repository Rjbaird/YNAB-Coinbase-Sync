import requests

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
    headers = {'Authorization': 'Bearer ' + TOKEN}
    params = {
        'method': 'GET',
        'headers': headers,
        'contentType': 'application/json'
    }

    response = requests.get(f'http://api.youneedabudget.com/v1/budgets/{BUDGET_ID}/accounts/{ACCOUNT_ID}', headers=headers, params=params)
    data = response.json()
    accountData = data['data']['account']
    accountBalance = accountData['balance'] / 1000
    print(f'YNAB Account balance: ${accountBalance}')
    return accountBalance

def update_account_balance(TOKEN, BUDGET_ID, ACCOUNT_ID, AMOUNT, DATE):
    """
    Makes a POST request to the YNAB API 

    Args:
        BASE_URL [str]: The base URL for the YNAB API.
        TOKEN [str]: YNAB token used for API authentication.
        BUDGET_ID [str]: ID for the YNAB Budget containing the Account you want the budget for.
        ACCOUNT_ID [str]: ID for the specific YNAB Account you need the balance for.
        AMOUNT [float]: The amount for the transactions as an interger. 
        DATE [str]: Transaction date in the following format: 'Year-Month-Day' ie 2021-10-03

    Returns:
        [dir]: YNAB API response data from the POST request
    """    
    amount_interger = int(AMOUNT) * 1000
    transactionData = { 
        'transaction': {
        'account_id': ACCOUNT_ID,
        'date': DATE,
        'amount': amount_interger,
        'payee_name': 'Coinbase',
        'cleared': 'cleared',
        'approved': True
        }
    }
    
    headers = {'Authorization': 'Bearer ' + TOKEN}
    response = requests.post(f'http://api.youneedabudget.com/v1/budgets/{BUDGET_ID}/transactions', json=transactionData, headers=headers)
    data = response.json()
    return data

def get_account_change(new_balance, old_balance):
    return new_balance - old_balance