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

        claimId = claimId[1:]

        # brc = bottom right corner
        brcx = ulcx + dimx - 1
        brcy = ulcy + dimy - 1
        squareLength = max(ulcx, ulcy, brcx, brcy, squareLength)
        return [ulcx, ulcy, brcx, brcy, claimId]

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
overlappingCoordinates = []
# for row in squareFabric: print(row)

for coordinatePair in allLines:
    # print('doing tuple', coordinatePair)
    lx, ty, rx, by, claimId = coordinatePair

    # print('range x: ', lx, rx)
    # print('range y: ', ty, by)

    for x in range(lx, rx + 1):
        for y in range(ty, by + 1):
            # print('x:', x, 'y:', y)
            if squareFabric[x][y] == 1:
                squareFabric[x][y] = 2
                overlappedSquare += 1
                overlappingCoordinates.append((x, y))
            elif squareFabric[x][y] == 0:
                squareFabric[x][y] = 1


# for row in squareFabric: print(row)

print(overlappedSquare)
print(len(overlappingCoordinates)) # sanity check
overlappingCoordinates.sort()
# print(overlappingCoordinates)

### part 2 ###

goodClaim = ''
possiblyGood = []
squareFabric = [[ [] for x in range(squareLength + 1)] for x in range(squareLength + 1)] # initialise 2d array

for coordinatePair in allLines:
    lx, ty, rx, by, claimId = coordinatePair
    if not goodClaim:
        goodClaim = claimId
        print('setting gc to', claimId)
    # print(possiblyGood)
    overlapped = False
    for overlap in overlappingCoordinates:
        ox, oy = overlap

        # i gave up
        if lx <= ox and rx >= ox:
            if ty <= oy and by >= oy:
                overlapped = True
                break

        # # narrow down points
        # if ox < lx:
        #     # print('x is less', ox, lx, oy);
        #     continue
        # if ox > rx:
        #     # print('x is more', ox, rx, oy)
        #     overlapped = False
        #     break
        #
        # if oy < ty:
        #     # print('y is less', oy, ty, ox);
        #     continue
        # if oy > by:
        #     # print('y is more', oy, by, ox )
        #     overlapped = False
        #     break
        #
        # # lx <= ox <= rx; ty <= oy <= by
        # # if overlapping, remove from possiblyGood
        # # print('removing', claimId)
        # overlapped = True
        # break
    if not overlapped:
        possiblyGood.append(claimId)


    # for x in range(lx, rx + 1):
    #     for y in range(ty, by + 1):
    #         # print('x:', x, 'y:', y)
    #         if len(squareFabric[x][y]): # has collided
    #             squareFabric[x][y].append(claimId)
    #             if goodClaim and goodClaim in squareFabric[x][y]:
    #                 print('gc was', goodClaim, '; resetting it (bc collided with', claimId, ')')
    #                 goodClaim = '' # reset if part of the collisions
    #         elif len(squareFabric[x][y]) == 0:
    #             squareFabric[x][y].append(claimId)

# print('goodClaim:', goodClaim)
print('pg:', possiblyGood)
inputFile.close()
