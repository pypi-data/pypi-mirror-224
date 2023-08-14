from Zora.url import run_query



query = '''




  query ListCollections($saleTypes: [SaleType!], $limit: Int!, $collectionAddresses: [String!]!, $sortKey: SaleSortKey! ) {
  sales(
    filter: {saleTypes: $saleTypes}
    networks: {chain: MAINNET, network: ETHEREUM}
    pagination: {limit: $limit}
    sort: {sortKey: $sortKey, sortDirection: DESC}
    where: {collectionAddresses: $collectionAddresses}
  ) {
    nodes {
      sale {
        buyerAddress
        collectionAddress
        networkInfo {
          chain
          network
        }
        price {
          usdcPrice {
            decimal
          }
        }
        saleContractAddress
        saleType
        sellerAddress
        tokenId
        transactionInfo {
          blockTimestamp
        }
      }
      token {
        collectionAddress
        collectionName
        description
        image {
          url
          size
        }
        metadata
        mintInfo {
          originatorAddress
          toAddress
        }
        name
        owner
      }
    }
  }
}



'''


def sales_query_results(address, limit, types, sort_by):
    variables = {'collectionAddresses': address, 'limit': limit, 'saleTypes': types, 'sortKey': sort_by, }
    result = run_query(query, variables)
    return result