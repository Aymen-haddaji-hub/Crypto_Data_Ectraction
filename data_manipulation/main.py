#!/usr/bin/python3
"""entrypoint for the program"""

from squeeth import *

# set up network and connect
controller = "0x64187ae08781B09368e6253F9E94951243A493D5"
w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/3e8762476abb40769ed841716fa428e3"))
with open('controller_abi.json') as f:
    abi = json.load(f)
contract = w3.eth.contract(address=controller, abi=abi)

print("ETH price:\t {}$".format(get_eth_price()))
print("Daily funding:\t {}".format(daily_funding(contract)))
print("Implied funding: {}".format(current_implied_funding(contract)))
print("ETH2 price:\t {}".format(eth2_price(contract)))
print("Mark price:\t {}".format(get_mark_price(contract)))
print("Volatility:\t {}".format(implied_volatility(contract)))
