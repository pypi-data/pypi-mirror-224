from Zora.url import run_query


query = '''

  query ListCollections($address: String!, $tokenId: String!) {
  token(
    token: {address: $address, tokenId: $tokenId}
  ) {
    token {
      collectionAddress
      collectionName
      description
      lastRefreshTime
      name
      owner
      tokenId
      tokenUrl
      tokenUrlMimeType
      image {
        url
      }
    }
    sales {
      buyerAddress
      collectionAddress
      price {
        usdcPrice {
          decimal
        }
      }
      saleContractAddress
      saleType
      sellerAddress
      tokenId
    }
  }
}




'''


def token_query_extract(address, token):
    #variables = {'address': '0x34d85c9cdeb23fa97cb08333b511ac86e1c4e258', 'tokenId': '60809' }
    variables = {'address': address, 'tokenId': token }
    result = run_query(query, variables)
    return result