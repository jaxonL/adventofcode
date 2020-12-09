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

def changeInstructionAndGetFinalAcc(ops):
    # maybe go forward til last instruction before visited, and keep a stack of previous instructions
    # if looped, pop previous instruction
    #   if prev instr = nop/jmp, switch, and check if continuing does anything
    #       save index that was changed
    acc = 0
    visited = [0] * len(ops)
    viewingQueue = []
    i = 0
    changedIndex = None
    originalOpVal = None
    while i < len(ops):
        # print('executing', i, ops[i], end=': ')
        if visited[i] is 1:
            # start bactracking
            # has seen -- shouldn't error else something extremely wrong
            prevIndex = viewingQueue.pop()
            # do some things
            prevOp, prevVal = ops[prevIndex]
            # print(prevOp, prevVal)
            while prevOp == 'acc' or (prevOp == 'nop' and prevVal == 0) or (prevIndex == changedIndex):
                # print('\n\tremoving instruction', prevIndex, ' - ', prevOp, prevVal, end=';')
                if prevIndex == changedIndex:
                    # change it back
                    ops[changedIndex] = originalOpVal
                    changedIndex = None
                    originalOpVal = None
                else:
                    # remove acc addition
                    acc -= prevVal
                # print(' new acc', acc)
                visited[prevIndex] = 0
                prevIndex = viewingQueue.pop()
                prevOp, prevVal = ops[prevIndex]

            if prevOp == 'nop':
                # change to jmp
                changedIndex = prevIndex
                originalOpVal = ops[changedIndex]
                ops[changedIndex] = ('jmp', prevVal)
                i, acc = JMP(prevIndex, acc, prevVal)
                # print('\n\tchanged', prevIndex, 'to jmp from', prevOp, prevVal, 'acc is', acc)
            else:
                # is a jmp, change to nop
                changedIndex = prevIndex
                originalOpVal = ops[changedIndex]
                ops[changedIndex] = ('nop', prevVal)
                i, acc = NOP(prevIndex, acc, prevVal)
                # print('\n\tchanged', prevIndex, 'to nop from', prevOp, prevVal, 'acc is', acc)

            viewingQueue.append(prevIndex)
        else:
            # have not seen before, continue
            op, val = ops[i]
            visited[i] = 1
            viewingQueue.append(i)
            i, acc = OP_DICT.get(op)(i, acc, val)
            # print('acc is', acc)
        # print('\t viewingQueue:', viewingQueue)

    # print('changed instr at index', changedIndex, ops[changedIndex])
    return acc

def dayEight():
    # instructions = readList('d8-sample.in', getOpValPair)
    instructions = readList('d8.in', getOpValPair)
    # for x in instructions[:5]:
    #     print(x)
    # print('part one:', getAccValueBeforeLoop(instructions))
    print('part two:', changeInstructionAndGetFinalAcc(instructions))

dayEight()
