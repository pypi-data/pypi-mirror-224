from Zora.url import run_query


query = '''

  query ListCollections($collectionAddresses: [String!]!, $limit: Int!) {
  aggregateStat {
    floorPrice(
      where: {collectionAddresses: $collectionAddresses}
      networks: {chain: MAINNET, network: ETHEREUM}
    )
    nftCount(
      where: {collectionAddresses: $collectionAddresses}
      networks: {chain: MAINNET, network: ETHEREUM}
    )
    ownerCount(
      where: {collectionAddresses: $collectionAddresses}
      networks: {chain: MAINNET, network: ETHEREUM}
    )
    ownersByCount(
      where: {collectionAddresses: $collectionAddresses}
      networks: {chain: MAINNET, network: ETHEREUM}
      pagination: {limit: $limit}
    ) {
      nodes {
        count
        owner
      }
    }
    salesVolume(
      networks: {chain: MAINNET, network: ETHEREUM}
      where: {collectionAddresses: $collectionAddresses}
    ) {
      chainTokenPrice
      totalCount
      usdcPrice
    }
  }
}


'''


def agg_stats_query_results(address, limit):
    #variables = {'collectionAddresses': '0xb47e3cd837ddf8e4c57f05d70ab865de6e193bbb', 'limit': 10}
    variables = {'collectionAddresses': address, 'limit': limit}
    result = run_query(query, variables)
    return result
       