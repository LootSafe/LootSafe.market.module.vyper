
owner: address

""" Represents a trade offer """
offer: {
    offer: address,
    request: address,
    offerValue: num256,
    requestValue: num256,
    merchant: address,
    customer: address,
    settleTime: uint,
    settled: bool
}

inventories: address[address]
trades: bytes32[offer]
tradesByMerchant: address[[bytes32]]

tradeIds: [bytes32]

@public
def __init__ ():
    self.owner = msg.sender

"""
Internal Functions
"""

@private
def _getOutstandingValue (asset: address, merchant: address) -> num256:
    """ Check how many of an asset a merchant has locked in offers """
    merchantTrades = tradesByMerchant[merchant]
    
    outstandingValue = 0

    if len(merchantTrades) > 0:
        for i in range(0, len(merchantTrades)):
            merchantOffer = trades[merchantTrades[i]]
            if offer.offer is asset and not offer.settled:
                assert offer.offerValue <= outstandingValue
                outstandingValue = outstandingValue - offer.offerValue

    return outstandingValue


@private
def _getBalance(asset: address, merchant: address) -> address:
    """ Return a balance """
    return address(asset).balanceOf(inventories[merchant])

"""
Getter Functions
"""

@public
@constant
def getTradesByMerchant (merchant: address) -> [bytes32]:
    """ Get a list of trades by a specific merchant """ 
    return tradesByMerchant[merchant]

@public
@constant
def getTrades () -> _trades:
    """ Get all market trades """
    return tradeIds

@public
@constant
def getTrade (tradeId: bytes32) -> [address, request, offerValue, requestValue, merchant, customer, settleTime, settled]:
    """ Get a specific trade """
    tradeOffer = trades[tradeId]
    return [
        tradeOffer.offer,
        tradeOffer.request,
        tradeOffer.offerValue,
        tradeOffer.requestValue,
        tradeOffer.merchant,
        tradeOffer.customer,
        tradeOffer.settleTime,
        tradeOffer.settled
    ]

@public
@constant
def getMyInventory () -> address:
    """ Get inventory of sender """
    return inventories[msg.sender]

"""
Public Functions
"""


@public
@payable
def ():
    assert msg.value is 0
    assert not inventories[msg.sender]

    inventories[msg.sender] = address(
        """ Create inventory contract """
    )