import requests
from requests.auth import HTTPBasicAuth

Headers = {
    "accept": "application/json",
}


class NFTApis:
    def __init__(self, chain_name, api_key):
        self.chain_name = chain_name
        self.api_key = api_key
        self.base_url = f'https://api.covalenthq.com/v1/{chain_name}'

    def get_nfts(self, wallet_address,
                 no_spam: bool = False,
                 no_nft_asset_metadata: bool = False,
                 with_uncached: bool = False):
        auth = HTTPBasicAuth(self.api_key, '')
        url = self.base_url + f'/address/{wallet_address}/balances_nft/'
        url += f'?no-spam={no_spam}&no-nft-asset-metadata={no_nft_asset_metadata}' \
               f'&with-uncached={with_uncached}'
        response = requests.get(url, auth=auth, headers=Headers)
        return response.json()

    def get_nfts_from_contract(self, contract_address: str,
                               no_metadata: bool = False,
                               with_uncached: bool = False,
                               page_size: int = 0,
                               page_number: int = 0,
                               traits_filter: str = '',
                               values_filter: str = '',
                               ):
        auth = HTTPBasicAuth(self.api_key, '')
        url = self.base_url + f'/nft/{contract_address}/metadata/'
        url += f'?no-metadata={no_metadata}&page-size={page_size}&page_number={page_number}' \
               f'&traits-filter={traits_filter}&values-filter={values_filter}' \
               f'&with-uncached={with_uncached}'
        response = requests.get(url, auth=auth, headers=Headers)
        return response.json()

    def get_single_nft_from_contract(self, contract_address: str,
                                     token_id: str,
                                     no_metadata: bool = False,
                                     with_uncached: bool = False
                                     ):
        auth = HTTPBasicAuth(self.api_key, '')
        url = self.base_url + f'/nft/{contract_address}/metadata/{token_id}/'
        url += f'?no-metadata={no_metadata}&with-uncached={with_uncached}'
        response = requests.get(url, auth=auth, headers=Headers)
        return response.json()

    def get_nft_transactions(self, contract_address: str,
                             token_id: str,
                             no_spam: bool = False):
        auth = HTTPBasicAuth(self.api_key, '')
        url = self.base_url + f'/tokens/{contract_address}/nft_transactions/{token_id}/'
        url += f'?no-spam={no_spam}'
        response = requests.get(url, auth=auth, headers=Headers)
        return response.json()

    def get_traits(self, collection_contract: str):
        auth = HTTPBasicAuth(self.api_key, '')
        url = self.base_url + f'nft/{collection_contract}/traits/'
        response = requests.get(url, auth=auth, headers=Headers)
        return response.json()

    def get_traits_summary(self, collection_contract: str):
        auth = HTTPBasicAuth(self.api_key, '')
        url = self.base_url + f'nft/{collection_contract}/traits_summary/'
        response = requests.get(url, auth=auth, headers=Headers)
        return response.json()

    def get_attributes_for_traits(self, collection_contract: str, trait: str):
        auth = HTTPBasicAuth(self.api_key, '')
        url = self.base_url + f'/nft/{collection_contract}/traits/{trait}/attributes/'
        response = requests.get(url, auth=auth, headers=Headers)
        return response.json()

    def get_collections(self, no_spam: bool = False,
                        page_size: int = 0,
                        page_number: int = 0, ):
        auth = HTTPBasicAuth(self.api_key, '')
        url = self.base_url + f'/nft/collections/'
        url += f'?no-spam={no_spam}&page-size={page_size}&page-number={page_number}'
        response = requests.get(url, auth=auth, headers=Headers)
        return response.json()

    def check_ownership_in_collections(self, wallet_address: str, collection_contract: str):
        auth = HTTPBasicAuth(self.api_key, '')
        url = self.base_url + f'/address/{wallet_address}/collection/{collection_contract}/'
        response = requests.get(url, auth=auth, headers=Headers)
        return response.json()

    def check_ownership_in_collections_for_token(self, wallet_address: str,
                                                 collection_contract: str,
                                                 token_id:str):
        auth = HTTPBasicAuth(self.api_key, '')
        url = self.base_url + f'/address/{wallet_address}/collection/{collection_contract}/token/{token_id}/'
        response = requests.get(url, auth=auth, headers=Headers)
        return response.json()

