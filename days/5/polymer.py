# assuming ascii input
test1 = 'dabAcCaCBAcCcaDA'
test2 = 'aabAAB'
test3 = 'Xxadf'
test4 = 'XxSsdDIijNnJACszZScZfFhHQyYrRqzdXTtxDEeNnGgOaAcCMcCLlMmogQeEqGgFfGyYuUOIiYyhHlLmUulAUKkudDOoDdaLGRrgoDdDdGgRruUhJLljQqdwWDZzHXxppPTwWCcZzDmfFlLPpdDSsgGtFfTEeTOotyYMOGgkJjKZUuQdNnDhHvVntKkTNqTjJeEVkZzttTYyTDdIiRrqQyYYyxbBXLlKHhvtYyzoKMmiIkaAUvVuvEejoOJUuQoOLlLloOxoOXaAqYYXxyzMmZyoOVhHIiIKfFkiIKAaUukRrKQqASsakLgGlGgLxXhHmcCzZxXMWdUulLJjDwnNYkKFfZzpPVuUvHhbQqIiLRrlEeVvBQJjlLGgjYyJoAalxXuUqgGQLQqOqNJjzZnyOusSUeEFfodcLuUlCcCIiNnGgaADVwWGgvZtTewWENnSszBKkDdeEYyt'
expected4 = 'ApTDILBt'

DIFFERENCE = ord('a') - ord('A')
INDEX_SHIFT = ord('A')

# initial code used to logic my way around the problem before involving file input
# def parsePolymerString(source):
#     global DIFFERENCE
#     # start with simple string
#     baseBuffer = ''
#     count = 0
#     while True: # iter for reading in chars
#         if count >= len(source):
#             break
#         currChar = source[count]
#         count += 1
#         lastIndex = len(baseBuffer) - 1
#         if lastIndex < 0: # nothing to compare to
#             baseBuffer += currChar
#             count += 1
#             continue
#         previousChar = baseBuffer[lastIndex]
#         # print(count, lastIndex)
#         # print('res =', abs(ord(currChar) - ord(previousChar)), '|', currChar, ord(currChar), '-', previousChar, ord(previousChar))
#         # print(DIFFERENCE)
#         while DIFFERENCE == abs(ord(currChar) - ord(previousChar)): # if equal, update curr and prev
#             # print(previousChar, 'and', currChar)
#             baseBuffer = baseBuffer[:lastIndex] # remove the thing
#
#             # update previous char
#             lastIndex = lastIndex - 1
#             # print(lastIndex)
#             # print(len(baseBuffer))
#             if lastIndex < 0:
#                 break
#             previousChar = baseBuffer[lastIndex]
#
#             # read in comparison char
#             count += 1
#             if count >= len(source):
#                 break
#             currChar = source[count]
#
#         if lastIndex >= 0:
#             baseBuffer += currChar
#
#     return baseBuffer

# print(parsePolymerString(test1)) # logic works -- now to parse file
# print('string parse:', parsePolymerString(test4)) # logic works -- now to parse file
# print('expected:', expected4)

