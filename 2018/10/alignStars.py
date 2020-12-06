import re

MATCH_PATTERN = re.compile('position=<(( )*(-)?\d+), (( )*(-)?\d+)> velocity=<(( )*(-)?\d+), (( )*(-)?\d+)>')
def parsePoints(line):
    global MATCH_PATTERN
    coordx, coordy, vx, vy = MATCH_PATTERN.match(line).group(1, 4, 7, 10)
    coordx = int(coordx.strip())
    coordy = int(coordy.strip())
    vx = int(vx.strip())
    vy = int(vy.strip())

    print('(', coordx, ',', coordy, ') at x:', vx, 'y:', vy)

    return { 'coord': (coordx, coordy), 'velocity': (vx, vy) }

def main():
    inputFile = open('d10-test.in')
    parsedPoints = [parsePoints(line) for line in inputFile if line.strip()]
    inputFile.close()

main()
