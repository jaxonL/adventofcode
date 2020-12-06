instructions = ''
instructionsList = {}

# refactor to array of objects { letter: string[]}

def parseLine(line):
    global instructions
    prereq = line.split(' ')[1]
    step = line.split(' ')[7]

    preqInd = instructions.find(prereq)
    stepInd = instructions.find(step)

    # print(prereq, preqInd, '->', step, stepInd)
    if prereq in instructionsList.keys():
        instructionsList[prereq].append(step)
    else:
        instructionsList[prereq] = [step]

    if preqInd == -1 and stepInd == -1:
        instructions = prereq + instructions

        insertStep(0, step, stepInd)
    elif stepInd == -1: # preq exists; no step
        insertStep(preqInd, step, stepInd)
    elif preqInd == -1: # step exists, no preq
        insertPreq(stepInd, prereq, preqInd)
    elif stepInd < preqInd:
            insertPreq(stepInd, prereq, preqInd)
    # print(instructions)
    # print(instructionsList)





def insertStep(preqInd, stepChar, stepInd):
    global instructions
    # print('ins step')
    if stepInd > -1:
        # remove it
        instructions = instructions[:stepInd] + instructions[stepInd + 1:]
    totalLen = len(instructions)

    for x in range(preqInd + 1, totalLen):
        currChar = instructions[x]
        # print(x)
        if currChar in instructionsList.keys() and stepChar in instructionsList[currChar]:
            continue
        if ord(currChar) > ord(stepChar):
            # print('not in list', instructions, x, x-1)
            instructions = instructions[:x] + stepChar + instructions[x:]
            break
    if instructions.find(stepChar) == -1:
        instructions += stepChar

def insertPreq(stepInd, preqChar, preqInd):
    global instructions
    # print('ins preq')
    if preqInd > -1:
        # remove it
        instructions = instructions[:preqInd] + instructions[preqInd + 1:]
    totalLen = len(instructions)
    for x in range(stepInd):
        # print(x)
        ind = stepInd - 1 - x
        currChar = instructions[x]
        if (currChar in instructionsList.keys() and preqChar in instructionsList[currChar]) or ord(currChar) < ord(preqChar):
            instructions = instructions[:ind + 1] + preqChar + instructions[ind + 1:]
            break
    if instructions.find(preqChar) == -1:
        instructions = preqChar + instructions

def main():
    inputFile = open('d7-reordered.in', 'r')
    for line in inputFile:
        line = line.strip()
        if line:
            parseLine(line)

    print(instructions)

main()
