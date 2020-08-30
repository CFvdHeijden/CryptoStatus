import secrets
import API
import ETHapp
import os
import time

#Convert to float for multiplying
#Use varialbes from ETHapp and API modules to calculate value of crypto in EUR
balanceLinkInEuro = float(ETHapp.myChainlinkBalance) * API.rateLink
balanceLinkInEuro = round(balanceLinkInEuro, 2)
#print(balanceLinkInEuro)
print()
print("PRICES             ", "             Value of my tokens:")
print("-------------------------------------------------------")
print("LINK price is eur: ", API.rateLink, "       LINK balance: ", balanceLinkInEuro)

balanceLendInEuro = float(ETHapp.myEthLendBalance) * API.rateLend
balanceLendInEuro = round(balanceLendInEuro, 2)
#print(balanceLendInEuro)
print("LEND price is eur: ", API.rateLend, "        LEND balance: ", balanceLendInEuro)

balanceEthInEuro = ETHapp.balance1 + ETHapp.balance2
balanceEthInEuro = float(balanceEthInEuro) * API.rateEth
balanceEthInEuro = round(balanceEthInEuro, 2)
#print(balanceEthInEuro)
print("ETH  price is eur: ", API.rateEth, "      ETH  balance: ", balanceEthInEuro)
print()

#Calculate RoI in EUR & % on moment of execution!!
totalCryptoInEuro = balanceLinkInEuro + balanceLendInEuro + balanceEthInEuro
profit = totalCryptoInEuro - secrets.investment
profit = round(profit, 2) 
#Do this for ETH, LINK & LEND

#Print the results:x    
print("Result:")
print("-------------------------------------------------------")
print("RoI in euro's:     ", profit)
percentage = totalCryptoInEuro / secrets.investment * 100
percentage = percentage - 100
percentage = round(percentage, 2)
print("RoI in %:          ", percentage)
print()
