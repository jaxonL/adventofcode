from collections import deque

def parseAsQueue(filename):
    inputFile = open(filename, 'r')

    queue = deque(inputFile.read().strip().split())
    inputFile.close()

    return queue

def calcNodeSum(cStack, mdStack, inQueue):
    cCount = cStack.pop()
    sum = 0

    while cCount == 0:
        mdCount = mdStack.pop()
        while mdCount:
            toAdd = int(inQueue.popleft())
            sum += toAdd
            # print('added', mdCount, 'e num', toAdd, sum)
            mdCount -= 1
        cCount = cStack.pop() if len(cStack) else -1
        cCount -= 1
    if cCount:
        cStack.append(cCount)
    return sum

def main():
    inputQueue = parseAsQueue('d8.in')
    childrenStack = deque()
    metadataStack = deque()
    allSum = 0

    while(len(inputQueue)):
        childrenCount = int(inputQueue.popleft())
        metadataCount = int(inputQueue.popleft())

        # print(childrenCount, metadataCount)

        childrenStack.append(childrenCount)
        metadataStack.append(metadataCount)

        if childrenCount:
            # print('continuing')
            continue

        # else do the function
        allSum += calcNodeSum(childrenStack, metadataStack, inputQueue)

    print(allSum)






main()
