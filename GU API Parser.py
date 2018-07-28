import urllib.request, json, pprint, sys, time
from collections import defaultdict
from datetime import datetime

userAddress = input('Enter Ethereum Address: ')
# 0x69b22E50dd4BE4cdfCED71F8E3aaa8a4871a1c67 # Primary
# 0x212B738551cfA71bEABEE191dE20f5C0783F582b # Alt
# 0x0008d343091EF8BD3EFA730F6aAE5A26a285C7a2 # Address with most cards.
# 0xe8ac0cf3a9cea74e7653a863499e8e661440be13 # Most legendary packs
# 0x48E809844ff6E17d5e2043d10a85bCBbB71F0FaE # Danny#1908
# 0xb6bE4De7F37baE20085d830A28982bE8aD19052b # Saltz
# 0xE4a8dfcA175cDcA4Ae370f5b7aaff24bD1C9C8eF # borovan - bought 100 shiny

apiUrl = 'https://api.godsunchained.com/user/' + userAddress + '/card/opened'

if userAddress == '':
    apiUrl = 'https://api.godsunchained.com/card'
    cycles = 0
    while True:
        print('Fetching...')
        with urllib.request.urlopen(apiUrl) as url:
            userInfo = json.load(url)
        with urllib.request.urlopen("https://pastebin.com/raw/e5rv9mep") as url:
            cardInfo = json.load(url)
        print('Done.')

        outputList = []
        totalCommons = 0
        totalRares = 0
        totalEpics = 0
        totalLegendaries = 0
        totalMythics = 0
        totalPlain = 0
        totalShadow = 0
        totalGold = 0
        totalDiamond = 0
        totalZeroPurity = 0
        totalPerfectPlain = 0
        totalPerfectShadow = 0
        totalPerfectGold = 0
        totalPerfectDiamond = 0

        outputList.append(pprint.pformat(('Time: ' + str(datetime.now()))))

        for card in userInfo:
            for cardNumber in cardInfo:
                if card['proto'] == cardInfo[cardNumber]['GLOBALID']:
                    if cardInfo[cardNumber]['rarity'] == 'Oi.Common':
                        totalCommons += 1
                    if cardInfo[cardNumber]['rarity'] == 'Oi.Rare':
                        totalRares += 1
                    if cardInfo[cardNumber]['rarity'] == 'Oi.Epic':
                        totalEpics += 1
                    if cardInfo[cardNumber]['rarity'] == 'Oi.Legendary':
                        totalLegendaries += 1
                    if cardInfo[cardNumber]['rarity'] == 'Oi.Mythic':
                        totalMythics += 1
                        print('SOMEBODY HAS A MYTHIC! User: ' + card['user'])
            if 0 <= card['purity'] <= 999:
                totalPlain += 1
            if 1000 <= card['purity'] <= 1999:
                totalShadow += 1
            if 2000 <= card['purity'] <= 2999:
                totalGold += 1
            if 3000 <= card['purity'] <= 3999:
                totalDiamond += 1
            if card['purity'] == 0:
                totalZeroPurity += 1
            if card['purity'] == 999:
                totalPerfectPlain += 1
            if card['purity'] == 1999:
                totalPerfectShadow += 1
            if card['purity'] == 2999:
                totalPerfectGold += 1
            if card['purity'] == 3999:
                totalPerfectDiamond += 1
                outputList.append(pprint.pformat(('Address with pure diamond: ' + str(card['user']) + ' Card: ' + str(card['proto'])))) # TODO: Create a function that takes card proto and returns its name.
            
            if card['proto'] == 380:
                firstPhoenix += 1
                print(card['purity'])

        outputList.append(pprint.pformat('Total Cards: ' + str(len(userInfo))))
        outputList.append(pprint.pformat('Total Commons: ' + str(totalCommons)))
        outputList.append(pprint.pformat('Total Rares: ' + str(totalRares)))
        outputList.append(pprint.pformat('Total Epics: ' + str(totalEpics)))
        outputList.append(pprint.pformat('Total Legendaries: ' + str(totalLegendaries)))
        outputList.append(pprint.pformat('Total Plain: ' + str(totalPlain)))
        outputList.append(pprint.pformat('Total Shadow: ' + str(totalShadow)))
        outputList.append(pprint.pformat('Total Gold: ' + str(totalGold)))
        outputList.append(pprint.pformat('Total Diamond: ' + str(totalDiamond)))
        outputList.append(pprint.pformat('Total Perfect Plain: ' + str(totalPerfectPlain)))
        outputList.append(pprint.pformat('Total Perfect Shadow: ' + str(totalPerfectShadow)))
        outputList.append(pprint.pformat('Total Perfect Gold: ' + str(totalPerfectGold)))
        outputList.append(pprint.pformat('Total Perfect Diamond: ' + str(totalPerfectDiamond)))
        outputList.append(pprint.pformat('Total Zero Purity: ' + str(totalZeroPurity)))

        open("allCardsCount.txt", "a").write(pprint.pformat(outputList))
        cycles += 1
        print('Fetched updated stats ' + str(cycles) + ' times.')
        time.sleep(3600)


