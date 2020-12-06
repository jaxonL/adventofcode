inputFile = open('d2.in', 'r') # getting used to no semicolons

# realised i could also just work on the input directly instead of storing it somewhere
counter = 0
doubleLetters = 0
tripleLetters = 0

for packageId in inputFile:
    packageId = packageId.strip() # and not trim()
    if packageId:
        counter += 1
        print(counter, ': ', packageId)
        # could do dict and map, but require 2 iterations
        once = []
        twice = []
        thrice = []
        more = []
        for letter in packageId:
            if letter in more:
                continue
            elif letter in thrice:
                thrice.remove(letter)
                more.append(letter)
            elif letter in twice:
                twice.remove(letter)
                thrice.append(letter)
            elif letter in once:
                once.remove(letter)
                twice.append(letter)
            else:
                once.append(letter)
        if len(twice):
            doubleLetters += 1
        if len(thrice):
            tripleLetters += 1

print('double: ', doubleLetters)
print('triple: ', tripleLetters)
print('checksum: ', doubleLetters * tripleLetters)
inputFile.close()
