import urllib.request, json, pprint, sys, time
from collections import defaultdict
from datetime import datetime

# Search from block 5939000
# Search to block 5975977

contractAddressList = ['0x0777F76D195795268388789343068e4fCd286919', '0x08dBf4f942ba8cd7871C13addEfdfFEf3E5a8035', '0xCA6746f65D53D2dF5022b5d775817e62e8462690', 
                        '0x015531A044BAe03bF4dAB1ceabfc232a969b7175', '0x482Cf6A9d6b23452C81d4D0f0f139C1414963f89', '0x84487E50dB6317E5e834d89d0e81Fd873462Ea47',
                        '0xe5dC9d1B58fD5a95fC20A6c6AfAA76d44D70A7DF', '0x6e0051C750b81f583f42f93A48d56497779992d8', '0xc47D7d42E44b2e04c83a45cF45898E597A0c2311',
                        '0x80b3075410Ee52C520DD203f60206F633D27A109', '0x6c5DC1dcdA3d309a6e919e6D0965f197E0Fc1913', '0x5789e2B5460caE9329d93A78511E2aC49f98a1f6',
                        '0x1e891C587b345ab02A31b57c1F926fB08913d10D', '0x314495517F380CEb7c498A35739E40864240ADCf', '0x80391307F1B08Cc068Fa1D1b77513B98C36DFbfa',
                        '0x000983ba1A675327F0940b56c2d49CD9c042DFBF']
listOfUniqueAddresses = []
contractsChecked = 0

for i in contractAddressList:
    apiUrl = 'http://api.etherscan.io/api?module=account&action=txlist&address=' + i + '&startblock=0&endblock=6050000&sort=asc'

    print('Fetching Contract Info...')
    with urllib.request.urlopen(apiUrl) as url:
        transactionHistory = json.load(url)
    print('Done.')

    for transaction in transactionHistory['result']:
        if transaction['from'] not in listOfUniqueAddresses:
            listOfUniqueAddresses.append(transaction['from'])

    contractsChecked += 1
    print('Checked ' + str(contractsChecked) + ' contracts.') 
print('Total unique addresses: ' + str(len(listOfUniqueAddresses)))

# iterations = 0
# firstPhoenix = 0
# lightBidding = 0
# for i in listOfUniqueAddresses:
#     guApiUrl = 'https://api.godsunchained.com/user/' + str(i) + '/card'

#     with urllib.request.urlopen(guApiUrl) as url:
#         userInfo = json.load(url)

#     if userInfo is None:
#         continue

#     for card in userInfo:
#         if card['proto'] == 380:
#             firstPhoenix += 1
#         if card['proto'] == 381:
#             lightBidding += 1
#     iterations += 1
#     print('Address ' + str(iterations) + ' out of ' + str(len(listOfUniqueAddresses)))

# print('Total First Phoenix Cards: ' + str(firstPhoenix))
# print('Total Lights Bidding Cards: ' + str(lightBidding))