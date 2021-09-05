# YNAB & Coinbase Sync
![Python](https://img.shields.io/badge/python-3.9.6-blue?style=for-the-badge&logo=python)
[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?style=for-the-badge)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)

Currently, there is no official way to sync a [Coinbase](https://www.coinbase.com/) account to YNAB ([You Need A Budget](https://www.youneedabudget.com/)) for an accurate view of your Net Worth.

This Python script uses the YNAB and Coinbase APIs to automatically update an investment or tracking account in YNAB. 

## Tech Stack

- [Python 3.9.6](https://www.python.org/)
- [YNAB API](https://api.youneedabudget.com/v1)
- [Coinbase Wallet API](https://developers.coinbase.com/docs/wallet/api-key-authentication)
- [CoinAPI.io](https://www.coinapi.io/)
  
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file. The YNAB and Coinbase API keys are free and the CoinAPI is free up to 100 calls per day.

**YNAB**

`YNAB_TOKEN` 

`BUDGET_ID` 

`ACCOUNT_ID`

**Coinbase**

`COINBASE_KEY` 

`COINBASE_SECRET`

**CoinAPI**

`EXCHANGE_KEY`

## Future Development Plans

- Add color tags to YNAB transactions based on positive or negative account changes
- Add Discord bot integration
- Filter out stablecoins such as USDC from portfolio balance that are used for purchases with the Coinbase debit card

  
## Acknowledgements
- [Coinbase API Troubleshooting](https://stackoverflow.com/questions/66619124/coinbase-api-standard-python-example-returns-invalid-signature)


## License
This project is licensed under [MIT](https://choosealicense.com/licenses/mit/) license.

## Feedback & Support

If you have any feedback or need support, feel free to reach out at rjbaird09@gmail.com
