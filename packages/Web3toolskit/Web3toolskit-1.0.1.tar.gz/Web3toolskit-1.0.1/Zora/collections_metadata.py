from Zora.url import run_query


query = '''

  query ListCollections($collectionAddresses: [String!]!) {
  collections(
    sort: {sortKey: CREATED, sortDirection: ASC}
    networks: {chain: MAINNET, network: ETHEREUM}
    where: {collectionAddresses: $collectionAddresses}
  ) {
    nodes {
      address
      name
      symbol
      totalSupply
      networkInfo {
        chain
        network
      }
      attributes {
        traitType
        valueMetrics {
          count
          percent
          value
        }
      }
      description
    }
  }
}


'''

def collection_query_results(address):
    variables = {'collectionAddresses': address}
    result = run_query(query, variables)
    return result