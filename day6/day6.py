from Input import Input as In
import Input
from typing import List
import time
from Helper import getAllNumbers, manhatten_distance
import operator


def part1(lines):
    points = []
    numbers = getAllNumbers(lines)
    ID = 1
    for x, y in numbers:
        points.append((x,y, ID))
        ID += 1

    print(points)


    # xmin = min(min(blockingPoints, key=operator.itemgetter(0))[0]-100, 0)
    # xmax = max(blockingPoints, key=operator.itemgetter(0))[0]+100
    # ymin = min(min(blockingPoints, key=operator.itemgetter(1))[1]-100,0)
    # ymax = max(blockingPoints, key=operator.itemgetter(1))[1]+100

    xmin = min(points, key=operator.itemgetter(0))[0]
    xmax = max(points, key=operator.itemgetter(0))[0]
    ymin = min(points, key=operator.itemgetter(1))[1]
    ymax = max(points, key=operator.itemgetter(1))[1]

    # blockingPoints = set(points) - set(blockedPoints)
    blockedPoints = set([(x,y,ID) for x, y,ID in points if x > xmin and x < xmax and y > ymin and y < ymax ])
    # blockedPoints = isBlockedInBothCords(points)
    # blockedPoints = set(points) - blockingPoints
    blockedIDs = set([ID for x,y,ID in blockedPoints])

    xmin = 0
    ymin = 0
    xmax += 100
    ymax += 100


    w = xmax
    h = ymax
    Field = [[[] for x in range(w)]for y in range(h)]

    for point in points:
        _, _, ID = point
        for x in range(xmin, xmax):
            for y in range(ymin, ymax):
                dist = manhatten_distance(point, (x,y))
                distTup = (dist, ID)
                if len(Field[y][x]) == 0:
                    Field[y][x].append(distTup)
                else:
                    for otherDist, otherID in Field[y][x]:
                        if otherDist > dist:
                            Field[y][x].clear()
                            Field[y][x].append(distTup)

                        elif otherDist == dist:
                            Field[y][x].append(distTup)
                        break


    numberOfUnique = [0 for x in range(len(points)+1)]

    for x in range(w):
        for y in range(h):
            if len(Field[y][x]) == 1:
                dist, ID = Field[y][x][0]
                if ID in blockedIDs:
                    numberOfUnique[ID] = numberOfUnique[ID] + 1

    print(max(numberOfUnique))
    return max(numberOfUnique)


def isBlockedInBothCords(points):

    blockedPoints = set()
    # print("len: ", len(points))

    for point in points:
        x, y, ID = point
        for otherpoint in points:
            ox, oy, ID = otherpoint
            if(ox < x and oy < y):
                for sndother in points:
                    sx, sy, _ = sndother
                    if sx > x and sy > y:
                        blockedPoints.add(point)

            if(ox < x and oy > y):
                for sndother in points:
                    sx, sy, _ = sndother
                    if sx > x and sy < y:
                        blockedPoints.add(point)


    # print("Blocked: ", blockedPoints)
    # print("len: ", len(blockedPoints))

    return blockedPoints












def main():
    start_time = time.time()
    input = In(6)
    lines: List[str] = input.lines(do_strip=True)

    testinput: List[str] = Input.linesTest(do_strip=True)

    assert part1(testinput) == 17
    print("Part1 with Testdata okay")
    print(part1(lines))

    # assert part2(testinput) == 4
    # print("Part2 with Testdata okay")
    # print(part2(lines))

    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__": main()


