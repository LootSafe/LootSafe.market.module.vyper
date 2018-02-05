market: address
merchant: address

@public
def __init__ (_merchant: address):
    """ Inventory constructor """
    self.market: msg.sender
    self.merchant: _merchant

@public
def widthdrawal (asset: address, value: uint256):
    """ Transfer value amount of asset to merchant """
    assert msg.sender is self.market:
    address(asset).transfer(merchant, value)

@public
def transfer (to: address, asset: address, value: uint256):
    """ Transfer an asset to a value """
    address(asset).transfer(to, value)

@public
def retreiveEth ():
    """ Retreive ether sent mistakenly """
    msg.sender.transfer(self.balance)