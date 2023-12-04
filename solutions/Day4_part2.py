file = open('../input/Day4_input.txt', 'r')

card = 0
sum = 0 

cardDict = {}

for number in range(1, 203):
    cardDict[number] = 1

while True:
    headline = file.readline()
    if not headline:
        break

    card += 1 

    headline = headline.strip()
    headline = headline.split(":")[1]
    winningNumbers = headline.split("|")[0]
    winningNumbers = winningNumbers.split(" ")
    cardNumbers = headline.split("|")[1]
    cardNumbers = cardNumbers.split(" ")
    
    winningNumbersInCard = 0
    for item in cardNumbers: 
        if item == "":
            pass
        elif item in winningNumbers:
            winningNumbersInCard += 1
    
    for number in range(1, winningNumbersInCard+1): 
        cardUpdateNum = card + number 
        updatedNumber = cardDict.get(cardUpdateNum) + (1 * cardDict.get(card))
        print(cardUpdateNum)
        print(cardDict.get(cardUpdateNum))
        print(updatedNumber)
        cardDict.update({cardUpdateNum: updatedNumber})

for number in range(1, 203):
    sum += cardDict.get(number)

print(cardDict)   
print(sum)