print('Fetching...')
with urllib.request.urlopen(apiUrl) as url:
   userInfo = json.load(url)
with urllib.request.urlopen("https://pastebin.com/raw/e5rv9mep") as url:
   cardInfo = json.load(url)
print('Done.')

n = 0
rarePacks = 0
epicPacks = 0
legendPacks = 0
shinyPacks = 0
totalPacks = 0
for pack in userInfo:
    if userInfo[n]['factory'] in ('0x0777F76D195795268388789343068e4fCd286919', 
                                '0x08dBf4f942ba8cd7871C13addEfdfFEf3E5a8035',
                                '0xCA6746f65D53D2dF5022b5d775817e62e8462690', 
                                '0x015531A044BAe03bF4dAB1ceabfc232a969b7175'):
        rarePacks += 1
    elif userInfo[n]['factory'] in ('0x482Cf6A9d6b23452C81d4D0f0f139C1414963f89',
                                    '0x84487E50dB6317E5e834d89d0e81Fd873462Ea47',
                                    '0xe5dC9d1B58fD5a95fC20A6c6AfAA76d44D70A7DF',
                                    '0x6e0051C750b81f583f42f93A48d56497779992d8'):
        epicPacks += 1
    elif userInfo[n]['factory'] in ('0xc47D7d42E44b2e04c83a45cF45898E597A0c2311',
                                    '0x80b3075410Ee52C520DD203f60206F633D27A109',
                                    '0x6c5DC1dcdA3d309a6e919e6D0965f197E0Fc1913',
                                    '0x5789e2B5460caE9329d93A78511E2aC49f98a1f6'):
        legendPacks += 1
    elif userInfo[n]['factory'] in ('0x1e891C587b345ab02A31b57c1F926fB08913d10D',
                                    '0x314495517F380CEb7c498A35739E40864240ADCf',
                                    '0x80391307F1B08Cc068Fa1D1b77513B98C36DFbfa',
                                    '0x000983ba1A675327F0940b56c2d49CD9c042DFBF'):
        shinyPacks += 1

    totalPacks += 1
    n += 1
print('Total packs: ' + str(totalPacks) + ' Total rare packs: ' + str(rarePacks) + ' Total epic packs: ' + str(epicPacks) + ' Total legendary packs: ' + str(legendPacks) + ' Total shiny packs: ' + str(shinyPacks))

