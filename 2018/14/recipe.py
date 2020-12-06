
def calcTen(targetLen):
    list = [3, 7]
    indA = 0
    indB = 1
    counter = 1
    while len(list) < targetLen + 10:
        # print(counter, ':', indA, '-', list[indA], indB, '-', list[indB])
        # counter += 1
        addToList = list[indA] + list[indB]
        # cast to string
        addToList = str(addToList)
        list.extend([int(x) for x in addToList])
        indA = (list[indA] + 1 + indA) % len(list)
        indB = (list[indB] + 1 + indB) % len(list)
        # print(list)

    return list[targetLen:targetLen + 10]

def calcNumBefore(targetString):
    list = [3, 7]
    indA = 0
    indB = 1
    found = False
    targetStringMaxInd = len(targetString) - 1
    targetArray = [int(x) for x in targetString]
    while not found:
        addToList = list[indA] + list[indB]
        # cast to string to get individual chars
        addToList = [int(x) for x in str(addToList)]
        checkTwice = True if len(addToList) > 1 else False
        list.extend(addToList)
        indA = (list[indA] + 1 + indA) % len(list)
        indB = (list[indB] + 1 + indB) % len(list)
        currListMaxInd = len(list) - 1

        # assume found
        # found = True
        # for i in range(targetStringMaxInd + 1): # requires also checking second to last index
        #     if list[currListMaxInd - i] != int(targetString[targetStringMaxInd - i]):
        #         found = False
        #         break
        #     if i == 3: print('matched 4 at', len(list) - targetStringMaxInd - 10)
        #     # elif i == 2: print('matched 3 at', len(list) - targetStringMaxInd - 10)
        #     # print('checking')

        if list[-len(targetString):] == targetArray:
            found = True # similar line from one of the solutions on the solutions thread
        if checkTwice and not found and list[-len(targetString) -1:-1] == targetArray:
            found = True # also check second to last index
        # print(list)
    # print(len(list), (targetStringMaxInd + 1))
    print(list[len(list) - targetStringMaxInd - 10:]);
    return len(list) - targetStringMaxInd - 1

def main():
    target = 236021
    # target = 9
    # target = 5
    # target = 18
    # target = 2018
    # lastTen = calcTen(target)
    # print(''.join([str(x) for x in lastTen]))
    # targetString = '1010'
    # targetString = '021'
    # targetString = '23602'
    targetString = '236021'
    # targetString = '51589'
    # targetString = '01245'
    # targetString = '92510'
    # targetString = '59414'
    previousCount = calcNumBefore(targetString)
    print(previousCount)

main()
