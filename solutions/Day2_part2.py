file = open('../input/Day2_input.txt', 'r')
gameNumber = 0
sumPower = 0

while True:
    headline = file.readline()
    if not headline:
        break
    
    gameNumber += 1 
    headline = headline.replace(" ", "")
    headline = headline.split(":")[1]
    headline = headline.split(";")
    amountRed = 0
    amountBlue = 0
    amountGreen = 0

    for game in headline: 
        dices = game.split(',')
        for dice in dices:
            num=""
            for c in dice:
                if c.isdigit():
                    num = num + c
            if "red" in dice:
                if int(num) > amountRed:
                    amountRed = int(num)
            if "blue" in dice:
                if int(num) > amountBlue:
                    amountBlue = int(num)
            if "green" in dice:
                if int(num) > amountGreen:
                    amountGreen = int(num)

    if amountRed == 0:
        amountRed = 1
    if amountBlue == 0: 
        amountBlue = 1
    if amountGreen == 0:
        amountGreen = 1

    sumPower += amountRed * amountBlue * amountGreen

print(sumPower)

        
            



