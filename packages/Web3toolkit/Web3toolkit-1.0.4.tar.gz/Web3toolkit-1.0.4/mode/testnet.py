import requests


# headers = {
#     "accept": "application/json",
#     "x-api-key": "qGhhOHYHol6KdEzJTJSox3j0gQRQsqV46ksKAZu7"
# }


def search(text):
    response = requests.get(f"https://sepolia.explorer.mode.network/api/v2/search?q={text}")
    return response.json()


def search_direct(text):
    response = requests.get(f"https://sepolia.explorer.mode.network/api/v2/search/check-redirect?q={text}")
    return response.json()


def main_page_transactions():
    response = requests.get(f"https://sepolia.explorer.mode.network/api/v2/main-page/transactions")
    return response.json()


def main_page_blocks():
    response = requests.get(f"https://sepolia.explorer.mode.network/api/v2/main-page/blocks")
    return response.json()


def stats():
    response = requests.get(f"https://sepolia.explorer.mode.network/api/v2/stats")
    return response.json()


def stats_transactions():
    response = requests.get(f"https://sepolia.explorer.mode.network/api/v2/stats/charts/transactions")
    return response.json()


def stats_market():
    response = requests.get(f"https://sepolia.explorer.mode.network/api/v2/stats/charts/market")
    return response.json()


def transactions_hash(hash):
    response = requests.get(f"https://sepolia.explorer.mode.network/api/v2/transactions/{hash}")
    return response.json()


def transactions_hash_token(hash, token):
    response = requests.get(
        f"https://sepolia.explorer.mode.network/api/v2/transactions/{hash}/token-transfers?type={token}")
    return response.json()


def transactions_hash_logs(hash):
    response = requests.get(f"https://sepolia.explorer.mode.network/api/v2/transactions/{hash}/logs")
    return response.json()


def transactions_hash_internal_trans(hash):
    response = requests.get(f"https://sepolia.explorer.mode.network/api/v2/transactions/{hash}/internal-transactions")
    return response.json()


def addresses():
    response = requests.get(f"https://sepolia.explorer.mode.network/api/v2/addresses")
    return response.json()


def address_hash(hash):
    response = requests.get(f"https://sepolia.explorer.mode.network/api/v2/addresses/{hash}")
    return response.json()


def address_hash_counters(hash):
    response = requests.get(f"https://sepolia.explorer.mode.network/api/v2/addresses/{hash}/counters")
    return response.json()


def address_hash_transactions(hash, filter_data):
    response = requests.get(
        f"https://sepolia.explorer.mode.network/api/v2/addresses/{hash}/transactions?filter={filter_data}")
    return response.json()


def address_hash_token_transfer(hash, filter_data, type):
    response = requests.get(
        f"https://sepolia.explorer.mode.network/api/v2/addresses/{hash}/token-transfers?type={type}&filter={filter_data}")
    return response.json()


def address_hash_internal_trans(hash, filter_data):
    response = requests.get(
        f"https://sepolia.explorer.mode.network/api/v2/addresses/{hash}/internal-transactions?filter={filter_data}")
    return response.json()


def address_hash_logs(hash):
    response = requests.get(f"https://sepolia.explorer.mode.network/api/v2/addresses/{hash}/logs")
    return response.json()


def address_hash_token_balances(hash):
    response = requests.get(f"https://sepolia.explorer.mode.network/api/v2/addresses/{hash}/token-balances")
    return response.json()


def address_hash_tokens(hash, filter_data):
    response = requests.get(f"https://sepolia.explorer.mode.network/api/v2/addresses/{hash}/tokens?type={filter_data}")
    return response.json()


def address_hash_withdraw(hash):
    response = requests.get(f"https://sepolia.explorer.mode.network/api/v2/addresses/{hash}/withdrawals")
    return response.json()


def tokens(token, type_data):
    response = requests.get(f"https://sepolia.explorer.mode.network/api/v2/tokens?q={token}&type={type_data}")
    return response.json()


def token_hash(hash):
    response = requests.get(f"https://sepolia.explorer.mode.network/api/v2/tokens/{hash}")
    return response.json()


def token_hash_transfers(hash):
    response = requests.get(f"https://sepolia.explorer.mode.network/api/v2/tokens/{hash}/transfers")
    return response.json()


def token_hash_holders(hash):
    response = requests.get(f"https://sepolia.explorer.mode.network/api/v2/tokens/{hash}/holders")
    return response.json()


def token_hash_counters(hash):
    response = requests.get(f"https://sepolia.explorer.mode.network/api/v2/tokens/{hash}/counters")
    return response.json()


def token_hash_instances(hash):
    response = requests.get(f"https://sepolia.explorer.mode.network/api/v2/tokens/{hash}/instances")
    return response.json()


def smart_contracts(filter_data):
    response = requests.get(f"https://sepolia.explorer.mode.network/api/v2/smart-contracts?filter={filter_data}")
    return response.json()


def smart_contracts_counters():
    response = requests.get(f"https://sepolia.explorer.mode.network/api/v2/smart-contracts/counters")
    return response.json()


def smart_contracts_hash(hash):
    response = requests.get(f"https://sepolia.explorer.mode.network/api/v2/smart-contracts/{hash}")
    return response.json()


def smart_contracts_hash_read_abi(hash):
    response = requests.get(f"https://sepolia.explorer.mode.network/api/v2/smart-contracts/{hash}/methods-read")
    return response.json()


def smart_contracts_hash_write_abi(hash):
    response = requests.get(f"https://sepolia.explorer.mode.network/api/v2/smart-contracts/{hash}/methods-write")
    return response.json()
