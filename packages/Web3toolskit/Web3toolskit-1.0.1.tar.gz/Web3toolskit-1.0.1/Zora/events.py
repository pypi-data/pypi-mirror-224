from Zora.url import run_query


query = '''

query ListCollections($address: String!,$tokenId: String!,$eventTypes: [EventType!], $limit: Int!) {
  events(
    where: {tokens: {address: $address, tokenId: $tokenId}}
    filter: {eventTypes: $eventTypes}
    sort: {sortKey: CREATED, sortDirection: DESC}
    pagination: {limit: $limit}
  ) {
    nodes {
      collectionAddress
      eventType
      tokenId
      properties {
        ... on ApprovalEvent {
          approved
          approvalEventType
          approvedAddress
          ownerAddress
        }
        ... on MintEvent {
          __typename
          collectionAddress
          originatorAddress
          price {
            usdcPrice {
              decimal
            }
          }
          toAddress
        }
        ... on Sale {
          saleContractAddress
          buyerAddress
          saleType
          sellerAddress
          tokenId
        }
        ... on TransferEvent {
          __typename
          collectionAddress
          fromAddress
          toAddress
        }
        ... on V3AskEvent {
          __typename
          address
          tokenId
          v3AskEventType
        }
        ... on V3ReserveAuctionEvent {
          __typename
          address
          eventType
          properties {
            ... on V3ReserveAuctionV1AuctionBidProperties {
              __typename
              firstBid
              price {
                usdcPrice {
                  decimal
                }
              }
            }
            ... on V3ReserveAuctionV1AuctionCreatedProperties {
              __typename
              auction {
                currency
                duration
                highestBid
                highestBidder
                seller
                sellerFundsRecipient
              }
            }
          }
        }
      }
    }
  }
}




'''


def events_query_results(address,token,type,limit):
    # variables = {'address':'0x34d85c9cdeb23fa97cb08333b511ac86e1c4e258','tokenId':'500','eventTypes': 'APPROVAL_EVENT','limit': 20 }
    variables = {'address': address,'tokenId': token,'eventTypes': type,'limit': limit }
    result = run_query(query, variables)
    return result