def parsePolymer(characterOccurenceCounter, filename):
    inputFile = open(filename, 'r')

    global DIFFERENCE
    global INDEX_SHIFT
    # start with simple string
    baseBuffer = ''
    previousChar = ''
    while True: # iter for reading in chars
        # print(baseBuffer)
        currChar = inputFile.read(1).strip()
        if not currChar: # eof
            # print('eof')
            break
        if not previousChar: # nothing to compare to
            # print('last ind', lastIndex, 'nothing to compare to')
            baseBuffer += currChar
            characterOccurences[ord(currChar.upper()) - INDEX_SHIFT] += 1   # incr char occurence in final string
            previousChar = currChar
            continue
        # print(baseBuffer, ' -- read', currChar, '-- comparing to', previousChar)
        # print('res =', abs(ord(currChar) - ord(previousChar)), '|', currChar, ord(currChar), '-', previousChar, ord(previousChar))
        while DIFFERENCE == abs(ord(currChar) - ord(previousChar)):
            # print('\t', previousChar, currChar, 'match') # it's a match!!
            characterOccurences[ord(currChar.upper()) - INDEX_SHIFT] -= 1   # decr char occurence in final string
            lastIndex = len(baseBuffer) - 1
            # case 1 - after comp, baseBuffer is empty -> main loop
            if lastIndex == 0:
                baseBuffer = '' # pop the char we matched
                previousChar = ''
                break
            # case 2 - after comp, baseBuffer has more chars -> stay in secondary loop
            baseBuffer = baseBuffer[:lastIndex] # remove the thing
            # update previous char
            previousChar = baseBuffer[lastIndex - 1]
            # print('\tinner loop; new buffer:', baseBuffer)

            # read in comparison char
            currChar = inputFile.read(1)
            # print('\tinner loop; next char (not comp\'ed yet):', currChar, 'to prevc', previousChar)
            if not currChar:
                break

            # print(lastIndex)
            # print(len(baseBuffer))
            # if lastIndex < 0:
            #     break
            # previousChar = baseBuffer[lastIndex]

            # print('\treverse comparison - read', currChar, '-- comparing to', previousChar, 'at ind', lastIndex)

        # # if lastIndex >= 0:
        # if not currChar:
        #     break
        # if lastIndex >= 0:
        #     baseBuffer += currChar

        # case 1 (outside of inner loop): should not add anything and just continue the loop
        if not previousChar:
            continue
        # case 3 if currChar and previousChar are different, append it
        baseBuffer += currChar
        previousChar = currChar
        characterOccurences[ord(currChar.upper()) - INDEX_SHIFT] += 1   # incr char occurence in final string


    inputFile.close()
    return baseBuffer

def replaceAllOf(char, targetString):
    # O(n) soln
    resultingString = ''
    for x in targetString:
        if x.lower() != char.lower():
            resultingString += x
    return resultingString

def getFoldOccurences(reducedPolymer):
    occurences = [0] * 26
    totalLength = len(reducedPolymer) # try to reduce times calculated
    for x in range(totalLength):
        currChar = reducedPolymer[x]
        distanceFromX = 1
        while (x + distanceFromX < totalLength) and (x - distanceFromX > -1): # while these indices still exist
            lhsChar = reducedPolymer[x - distanceFromX]
            rhsChar = reducedPolymer[x + distanceFromX]
            if DIFFERENCE == abs(ord(lhsChar) - ord(rhsChar)):
                distanceFromX += 1
            else:
                break
        occurences[ord(currChar.upper()) - INDEX_SHIFT] += distanceFromX - 1   # incr char occurence
        # print(currChar, 'contributes', distanceFromX -1, 'folds -- total', occurences[ord(currChar.upper()) - INDEX_SHIFT])
    return occurences

characterOccurences = [0] * 26 # for 26 letters in the alphabet
polymer = parsePolymer(characterOccurences, 'd5.in')
foldsDueToChar = getFoldOccurences(polymer)


# print('polymer:', polymer)
print('1st polymer len:', len(polymer))
# for x in range(1,len(polymer)):
#     print(x, ':', polymer[x])
maxInd = 0
for x in range(26):
    # print(chr(x + INDEX_SHIFT), ':', foldsDueToChar[x], chr(maxInd + INDEX_SHIFT), '(max):', foldsDueToChar[maxInd])
    if foldsDueToChar[x] > foldsDueToChar[maxInd]:
        # print(chr(x + INDEX_SHIFT), '>', chr(maxInd + INDEX_SHIFT))
        maxInd = x
    # elif foldsDueToChar[x] == foldsDueToChar[maxInd]:
        # print('equality for', chr(x + INDEX_SHIFT), chr(maxInd + INDEX_SHIFT))
    # else:
        # print(chr(x + INDEX_SHIFT), '<', chr(maxInd + INDEX_SHIFT))

removeChar = chr(maxInd + INDEX_SHIFT)
# print(removeChar)

newPolymer = replaceAllOf(removeChar, polymer)
# print(newPolymer) # used in the console with output directed to a file called secondPart.in
notUseful = [0]*26
finalPolymer = parsePolymer(notUseful, 'secondPart.in')
print('final length:', len(finalPolymer))
