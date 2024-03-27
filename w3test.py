from web3 import Web3, EthereumTesterProvider
import json


w3 = Web3(Web3.WebsocketProvider('wss://polygon-mainnet.g.alchemy.com/v2/kzyx2FaLsl5CHuB4swMESmg-VtusFe7l'))
print("Connected = ",w3.isConnected())
smart_contract_string = open('abi.txt', "r").read()
smart_contract_json = json.loads(smart_contract_string)

myContract = w3.eth.contract(address='0xa5E0829CaCEd8fFDD4De3c43696c57F7D7A678ff', abi=smart_contract_string)

tw = myContract.caller().getAmountsOut(
                    100000000,
                    ['0x1BFD67037B42Cf73acF2047067bd4F2C47D9BfD6' ,
                    '0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174'])
value = tw[1]/1000000
print(" value = ",value)
#myContract.caller().decimals()

from web3 import Web3, EthereumTesterProvider
import json


w3 = Web3(Web3.WebsocketProvider('wss://polygon-mainnet.g.alchemy.com/v2/kzyx2FaLsl5CHuB4swMESmg-VtusFe7l'))
print("Connected = ",w3.isConnected())
smart_contract_string = open('abi.txt', "r").read()
smart_contract_json = json.loads(smart_contract_string)

myContract = w3.eth.contract(address='0x6e98bDeB8000404e6554107ef2b60e82E3BaC3c0', abi=smart_contract_string)

tw = myContract.caller().currentPriceInDollerPerToken()
value = tw/1000000
print(" value = ",value)