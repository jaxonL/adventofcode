
A_ORD = ord('A')

def parseInput(filename):
    inputFile = open(filename, 'r')
    metadata = [None for x in range(26)]

    for line in inputFile:
        if line.strip():
            prereq = line.split(' ')[1]
            step = line.split(' ')[7]

            # print(prereq, '->', step)
            # print(ord(prereq) - ord('A'), '->', ord(step) - ord('A'))
            prereqOrd = ord(prereq) - A_ORD
            stepOrd = ord(step) - A_ORD
            # initialise values
            if metadata[prereqOrd] is None:
                metadata[prereqOrd] = ''
            if metadata[stepOrd] is None:
                metadata[stepOrd] = str(prereq)
            else:
                metadata[stepOrd] += str(prereq)
    inputFile.close()
    return metadata

def findZeroValues(md):
    values = []
    for key in md.keys():
        if len(md[key]) == 0:
            values.append(key)
    soleValue = values[0]
    if len(values) > 1:
        # find the one that has the largest 'isAfter' char
        soleValue = max(values, key=lambda x: md[x]['largestBefore'])
    # completeVal= []
    # for key in values:
    #     popped = md.pop(key)
    #     popped['letter'] = key
    #     completeVal.append(popped)
    #     for val in popped['isAfter']:
    #         md[val]['isBefore'] -= 1
    popped = md.pop(soleValue)
    popped['letter'] = key
    # completeVal.append(popped)
    for val in popped['isAfter']:
        md[val]['isBefore'] -= 1
    return soleValue
    # return (values, completeVal)

def removeFromString(md, charRmv):
    print('removing', charRmv)
    for i in range(26):
        if md[i] is None:
            continue
        if md[i] is not '' and md[i] is not -1:
            indRmv = md[i].find(charRmv)
            if indRmv is not -1:
                # print(i)
                upperHalf = md[i][0:indRmv]
                lowerHalf = md[i][indRmv + 1:] if len(md[i]) > indRmv + 2 else ''
                md[i] = upperHalf + lowerHalf
            # else:
                # print(i, charRmv, 'is not a prereq')
        # else:
            # print(i, 'nothing to remove')
    
    return md

def constructString(md):
    instructions = ''
    done = False
    count = 0
    # while not done and count < 10:
    while not done:
        done = True
        for i in range(26):
            #  iterate once and break when none
            print(i, md[i])
            if md[i] is '':
                # cast ord
                removeChar = chr(i + A_ORD)
                print(removeChar)
                instructions += removeChar
                md = removeFromString(md, removeChar)
                md[i] = -1
                print('set', removeChar, i, 'to -1')
                done = False
                # break <- should break tho???
            elif md[i] is not -1 and md[i] is not None:
                done = False
        count += 1
        print(count, ': done another iter, done is', 'true' if done else 'false', 'string is', instructions)
    return instructions

def main():
    # metadata = parseInput('d7.in')
    # metadata = parseInput('d7-testEdge.in')
    metadata = parseInput('d7-test.in')
    # metadata = parseInput('d7-test2.in')

    # sort md strings
    for i in range(26):
        if metadata[i] is not '' and metadata[i] is not None:
            metadata[i] = ''.join(sorted(metadata[i]))
    result = constructString(metadata)
    # print(metadata)
    # print(result)


main()
