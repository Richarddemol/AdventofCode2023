file = open('../input/Day3_input.txt', 'r')

grid = []
horizontal = []

while True:
    headline = file.readline()
    if not headline:
        break
    
    horizontal = []

    for c in headline: 
        horizontal.append(c)
    
    grid.append(horizontal)

x = 0
y = 0
#numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ["%", "*", "=", "!", "@", "#", "$", "^", "&", ")", "(", "-", "_", "+", ",","/","`","~","\\","[","]","{","}"]
sum = 0

while y <= 140:
    num = ""
    h = y-1 
    if x == 0:
        v = x
    else:
        v = x-1
    if x == 139:
        mv = 139
    else:
        mv = x+1
    if grid[x][y].isdigit() and not grid[x][y+1].isdigit():
        mh = y+2
        while h != mh and h <= 140: 
            if grid[v][h] in symbols:
                sum += int(grid[x][y])
                print(grid[x][y])
                grid[x][y] = "0"
                break
            elif h <= 140:
                h += 1
            if h == mh and v == mv:
                break
            if h == mh: 
                v = v+1 
                h = y-1
        y += 1
    elif grid[x][y].isdigit() and grid[x][y+1].isdigit() and not grid[x][y+2].isdigit():
        mh = y+3
        while h != mh and h <= 140: 
            if grid[v][h] in symbols:
                num = grid[x][y] + grid[x][y+1]
                print(num)
                sum += int(num)
                grid[x][y] = "0"
                grid[x][y+1] = "0"
                break
            elif h <= 140:
                h += 1
            if h == mh and v == mv:
                break
            if h == mh: 
                v = v+1 
                h = y-1
        y += 2
    elif grid[x][y].isdigit() and grid[x][y+1].isdigit() and grid[x][y+2].isdigit() and not grid[x][y+3].isdigit():
#        print(str(grid[x][y]) + str(grid[x][y+1]) + str(grid[x][y+2]))
        mh = y+4
        while h != mh and h <= 140: 
           # print("v " + str(v) + " h " + str(h))
            if grid[v][h] in symbols:
                num = grid[x][y] + grid[x][y+1] + grid[x][y+2]
                print(num)
                sum += int(num)
                grid[x][y] = "0"
                grid[x][y+1] = "0"
                grid[x][y+2] = "0"
                break
            elif h <= 140:
                h += 1
            if h == mh and v == mv:
                break
            if h == mh: 
                v = v+1 
                h = y-1
        y += 3


    
    y += 1
    if y == 141: 
        x += 1
        y = 0
    if x == 139 and y == 140:
        break

#l = 0 
#while l != 140: 
#    print(grid[l])
#    l += 1

print(sum)
#print(grid[1][0])