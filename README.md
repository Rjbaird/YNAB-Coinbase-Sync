# Connecting Coinbase to YNAB

https://docs.pro.coinbase.com/?python#introduction

https://www.reddit.com/r/CoinBase/comments/foebre/python_api/flhz510/

https://realpython.com/how-to-make-a-discord-bot-python/

**Action:** 
I want to have an accurate view of my bet worth in YNAB

**The Problem:** 
Currently, there is no official way to sync my Coinbase to my YNAB account. This gives me an incorrect view of my net worth

**The Solution:** 
Create a python script that gets my portfolio balance in Coinbase and makes a transaction/adjustment to an investment account in YNAB.

The script should run every day at 8am.

**Full Spec**
- The script will run from the main function in main.py
- The main function sets all the environmental variables it needs for the following functions
- coinbase.py uses the Coinbase API to get my account balance for each wallet in Coinbase.
- It contains a function that loops through each wallet balance and creates a total account balance from Coinbase

- Next, the main funciton will run functions from the YNAB.py file. The YNAB.py contains functions that will take the data from the coinbase.py script and do the following:
    - Use the YNAB API to get the current crypto account balance in YNAB
    - Calculate how much needs to be adjusted in the YNAB account
    - Create an transaction object for the YNAB Adjustment.
    - Send transaction object to YNAB
    - Return the adjustment amount made to YNAB
- The create_message function creates a message based on the account adjustment. 
    - An increase in the account account will create the following message:
        - 'Coinbase adjustment created! Your Coinbase account is now at {current value}, up ${dollar amount} from last week 🥳'
    - A decrease in the the account will create the following message:
        - 'Coinbase adjustment created! Your Coinbase account is now at {current value}, down -${dollar amount} from last week 💩'
- Finally, the main funciton will call the Discord send_message function in bot.py
- bot.py will send the message thru the Discord API with the adjustment amount to my Bairrya server as Money Bot

**Tech Stack**
- Python
- [YNAB API](https://api.youneedabudget.com/v1)
- [Discord API](https://realpython.com/how-to-make-a-discord-bot-python/)
- [Coinbase Wallet API](https://developers.coinbase.com/docs/wallet/api-key-authentication)
- [CoinAPI.io](https://www.coinapi.io/)

