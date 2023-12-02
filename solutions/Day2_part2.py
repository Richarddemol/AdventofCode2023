file = open('../input/Day2_input.txt', 'r')
gameNumber = 0
sumGameNumber = 0

while True:
    headline = file.readline()
    if not headline:
        break
    
    gameNumber += 1 
    headline = headline.replace(" ", "")
    headline = headline.split(":")[1]
    headline = headline.split(";")
    fail = 0
    for game in headline: 
        dices = game.split(',')
        for dice in dices:
            num=""
            for c in dice:
                if c.isdigit():
                    num = num + c
            if "red" in dice:
                if int(num) >= 13:
                    fail = 1
            if "blue" in dice:
                if int(num) >= 15:
                    fail = 1
            if "green" in dice:
                if int(num) >= 14:
                    fail = 1
    if fail == 0: 
        sumGameNumber += gameNumber

print(sumGameNumber)

        
            



