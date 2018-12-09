from collections import deque

class Node:
    def __init__(self, totalChildren, metadataCount):
        self.mdCount = metadataCount
        self.cCount = totalChildren
        self.children = []
        self.value = 0

    def __str__(self):
        return 'Node with value ' + str(self.value) + ' and ' + str(self.cCount) + ' children'

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

def createChildNodes(cStack, mdStack, inQueue):
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

def buildTree(inQueue):
    treeNode = Node(int(inQueue.popleft()), int(inQueue.popleft()))

    if treeNode.cCount == 0:
        for x in range(treeNode.mdCount):
            treeNode.value += int(inQueue.popleft())

        # print('leaf node has value', treeNode.value)
        return treeNode

    # print('non leaf node -', treeNode.cCount, 'children')
    for x in range(treeNode.cCount):
        treeNode.children.append(buildTree(inQueue))

    for x in range(treeNode.mdCount):
        indexToAdd = int(inQueue.popleft()) - 1
        # print(indexToAdd, treeNode.cCount, len(treeNode.children))
        if indexToAdd < treeNode.cCount:
            treeNode.value += treeNode.children[indexToAdd].value

    # print('non leaf node value', treeNode.value)

    return treeNode

def main():
    inputQueue = parseAsQueue('d8.in')
    childrenStack = deque()
    metadataStack = deque()
    allSum = 0

    # while(len(inputQueue)):
    #     childrenCount = int(inputQueue.popleft())
    #     metadataCount = int(inputQueue.popleft())
    #     currNode = Node(metadataCount)
    #
    #     # print(childrenCount, metadataCount)
    #
    #     childrenStack.append(childrenCount)
    #     metadataStack.append(metadataCount)
    #
    #     if childrenCount:
    #         # print('continuing')
    #         continue
    #
    #     # else do the function
    #     allSum += calcNodeSum(childrenStack, metadataStack, inputQueue)
    # print(allSum)

    navigTree = buildTree(inputQueue)

    print(navigTree)







main()
