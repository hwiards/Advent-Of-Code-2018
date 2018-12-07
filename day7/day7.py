from Input import Input as In
import Input
from typing import List
import time
from Helper import getAllNumbers, manhatten_distance, alphabet
import operator
from typing import List, Iterator
import re


def getFirstNext(lines: List[str]):
    numbers: Iterator[Iterator[str]] = map(lambda s: map(str, re.findall(r'\s\w\s', s)), lines)
    return [[ch.strip() for ch in x] for x in numbers]  # Leicht printbar


def part1(lines):
    firstNext = getFirstNext(lines)

    nodeDict = dict()

    for start, next in firstNext:
        if not start in nodeDict:
            nodeDict[start] = Node(start)

        if not next in nodeDict:
            nodeDict[next] = Node(next)

        nodeDict[start].output.append(next)
        nodeDict[next].input.append(start)


    reihenfolge = ""
    empty = False
    while not empty:
        len0 = []
        for key in nodeDict:
            node = nodeDict[key]
            if len(node.input) == 0:
                len0.append(node)

        if not len(len0) == 0:
            len0.sort(key=lambda node: node.name)
            reihenfolge += len0[0].name

            for next in len0[0].output:
                nodeDict[next].input.remove(len0[0].name)
            del nodeDict[len0[0].name]
        else:
            empty = True

    print(reihenfolge)
    return reihenfolge



def part2(lines, offset, numWorker):
    firstNext = getFirstNext(lines)

    nodeDict = dict()
    workers= dict()

    for workerID in range(numWorker):
        workers[workerID] = ("-1",0);

    for start, next in firstNext:
        if not start in nodeDict:
            nodeDict[start] = Node(start)

        if not next in nodeDict:
            nodeDict[next] = Node(next)

        nodeDict[start].output.append(next)
        nodeDict[next].input.append(start)


    reihenfolge = ""
    empty = False
    ticks = 0
    alpha = alphabet.upper()
    while dict:
        len0 = []
        delJob = []
        for key in nodeDict:
            node = nodeDict[key]
            if len(node.input) == 0:
                len0.append(node)


        ## Tick
        for workerID in workers:
            jobname, timeleft = workers[workerID]
            workers[workerID] = (jobname, max(timeleft - 1,0))

        ticks += 1

        for workerID in workers:
                for job in len0.copy():
                    jobname, timeleft = workers[workerID]
                    if timeleft == 0:
                        name = job.name
                        if not name in nodeDict:
                            continue
                        if jobname != "-1":
                            delJob.append(jobname)


                        timeofnewjob = alpha.find(job.name) + offset +1
                        taken = job.taken
                        if not taken:
                            workers[workerID] = (name, timeofnewjob)
                            len0.remove(job)
                            nodeDict[job.name].taken = True
                            continue




        delJob.sort()
        for job in delJob:
            if not job in nodeDict:
                continue

            reihenfolge += job


            for next in nodeDict[job].output:
                nodeDict[next].input.remove(nodeDict[job].name)
            del nodeDict[job]

    print(ticks)
    return ticks


class Node:


    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
        self.input = []
        self.output = []
        self.taken = False















def main():
    start_time = time.time()
    input = In(7)
    lines: List[str] = input.lines(do_strip=True)

    testinput: List[str] = Input.linesTest(do_strip=True)

    # assert part1(testinput) == "CABDFE"
    # print("Part1 with Testdata okay")
    # print(part1(lines))

    assert part2(testinput, 0, 2) == 15
    print("Part2 with Testdata okay")
    print(part2(lines))

    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__": main()
