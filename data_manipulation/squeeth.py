#!/usr/bin/python3
"""
    Python script that extract the data from a
    deployed Squeeth protocol smart contracts
"""

from web3 import Web3
import json
import requests


def get_eth_price():
    """
        get ethereum price from yahoo finance
    """
    url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
    response = requests.get(url)
    data = json.loads(response.text)
    return data['ethereum']['usd']

def eth2_price(contract):
    """
        Function that return ethereum layer 2 price
    """
    eth2_price = contract.functions.getIndex(1).call()
    p = str(eth2_price)[:8]
    return "{:,}".format(int(p))


def get_mark_price(contract):
    """
        Function that extract the data from a
        deployed Squeeth protocol smart contracts
    """
    mark = contract.functions.getDenormalizedMark(1).call()
    x = str(mark)[:8]
    return "{:,}".format(int(x))

def daily_funding(contract):
    """
        Function that extract the data from a
        deployed Squeeth protocol smart contracts
    """
    daily = contract.functions.getDenormalizedMark(86400).call()
    last = contract.functions.getDenormalizedMark(1800).call()
    h_dail_funding = (daily - last) / 10000000000000000
    return round(h_dail_funding, 2)

def current_implied_funding(contract):
    """
        Function that extract the data from a
        deployed Squeeth protocol smart contracts
    """
    daily = contract.functions.getDenormalizedMark(86400).call()
    last = contract.functions.getDenormalizedMark(1).call()
    implied_funding = (daily - last) / 10000000000000000
    return round(implied_funding, 2)

def implied_volatility(contract):
    """
        Function that extract the data from a
        deployed Squeeth protocol smart contracts
    """
    daily = contract.functions.getDenormalizedMark(86400).call()
    eth_price = contract.functions.getIndex(1).call()
    implied_volatility = ((daily - get_eth_price()) / eth_price) * 100
    return implied_volatility 