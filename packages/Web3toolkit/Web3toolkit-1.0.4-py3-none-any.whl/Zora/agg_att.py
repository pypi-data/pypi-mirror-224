from Zora.url import run_query


query = '''

  query ListCollections($address: String!, $tokenId: String!) {
  aggregateAttributes(
    where: {tokens: {address: $address, tokenId: $tokenId }}
  ) {
    traitType
    valueMetrics {
      count
      percent
      value
    }
  }
}

'''


def agg_att_query_results(address, token):
    #variables = {'address': '0x60e4d786628fea6478f785a6d7e704777c86a7c6', 'tokenId': '7077'}
    variables = {'address':  address, 'tokenId': token}
    result = run_query(query, variables)
    return result