while True:

    print('To search by rarity, press 1')
    print('To search by purity, press 2')
    print('For packs and their contents, press 3')

    searchType = input('Search type: ')

    if searchType == '1':

        print('1: Common')
        print('2: Rare')
        print('3: Epic')
        print('4: Legendary')

        queryRarity = input('Enter number for rarity: ')

        if queryRarity == '1':
            raritySearchValue = 'Common'
        if queryRarity == '2':
            raritySearchValue = 'Rare'
        if queryRarity == '3':
            raritySearchValue = 'Epic'
        if queryRarity == '4':
            raritySearchValue = 'Legendary'

        parsedCardInfo = defaultdict(list)
        i = 0
        n = 0
        for pack in userInfo:
            for card in pack['cards']:
                parsedCardInfo[card['proto']].append(card['purity'])
                i += 1
            i = 0
            n += 1

        duplicateCards = 0
        rarityResultsList = []
        for card in cardInfo:
            for proto in parsedCardInfo:
                if cardInfo[card]['GLOBALID'] == proto:
                    if cardInfo[card]['rarity'] == 'Oi.' + raritySearchValue:
                        rarityResultsList.append(str(len(parsedCardInfo[proto])) + ' - ' + cardInfo[card]['name'] + ' - ' + str(parsedCardInfo[proto]))
                        duplicateCards = duplicateCards + len(parsedCardInfo[proto])

        pprint.pprint(rarityResultsList)
        print('Total Unique ' + raritySearchValue + ' Cards: ' + str(len(rarityResultsList)))
        print('Total ' + raritySearchValue + ' Cards: ' + str(duplicateCards))

    if searchType == '2':

        print('1: Plain')
        print('2: Shadow')
        print('3: Gold')
        print('4: Diamond')

        queryPurity = input('Enter number for purity: ')

        if queryPurity == '1':
            purityLow = 0
            purityHigh = 999
        if queryPurity == '2':
            purityLow = 1000
            purityHigh = 1999
        if queryPurity == '3':
            purityLow = 2000
            purityHigh = 2999
        if queryPurity == '4':
            purityLow = 3000
            purityHigh = 3999

        parsedCardInfo = defaultdict(list)
        i = 0
        n = 0
        for pack in userInfo:
            for card in userInfo[n]['cards']:
                if purityLow <= int(userInfo[n]['cards'][i]['purity']) <= purityHigh:
                    parsedCardInfo[userInfo[n]['cards'][i]['proto']] = userInfo[n]['cards'][i]['purity']
                i += 1
            i = 0
            n += 1

        commonCount = 0
        rareCount = 0
        epicCount = 0
        legendaryCount = 0
        purityResultsList = []
        for card in cardInfo:
            for proto in parsedCardInfo:
                if cardInfo[card]['GLOBALID'] == proto:
                    if cardInfo[card]['rarity'] == 'Oi.Common':
                        trimmedRarity = 'Common'
                        commonCount += 1
                    if cardInfo[card]['rarity'] == 'Oi.Rare':
                        trimmedRarity = 'Rare'
                        rareCount += 1
                    if cardInfo[card]['rarity'] == 'Oi.Epic':
                        trimmedRarity = 'Epic'
                        epicCount += 1
                    if cardInfo[card]['rarity'] == 'Oi.Legendary':
                        trimmedRarity = 'Legendary'
                        legendaryCount += 1
                    purityResultsList.append(cardInfo[card]['name'] + ' - ' + str(parsedCardInfo[proto]) + ' - ' + trimmedRarity)
                    i += 1
        pprint.pprint(purityResultsList)
        print('Total Cards: ' + str(len(purityResultsList)))
        print('Total Commons: ' + str(commonCount))
        print('Total Rares: ' + str(rareCount))
        print('Total Epics: ' + str(epicCount))
        print('Total Legendaries: ' + str(legendaryCount))

    # if searchType == '3':
    print('To search by rarity, press 1')
    print('To search by purity, press 2')
    print('To list all of your packs and their contents, press 3')

    searchType = input('Search type: ')

    if searchType == '1':

        print('1: Common')
        print('2: Rare')
        print('3: Epic')
        print('4: Legendary')

        queryRarity = input('Enter number for rarity: ')

        if queryRarity == '1':
            raritySearchValue = 'Common'
        if queryRarity == '2':
            raritySearchValue = 'Rare'
        if queryRarity == '3':
            raritySearchValue = 'Epic'
        if queryRarity == '4':
            raritySearchValue = 'Legendary'

        parsedCardInfo = defaultdict(list)
        i = 0
        n = 0
        for pack in userInfo:
            for card in userInfo[n]['cards']:
                parsedCardInfo[userInfo[n]['cards'][i]['proto']].append(userInfo[n]['cards'][i]['purity'])
                i += 1
            i = 0
            n += 1

        rarityResultsList = []
        for card in cardInfo:
            for proto in parsedCardInfo:
                if cardInfo[card]['GLOBALID'] == proto:
                    if cardInfo[card]['rarity'] == 'Oi.' + raritySearchValue:
                        rarityResultsList.append(cardInfo[card]['name'] + ' - ' + str(parsedCardInfo[proto]))

        pprint.pprint(rarityResultsList)
        print('Total Unique Cards: ' + str(len(rarityResultsList)))

    if searchType == '2':

        print('1: Plain')
        print('2: Shadow')
        print('3: Gold')
        print('4: Diamond')

        queryPurity = input('Enter number for purity: ')

        if queryPurity == '1':
            purityLow = 0
            purityHigh = 999
        if queryPurity == '2':
            purityLow = 1000
            purityHigh = 1999
        if queryPurity == '3':
            purityLow = 2000
            purityHigh = 2999
        if queryPurity == '4':
            purityLow = 3000
            purityHigh = 3999
        
        print(purityHigh)
        print(purityLow)

        parsedCardInfo = defaultdict(list)
        i = 0
        n = 0
        for pack in userInfo:
            for card in userInfo[n]['cards']:
                if purityLow <= int(userInfo[n]['cards'][i]['purity']) <= purityHigh:
                    parsedCardInfo[userInfo[n]['cards'][i]['proto']] = userInfo[n]['cards'][i]['purity']
                i += 1
            i = 0
            n += 1

        purityResultsList = []
        for card in cardInfo:
            for proto in parsedCardInfo:
                if cardInfo[card]['GLOBALID'] == proto:
                    if cardInfo[card]['rarity'] == 'Oi.Common':
                        trimmedRarity = 'Common'
                    if cardInfo[card]['rarity'] == 'Oi.Rare':
                        trimmedRarity = 'Rare'
                    if cardInfo[card]['rarity'] == 'Oi.Epic':
                        trimmedRarity = 'Epic'
                    if cardInfo[card]['rarity'] == 'Oi.Legendary':
                        trimmedRarity = 'Legendary'
                    purityResultsList.append(cardInfo[card]['name'] + ' - ' + str(parsedCardInfo[proto]) + ' - ' + trimmedRarity)
                    i += 1
        pprint.pprint(purityResultsList)
        print('Total Cards: ' + str(len(purityResultsList)))

    # if searchType == '3':
