# day 8 challenge

def NOP(currIndex, acc, val):
    return (currIndex + 1, acc)

def ACC(currIndex, acc, val):
    return (currIndex + 1, acc + val)

def JMP(currIndex, acc, val):
    return (currIndex + val, acc)

OP_DICT = {
    'nop': NOP,
    'jmp': JMP,
    'acc': ACC
}

def getOpValPair(lineString):
    op, val = lineString.split(' ') # expecting stuff to be "<op> <value>"
    return (op.lower(), int(val))

# copy-pasta'd . should refactor into utilities class
def readList(filepath, castFn=str):
    # assumes filepath is a simple file with values per line
    # and reads it into a list. casts the elements according
    # to castFn
    inputFile = open(filepath, 'r')
    inputList = [castFn(line.strip()) for line in inputFile if line.strip()]
    return inputList

def getAccValueBeforeLoop(ops):
    acc = 0
    visited = [0] * len(ops)
    # print(visited)
    i = 0
    while visited[i] is 0:
        op, val = ops[i]
        visited[i] = 1
        operation = OP_DICT.get(op)
        if operation is None:
            print('this shouldnt happen; op is none -', op)
        else:
            i, acc = operation(i, acc, val)

    return acc

def dayEight():
    # instructions = readList('d8-sample.in', getOpValPair)
    instructions = readList('d8.in', getOpValPair)
    # for x in instructions[:5]:
    #     print(x)
    print(getAccValueBeforeLoop(instructions))

dayEight()
