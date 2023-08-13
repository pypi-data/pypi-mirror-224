



from Zora.url import run_query


query = '''
    query ListCollections($collectionAddresses: [String!]!) {
    offchainOrders(
    where: {collectionAddresses: $collectionAddresses}
    networks: {network: ETHEREUM, chain: MAINNET}
    sort: {sortKey: USDC_PRICE, sortDirection: ASC}
  ) {
    nodes {
      offchainOrder {
        calldata
        contractAddress
        endTime
        price {
          usdcPrice {
            decimal
          }
        }
        tokenId
        startTime
        orderType
        offerer
      }
    }
  }
}




'''

def off_chain_query_results(address):
    variables = {'collectionAddresses': address}
    result = run_query(query, variables)
    return result