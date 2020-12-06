from collections import deque
import sys # to get command line arguments with sys.argv

def calculateHighScore(playerCount, maxMarbleValue):
    scoreBoard = [0] * playerCount # not elegant space-wise

    gameboard = deque([0])

    # marbleVal is also the turn number
    for marbleVal in range(1, maxMarbleValue + 1):
        # if not divisible by 23, rotate to the left by 1 and append
        if marbleVal % 23 != 0:
            gameboard.rotate(-1)
            gameboard.append(marbleVal)
        else:
            # divisible by 23 => add the value of the popped marble and this marble to the elf who is playing this turn
            gameboard.rotate(7)
            pointsEarned = gameboard.pop() + marbleVal
            elf = marbleVal % playerCount if marbleVal % playerCount else playerCount
            scoreBoard[elf - 1] += pointsEarned
            # rotate back by 1
            gameboard.rotate(-1)
        # print(gameboard)

    return max(scoreBoard)

def main():
    if len(sys.argv) < 3:
        print('Player count and/or max marble value is/are missing. Exiting...')
        exit(1)

    print(calculateHighScore(int(sys.argv[1]), int(sys.argv[2])))


main()
