file = open('../input/Day4_input.txt', 'r')

card = 0
sum = 0

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
    
    if winningNumbersInCard == 0: 
        y = 0
    else:
        y = 2**(winningNumbersInCard - 1)


    sum += y
    

print(sum)


