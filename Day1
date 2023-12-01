file = open('day1', 'r')

while True:
    headline = file.readline()
    if not headline:
        break
    
    headline = headline.replace("one", "o1ne")
    headline = headline.replace("two", "tw2o")
    headline = headline.replace("three", "th3ree")
    headline = headline.replace("four", "fo4ur")
    headline = headline.replace("five", "fi5ve")
    headline = headline.replace("six", "s6ix")
    headline = headline.replace("seven", "se7ven")
    headline = headline.replace("eight", "ei8ght")
    headline = headline.replace("nine", "ni9ne")

    num = "" 
    for c in headline:
        if c.isdigit():
            num = num + c            
    if len(num) > 1: 
        num = num[0] + num[-1]
    if len(num) == 1: 
        num = num[0] + num[0]
    print(num)
