import requests
from requests.auth import HTTPBasicAuth

Headers = {
    "accept": "application/json",
}


class BalancesApi:
    def __init__(self, chain_name: str, wallet_address: str, api_key: str):
        self.chain_name = chain_name,
        self.wallet_address = wallet_address,
        self.api_key = api_key
        self.url = f'https://api.covalenthq.com/v1/{chain_name}/address/{wallet_address}/'

    def get_token_balance(self, quote_currency: str = '',
                          nft: bool = False,
                          no_nft_fetch: bool = False,
                          no_spam: bool = False,
                          no_nft_asset_metadata: bool = False):
        auth = HTTPBasicAuth(self.api_key, '')
        url = self.url + f'balances_v2/?nft={nft}&no-nft-fetch={no_nft_fetch}&no-spam={no_spam}' \
                         f'&no-nft-asset-metadata={no_nft_asset_metadata}'
        if len(quote_currency):
            url += f'&quote-currency={quote_currency}'
        response = requests.get(url, auth=auth, headers=Headers)
        return response.json()

    def get_historical_token_balance(self, quote_currency: str = '',
                                     nft: bool = False,
                                     no_nft_fetch: bool = False,
                                     no_spam: bool = False,
                                     no_nft_asset_metadata: bool = False,
                                     block_height: int = 0,
                                     date: int = 0):
        auth = HTTPBasicAuth(self.api_key, '')
        url = self.url + f'historical_balances/?nft={nft}&no-nft-fetch={no_nft_fetch}&no-spam={no_spam}' \
                         f'&no-nft-asset-metadata={no_nft_asset_metadata}'
        if len(quote_currency):
            url += f'&quote-currency={quote_currency}'
        if block_height != 0:
            url += f'block-height={block_height}'
        if date != 0:
            url += f'date={date}'
        response = requests.get(url, auth=auth, headers=Headers)
        return response.json()

    def get_historical_portfolio(self, quote_currency: str = '', days: int = 0):
        auth = HTTPBasicAuth(self.api_key, '')
        url = self.url + f'portfolio_v2/'
        if days != 0:
            url += f'?days={days}'
        if len(quote_currency):
            url += '?' if '?' not in url else '&'
            url += f'quote-currency={quote_currency}'
        print('p', url)
        response = requests.get(url, auth=auth, headers=Headers)
        return response.json()

    def get_ERC20_token_transfer(self, contract_address: str,
                                 quote_currency: str = '',
                                 starting_block: int = 0,
                                 ending_block: int = 0):
        auth = HTTPBasicAuth(self.api_key, '')
        url = self.url + f'transfers_v2/?contract-address={contract_address}/'
        if starting_block != 0:
            url += f'&starting-block={starting_block}&ending-block={ending_block}'
        if len(quote_currency):
            url += f'&quote-currency={quote_currency}'
        print('erc20', url)
        response = requests.get(url, auth=auth, headers=Headers)
        return response.json()

    def get_token_holders(self, quote_currency: str = '',
                          block_height: int = 0,
                          page_size: str = 0,
                          page_number: int = 0):
        auth = HTTPBasicAuth(self.api_key, '')
        url = f'https://api.covalenthq.com/v1/{self.chain_name}/address/token_holders_v2/'
        if block_height != 0:
            url += f'?block-height={block_height}'
        if page_size != 0:
            url += '?' if '?' not in url else '&'
            url += f'page-size={page_size}&page-number={page_number}'
        if len(quote_currency):
            url += '?' if '?' not in url else '&'
            url += f'quote-currency={quote_currency}'
        print('hol', url)
        response = requests.get(url, auth=auth, headers=Headers)
        return response.json()
