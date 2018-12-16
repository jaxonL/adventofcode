def buildPatternDict(filename):
  inFile = open(filename, 'r')
  dict = {}
  for line in inFile:
    if line.strip():
      patt, arrow, newPlant = line.strip().split(' ')
      if newPlant == '#':
        # save to dictionary
        key = patt[2:5]
        prefix = patt[:2]
        if key not in dict.keys():
          dict[key] = [prefix]
        else:
          dict[key].append(prefix)
  inFile.close()
  return dict


def countPlants(genZero, dict, lastGen, dontAddFront):
    # print(genZero, lastGen)
    nextGen = genZero
    offset = 0
    tot = 0
    for i in range(lastGen):
        # print('next (b4 reass):', nextGen)
        # prevGen = '..' + nextGen + '..' if not dontAddFront else nextGen + '..'
        prevGen = '..' + nextGen + '..'
        # print('prev (after):', prevGen)
        # print(' ')
        offset -= 2
        nextGen = ''
        # print('prevgen len', len(prevGen))
        for j in range(len(prevGen)):
            currentPatt = prevGen[j:j + 3]
            while len(currentPatt) < 3:
                currentPatt += '.'
            # print(j, currentPatt)
            try:
                fertile = dict[currentPatt]
                prefixPatt = ''
                prevInd = j - 2
                if prevInd == -2:
                    prefixPatt = '..'
                elif prevInd == -1:
                    prefixPatt = '.' + prevGen[prevInd + 1:j]
                else:
                    prefixPatt = prevGen[prevInd:j]
                if prefixPatt in fertile:
                    nextGen += '#'
                else:
                    # print(j, 'not in fertile -- adding dot')
                    nextGen += '.'
            except:
                # print(j, 'no patt match -- adding dot')
                nextGen += '.'
            # print(j, 'building up next gen:', nextGen)
        # print('nextgen len', len(nextGen), '---', len(prevGen))
        # print(nextGen, offset)


    # offset = -4 if dontAddFront else offset
    # print(nextGen, offset)
    # offset should always be 40 if gen = 20
    for i in range(len(nextGen)):
        if nextGen[i] == '#':
            # print(i, '=>', i + offset)
            tot += (i + offset)
    return tot

def main():
  initialState = '##.###.......#..#.##..#####...#...#######....##.##.##.##..#.#.##########...##.##..##.##...####..####'
  testState = '#..#.#..##......###...###'
  # patternDict = buildPatternDict('patterns-test.in')
  patternDict = buildPatternDict('patterns.in')
  # print(patternDict)
  # count = countPlants(testState, patternDict, 20)
  # count = countPlants(initialState, patternDict, 20, False)
  count = countPlants(initialState, patternDict, 50000000000, False)
  print(count)

main()
