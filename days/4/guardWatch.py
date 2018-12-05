# finalement might not need
# from datetime import datetime # woah libraries step up
from copy import copy # of all the libraries...
dutyBook = {} # where date = primary key
guardWatch = {} # where guardid = primary key (keep track of sleep)

def parseSingleRecord(recordLine):
    global dutyBook
    global guardWatch
    # from '[YYYY-MM-DD HH:MM] event' to
    # { date: MMDD, event: (one of 'g'/'w'/'f'), minutes: MM (doesn't matter if event = g), guardId: null if w/f; else id}
    predate, event = recordLine.split('] ')
    predate = predate[1:] # remove the '['

    # print(predate, event)
    fulldate, fulltime = predate.split(' ')

    mmdd = int(''.join(fulldate.split('-')[1:]))
    hour, minutes = [int(val) for val in fulltime.split(':')]

    # switch cases -- and where i discover python doesn't support switches?
    e = event[0].lower()
    guardId = ''
    # print (mmdd, hour, minutes, e)

    # sort key because i'm lazy
    # sortkey = mmdd * 1000 + 100 * hour + minutes # why do you not assign by value???
    sortkey = int(''.join(fulldate.split('-')[:][1:])) * 10000 + 100 * hour + minutes
    # print(sortkey, fulldate, fulltime)

    # important that only 1 guard per date => can use date as primary key instead
    # wait no can't because harder to find who slept more... or would it? -> maybe later
    if e == 'g':
        # parse out guard id
        guardId = event.split(' ')[1] # 'Guard #xx begins shift'
        if hour == 23:
            mmdd += 1 # shift starts at midnight on next day
        dutyBook[mmdd] = guardId

        if guardId not in guardWatch:
            guardWatch[guardId] = [0] * 60
        # dutyBook[guardId]['onDuty'].append(mmdd) # adds to duty book
        return { 'date': mmdd, 'event': e, 'minutes': minutes, 'guardId': guardId, 'sortkey': sortkey }

    return { 'date': mmdd, 'event': e, 'minutes': minutes, 'guardId': '', 'sortkey': sortkey }



def parseReposeRecords(pathToFile):
    global dutyBook
    global guardWatch
    inputFile = open(pathToFile, 'r')

    # ultimately:
    # { guardId: '#xx', onDuty: [718, 204, 131, 1230],
    #  timeAsleep: [0,0,0,4,...] } (timeAsleep is an array of 60 elements)
    # allRecords = [parseSingleRecord(line) for line in inputFile if line.strip() and parseSingleRecord(line)]
    allRecords = [parseSingleRecord(line) for line in inputFile if line.strip()]

    inputFile.close()

    # continuing on...
    # once we have a dutybook, no need to sort
    # no wait -- still require sorting

    allRecords.sort(key=sortByDate)
    previousAsleepTime = 60
    currentGuard = ''
    for line in allRecords:
        # print(line)
        recordGuardId = line['guardId']
        if recordGuardId:
            # print(line['date'], 'changed guard from', currentGuard, 'to', recordGuardId, 'or new shift')
            if previousAsleepTime < 60:
                for x in range(previousAsleepTime, 60):
                    guardWatch[currentGuard][x] += 1
            currentGuard = recordGuardId # update to new guard
            previousAsleepTime = 60
            continue
        if line['event'] == 'w':
            for x in range(previousAsleepTime, line['minutes']):
                guardWatch[currentGuard][x] += 1
            previousAsleepTime = 60
        elif line['event'] == 'f':
            previousAsleepTime = line['minutes']
        # nightGuard = dutyBook[line['date']] # get guard id -- extra step due to sorting... ah well

def sortByDate(record):

    return record['sortkey']

def getTotalAndMost(guardWatchFile):
    totAndMost = {}
    sleepiest = ''
    mostTimesAsleep = ''
    for guard in guardWatchFile.keys():
        mostAsleepMin = -1
        amount = 0
        total = 0
        for x in range(0, len(guardWatchFile[guard])):
            total += guardWatchFile[guard][x]
            if mostAsleepMin == -1 or guardWatchFile[guard][x] > guardWatchFile[guard][mostAsleepMin]:
                mostAsleepMin = x
                amount = guardWatchFile[guard][x]
        if not sleepiest or totAndMost[sleepiest]['total'] < total:
            sleepiest = guard
        if mostAsleepMin > -1:
            amount = guardWatch[guard][mostAsleepMin]

        totAndMost[guard] = { 'total': total, 'mostAsleepMin': mostAsleepMin, 'amount': amount }

        if not mostTimesAsleep or totAndMost[mostTimesAsleep]['amount'] < amount:
            mostTimesAsleep = guard


    print('part 1:', sleepiest, totAndMost[sleepiest])
    print('part 2:', mostTimesAsleep, totAndMost[mostTimesAsleep])
    return totAndMost

parseReposeRecords('d4.in')
# print(guardWatch['#10'])
totalsAndMost = getTotalAndMost(guardWatch)
# print(totalsAndMost)
