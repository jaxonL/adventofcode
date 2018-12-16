
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
    while not found:
        addToList = list[indA] + list[indB]
        # cast to string
        addToList = str(addToList)
        list.extend([int(x) for x in addToList])
        indA = (list[indA] + 1 + indA) % len(list)
        indB = (list[indB] + 1 + indB) % len(list)
        currListMaxInd = len(list) - 1
        # assume found
        found = True
        for i in range(targetStringMaxInd + 1):
            if list[currListMaxInd - i] != int(targetString[targetStringMaxInd - i]):
                found = False
                break
            print('checking')

        # if list[-len(targetString):] == [int(x) for x in targetString]: found = True # similar line from one of the solutions on the solutions thread
        # print(list)
    # print(len(list), (targetStringMaxInd + 1))
    return len(list) - targetStringMaxInd - 1

def main():
    target = 236021
    # target = 9
    # target = 5
    # target = 18
    # target = 2018
    # lastTen = calcTen(target)
    # print(''.join([str(x) for x in lastTen]))
    targetString = '236021'
    # targetString = '51589'
    # targetString = '01245'
    # targetString = '92510'
    # targetString = '59414'
    previousCount = calcNumBefore(targetString)
    print(previousCount)

main()
