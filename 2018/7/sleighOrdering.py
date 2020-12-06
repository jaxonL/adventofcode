
def parseInput(filename):
    inputFile = open(filename, 'r')
    metadata = {}

    for line in inputFile:
        if line.strip():
            prereq = line.split(' ')[1]
            step = line.split(' ')[7]

            # print(prereq, '->', step)
            if prereq not in metadata:
                metadata[prereq] = { 'isBefore': 1, 'isAfter': [], 'largestBefore': '' }
            else:
                metadata[prereq]['isBefore'] += 1

            if step not in metadata:
                metadata[step] = { 'isBefore': 0, 'isAfter': [prereq], 'largestBefore': '' }
            else:
                metadata[step]['isAfter'].append(prereq)
                metadata[step]['largestBefore'] = prereq if prereq > metadata[step]['largestBefore'] else metadata[step]['largestBefore']
    inputFile.close()
    return metadata

def findZeroValues(md):
    values = []
    for key in md.keys():
        if md[key]['isBefore'] == 0:
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

def constructString(md):
    instructions = ''
    while len(md.keys()) != 0:
        # print(md)
        # find min key
        # valuesToOrder, completeValOrder = findZeroValues(md)
        removeVal = findZeroValues(md)
        # subtract

        # print(len(md.keys()))
        # organise
        # valuesToOrder.sort()
        # completeValOrder.sort(key=lambda x: len(x['isAfter']), reverse=True)
        # print(valuesToOrder)
        # print(completeValOrder)
        instructions = removeVal + instructions

    return instructions

def main():
    metadata = parseInput('d7.in')
    result = constructString(metadata)
    # print(metadata)
    print(result)


main()
