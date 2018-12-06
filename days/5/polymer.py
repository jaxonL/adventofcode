# assuming ascii input
test1 = 'dabAcCaCBAcCcaDA'
test2 = 'aabAAB'
test3 = 'Xxadf'
test4 = 'XxSsdDIijNnJACszZScZfFhHQyYrRqzdXTtxDEeNnGgOaAcCMcCLlMmogQeEqGgFfGyYuUOIiYyhHlLmUulAUKkudDOoDdaLGRrgoDdDdGgRruUhJLljQqdwWDZzHXxppPTwWCcZzDmfFlLPpdDSsgGtFfTEeTOotyYMOGgkJjKZUuQdNnDhHvVntKkTNqTjJeEVkZzttTYyTDdIiRrqQyYYyxbBXLlKHhvtYyzoKMmiIkaAUvVuvEejoOJUuQoOLlLloOxoOXaAqYYXxyzMmZyoOVhHIiIKfFkiIKAaUukRrKQqASsakLgGlGgLxXhHmcCzZxXMWdUulLJjDwnNYkKFfZzpPVuUvHhbQqIiLRrlEeVvBQJjlLGgjYyJoAalxXuUqgGQLQqOqNJjzZnyOusSUeEFfodcLuUlCcCIiNnGgaADVwWGgvZtTewWENnSszBKkDdeEYyt'
expected4 = 'ApTDILBt'

DIFFERENCE = ord('a') - ord('A')

def parsePolymerString(source):
    global DIFFERENCE
    # start with simple string
    baseBuffer = ''
    count = 0
    while True: # iter for reading in chars
        if count >= len(source):
            break
        currChar = source[count]
        count += 1
        lastIndex = len(baseBuffer) - 1
        if lastIndex < 0: # nothing to compare to
            baseBuffer += currChar
            count += 1
            continue
        previousChar = baseBuffer[lastIndex]
        # print(count, lastIndex)
        # print('res =', abs(ord(currChar) - ord(previousChar)), '|', currChar, ord(currChar), '-', previousChar, ord(previousChar))
        # print(DIFFERENCE)
        while DIFFERENCE == abs(ord(currChar) - ord(previousChar)): # if equal, update curr and prev
            # print(previousChar, 'and', currChar)
            baseBuffer = baseBuffer[:lastIndex] # remove the thing

            # update previous char
            lastIndex = lastIndex - 1
            # print(lastIndex)
            # print(len(baseBuffer))
            if lastIndex < 0:
                break
            previousChar = baseBuffer[lastIndex]

            # read in comparison char
            count += 1
            if count >= len(source):
                break
            currChar = source[count]

        if lastIndex >= 0:
            baseBuffer += currChar

    return baseBuffer

# print(parsePolymerString(test1)) # logic works -- now to parse file
# print('string parse:', parsePolymerString(test4)) # logic works -- now to parse file
# print('expected:', expected4)

def parsePolymer():
    inputFile = open('d5.in', 'r')

    global DIFFERENCE
    # start with simple string
    baseBuffer = ''
    previousChar = ''
    while True: # iter for reading in chars
        # print(baseBuffer)
        currChar = inputFile.read(1)
        if not currChar: # eof
            print('eof')
            break
        if not previousChar: # nothing to compare to
            # print('last ind', lastIndex, 'nothing to compare to')
            baseBuffer += currChar
            previousChar = currChar
            continue
        # print(baseBuffer, ' -- read', currChar, '-- comparing to', previousChar)
        # print('res =', abs(ord(currChar) - ord(previousChar)), '|', currChar, ord(currChar), '-', previousChar, ord(previousChar))
        while DIFFERENCE == abs(ord(currChar) - ord(previousChar)):
            # print('\t', previousChar, currChar, 'match') # it's a match!!
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


    inputFile.close()
    return baseBuffer
polymer = parsePolymer()
# print('polymer:', polymer)
print('polymer len:', len(polymer))
