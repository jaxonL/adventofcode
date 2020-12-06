inputFile = open('d2.in', 'r')

allPackageIds = [line.strip() for line in inputFile if line.strip()]

# bruteforce times

# worst case: O(n!) :')

for x in range(len(allPackageIds) - 1): # only take up to second to last
    packageId = allPackageIds[x]
    matching = ''
    differentAt = -1
    for y in range(x + 1, len(allPackageIds)):
        matching = allPackageIds[y]
        different = 0
        for z in range(len(matching)):
            if packageId[z] != matching[z]:
                if different:
                    matching = ''
                    differentAt = -1
                    break
                else:
                    different += 1
                    differentAt = z
                    # print('differs once')
        if matching:
            break
    if matching:
        print(differentAt)
        print(packageId, 'and', matching)
        print(''.join([packageId[:differentAt], packageId[differentAt + 1:]]))
        print(''.join([matching[:differentAt], matching[differentAt + 1:]]))
        break

inputFile.close()
