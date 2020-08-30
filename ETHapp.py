from web3 import Web3
from decimal import Decimal
import requests

#Import secrets module for public keys & api keys
import secrets

#Connect to ethereum blockchain using infura and web3 module
web3 = Web3(Web3.HTTPProvider(secrets.infura_url))

#Contract addresses of the ERC20 tokens and etherscan global url:
chainlinkAddress = "0x514910771af9ca656af840dff83e8264ecf986ca"
aaveAddress = "0x80fB784B7eD66730e8b1DBd9820aFD29931aab03"
url_etherscan = "https://api.etherscan.io/api"

#Iterate over list of contract addresses to collect ABI's and store them in a list
#called responses
contractAddresses = ["0x514910771af9ca656af840dff83e8264ecf986ca", "0x80fB784B7eD66730e8b1DBd9820aFD29931aab03"]
responses = []
for i in contractAddresses:
	API_ENDPOINT = url_etherscan+"?module=contract&action=getabi&address="+str(chainlinkAddress)+"&apikey="+str(secrets.MyApiKeyToken)
	r = requests.get(url = API_ENDPOINT)
	responses.append(r.json())

#Create LINK and EthLend instances and use them as variables in the balanceOf function in the
#ERC20 contracts. Call the function and creates variables that hold my balance!!!

#Also uses fromWei and round functions to create 2 decimal numbers for readability
#Improve by creating a loop for this.
chainlinkInstance = web3.eth.contract(
	address = Web3.toChecksumAddress(chainlinkAddress), 
	abi = responses[0]["result"]
)
myChainlinkBalance = chainlinkInstance.functions.balanceOf(secrets.address1).call({'from':secrets.address1})
myChainlinkBalance = web3.fromWei(myChainlinkBalance, 'ether')
myChainlinkBalance = round(myChainlinkBalance, 2)
#print("my LINK:          ", myChainlinkBalance)

aaveInstance = web3.eth.contract(
	address = Web3.toChecksumAddress(aaveAddress), 
	abi = responses[1]["result"]
)
myEthLendBalance = aaveInstance.functions.balanceOf(secrets.address1).call({'from':secrets.address1})
myEthLendBalance = web3.fromWei(myEthLendBalance, 'ether')
myEthLendBalance = round(myEthLendBalance, 2)
#print("my EthLend:       ", myEthLendBalance)

balance1 = web3.eth.getBalance(secrets.address1)
balance1 = web3.fromWei(balance1, 'ether')
balance1 = round(balance1, 2)
#print("my ETH:           ", balance1)

balance2 = web3.eth.getBalance(secrets.address2)
balance2 = web3.fromWei(balance2, 'ether')
balance2 = round(balance2, 2)
#print("my ETH in ledger: ", balance2)