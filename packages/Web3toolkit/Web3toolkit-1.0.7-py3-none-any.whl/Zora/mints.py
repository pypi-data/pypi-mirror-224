#import requests
from Zora.url import run_query


query = '''

 query ListCollections($sortKey: MintSortKey!, $limit: Int!, $minterAddresses: [String!]) {
  mints(
    pagination: {limit: $limit}
    sort: {sortKey: $sortKey, sortDirection: DESC}
    where: {minterAddresses: $minterAddresses}
  ) {
    nodes {
      mint {
        collectionAddress
        originatorAddress
        price {
          usdcPrice {
            decimal
          }
        }
        toAddress
        tokenId
      }
      token {
        collectionAddress
        collectionName
        description
        name
        owner
        tokenId
        image {
          url
        }
      }
    }
  }
}


'''


def mints_query_results(mint_address,limit,sort_key):

    variables = {'minterAddresses': mint_address, 'limit': limit,  'sortKey': sort_key, }
    result = run_query(query, variables)
    return result