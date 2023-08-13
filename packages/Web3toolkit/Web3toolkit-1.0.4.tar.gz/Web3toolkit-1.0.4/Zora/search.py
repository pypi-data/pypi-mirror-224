from Zora.url import run_query


query = '''

  query ListCollections( $limit: Int!, $text: String!) {
  search(
    pagination: {limit: $limit}
    query: {text: $text}
    filter: {entityType: COLLECTION}
  ) {
    nodes {
      collectionAddress
      description
      entityType
      name
      tokenId
      entity {
        ... on Collection {
          name
          symbol
          address
          description
          totalSupply
          networkInfo {
            chain
            network
          }
        }
      }
    }
    pageInfo {
      hasNextPage
      limit
    }
  }
}




'''


def search_query_results(text, limit):
    variables = {'text': text, 'limit': limit }
    result = run_query(query, variables)
    return result