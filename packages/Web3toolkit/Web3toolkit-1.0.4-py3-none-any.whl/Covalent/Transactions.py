import requests
from requests.auth import HTTPBasicAuth

Headers = {
    "accept": "application/json",
}


class TransactionsApi:
    def __init__(self, chain_name, api_key):
        self.chain_name = chain_name
        self.api_key = api_key
        self.base_url = f'https://api.covalenthq.com/v1/{chain_name}'

    def get_transactions(self, tx_hash: str,
                         quote_currency: str = '',
                         no_logs: bool = False,
                         with_dex: bool = False,
                         with_nft_sales: bool = False,
                         with_lending: bool = False):
        auth = HTTPBasicAuth(self.api_key, '')
        url = self.base_url + f'/transaction_v2/{tx_hash}/'
        url += f'?no-logs={no_logs}&with_dex={with_dex}&with-nft-sales={with_nft_sales}' \
               f'&with-lending={with_lending}'
        if len(quote_currency):
            url += f'&quote-currency={quote_currency}'
        response = requests.get(url, auth=auth, headers=Headers)
        return response.json()

    def get_transaction_summary_from_address(self, wallet_address: str):
        auth = HTTPBasicAuth(self.api_key, '')
        url = self.base_url + f'/address/{wallet_address}/transactions_summary/'
        response = requests.get(url, auth=auth, headers=Headers)
        return response.json()

    def get_earliest_transactions(self, wallet_address: str,
                                  quote_currency: str = '',
                                  no_logs: bool = False):
        auth = HTTPBasicAuth(self.api_key, '')
        url = self.base_url + f'/bulk/transactions/{wallet_address}/'
        url += f'?no-logs={no_logs}'
        if len(quote_currency):
            url += f'&quote-currency={quote_currency}'
        response = requests.get(url, auth=auth, headers=Headers)
        return response.json()

    def get_recent_transactions(self, wallet_address: str,
                                quote_currency: str = '',
                                no_logs: bool = False):
        auth = HTTPBasicAuth(self.api_key, '')
        url = self.base_url + f'/address/{wallet_address}/transactions_v3/'
        url += f'?no-logs={no_logs}'
        if len(quote_currency):
            url += f'&quote-currency={quote_currency}'
        response = requests.get(url, auth=auth, headers=Headers)
        return response.json()

    def get_paginated_transactions(self, wallet_address: str,
                                   page: int,
                                   quote_currency: str = '',
                                   no_logs: bool = False):
        auth = HTTPBasicAuth(self.api_key, '')
        url = self.base_url + f'/address/{wallet_address}/transactions_v3/page/{page}/'
        url += f'?no-logs={no_logs}'
        if len(quote_currency):
            url += f'&quote-currency={quote_currency}'
        response = requests.get(url, auth=auth, headers=Headers)
        return response.json()

    def get_all_transactions_in_block(self, block_height: str,
                                      quote_currency: str = '',
                                      no_logs: bool = False):
        auth = HTTPBasicAuth(self.api_key, '')
        url = self.base_url + f'/block/{block_height}/transactions_v3/'
        url += f'?no-logs={no_logs}'
        if len(quote_currency):
            url += f'&quote-currency={quote_currency}'
        response = requests.get(url, auth=auth, headers=Headers)
        return response.json()

    def get_all_transactions_in_block_by_page(self, block_height: str,
                                              page: int,
                                              quote_currency: str = '',
                                              no_logs: bool = False):
        auth = HTTPBasicAuth(self.api_key, '')
        url = self.base_url + f'/block/{block_height}/transactions_v3/page/{page}/'
        url += f'?no-logs={no_logs}'
        if len(quote_currency):
            url += f'&quote-currency={quote_currency}'
        response = requests.get(url, auth=auth, headers=Headers)
        return response.json()

    def get_bulk_time_bucket_transactions(self, wallet_address: str,
                                          time_bucket: int,
                                          quote_currency: str = '',
                                          no_logs: bool = False):
        auth = HTTPBasicAuth(self.api_key, '')
        url = self.base_url + f'/bulk/transactions/{wallet_address}/{time_bucket}/'
        url += f'?no-logs={no_logs}'
        if len(quote_currency):
            url += f'&quote-currency={quote_currency}'
        response = requests.get(url, auth=auth, headers=Headers)
        return response.json()
