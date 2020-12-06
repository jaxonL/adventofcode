# day 1 challenge (done on dec 6)

def readList(filepath, castFn=str):
    # assumes filepath is a simple file with values per line
    # and reads it into a list. casts the elements according
    # to castFn
    inputFile = open(filepath, 'r')
    inputList = [castFn(line.strip()) for line in inputFile if line.strip()]
    return inputList

# returns a pair
def getSum(targetSum=2020):
    inputList = readList('d1.in', int)
    # sort list asc in place
    inputList.sort()
    startInd = 0
    endInd = len(inputList) - 1
    while startInd < endInd:
        # compare
        startDiff = targetSum - inputList[startInd]
        if inputList[endInd] == startDiff:
            # found it!
            print('found sum numbers:', inputList[startInd], inputList[endInd])
            return (inputList[startInd], inputList[endInd])
        
        if inputList[endInd] > startDiff:
            # number at the end too big for sum, go down
            endInd -= 1
        else:
            # cannot find such a sum, increment start
            startInd += 1
    return (None, None)


def getSumWithThree(targetSum=2020):
    inputList = readList('d1.in', int)
    # sort list asc in place
    inputList.sort()
    startInd = 0
    endInd = len(inputList) - 1
    while startInd < endInd:
        # compare
        startDiff = targetSum - inputList[startInd]
        third = targetSum - inputList[startInd] - inputList[endInd]
        if third <= inputList[startInd]:
            # num at end index may be too large; decrement that
            endInd -= 1
        else:
            # try to find the third number
            midInd = startInd + 1
            while midInd < endInd:
                if inputList[midInd] == third:
                    # found it!
                    print('found sum numbers:', inputList[startInd], inputList[midInd], inputList[endInd])
                    return (inputList[startInd], inputList[midInd], inputList[endInd])
                if inputList[midInd] < third:
                    midInd += 1
                else:
                    # inputList[midInd] > third
                    break
            # if we didnt find it, increment the start index
            startInd += 1
    return (None, None, None)

def dayOne():
    first, second = getSum()
    if first is not None and second is not None:
        print('part one answer:', first * second)
    else:
        print('error somewhere... right?')

    one, two, three = getSumWithThree()
    if one is None or two is None or three is None:
        print('maybe wrong algorithm...')
    else:
        print('part two answer:', one * two * three)

dayOne()
