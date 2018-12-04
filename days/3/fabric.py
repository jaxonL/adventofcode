inputFile = open('d3p1.in', 'r')
squareLength = 0
def returnCoordinatePair(claimDetails):
    global squareLength
    claimDetails = claimDetails.strip()
    if claimDetails:
        claimId, at, ulc, dimensions = claimDetails.split(' ') # ulc = upper left corner
        # print(claimId + '_(claim)|' + ulc + '_(ulc)|' + dimensions + '_(dimensions)')
        # cannot do lazy parsing!
        # ulcx = int(ulc[0])
        # ulcy = int(ulc[2])
        ulcx, ulcy = ulc.split(',')
        ulcx = int(ulcx)
        ulcy = int(ulcy[:(len(ulcy) - 1)])

        # dimx = int(dimensions[0])
        # dimy = int(dimensions[2])
        dimx, dimy = dimensions.split('x')
        dimx = int(dimx)
        dimy = int(dimy)

        # brc = bottom right corner
        brcx = ulcx + dimx - 1
        brcy = ulcy + dimy - 1
        squareLength = max(ulcx, ulcy, brcx, brcy, squareLength)
        return [ulcx, ulcy, brcx, brcy]

allLines = [returnCoordinatePair(line) for line in inputFile if line.strip()]

# for pairs in allLines: print(pairs)

# print(max(allLines, key=findMaxCoordinate))
print('fabric side length:', squareLength, '\n')

# squareLength = max(max(max(allLines, key=findMaxCoordinate))) # ew but trying to bruteforce ¯\_(ツ)_/¯

# list references !!! would not work since the exact copy of oneColumn is repeated,
# so changing one value changes all values
# oneColumn = [ 0 for x in range(squareLength + 1)]
# squareFabric = [oneColumn for x in range(squareLength + 1)] # initialise 2d array

squareFabric = [[ 0 for x in range(squareLength + 1)] for x in range(squareLength + 1)] # initialise 2d array

# for row in squareFabric: print(row)

overlappedSquare = 0
# for row in squareFabric: print(row)

for coordinatePair in allLines:
    # print('doing tuple', coordinatePair)
    lx, ty, rx, by = coordinatePair

    # print('range x: ', lx, rx)
    # print('range y: ', ty, by)

    for x in range(lx, rx + 1):
        for y in range(ty, by + 1):
            # print('x:', x, 'y:', y)
            if squareFabric[y][x] == 1:
                squareFabric[y][x] = 2
                overlappedSquare += 1
            elif squareFabric[y][x] == 0:
                squareFabric[y][x] = 1


# for row in squareFabric: print(row)

print(overlappedSquare)
inputFile.close()
