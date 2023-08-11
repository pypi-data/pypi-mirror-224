from web3 import Web3
from web3.eth import AsyncEth

w3 = Web3(Web3.AsyncHTTPProvider("http://127.0.0.1:8545"),
          modules={'eth': (AsyncEth,)}, middlewares=[])

