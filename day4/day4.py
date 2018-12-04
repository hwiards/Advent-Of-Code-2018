from typing import List
from Input import Input
from Helper import getAllNumbers
import math

def part1(lines: List[str]):

    lines.sort()

    numbers = getAllNumbers(lines)

    h = 0
    m = 0
    m_start = 0
    guard = 0
    start = True

    GUARDS = dict()

    for line in numbers:
        print(line)
        if len(line) == 6:
            _, _, _, h, m, guard = line
            continue
        if len(line) == 5:
            _, _, _, h, m = line
            if guard not in GUARDS:
                GUARDS[guard] = [0 for x in range(60)]
            if start:
                start = False
                m_start = m
                continue

            times = GUARDS[guard]
            for minute in range(m_start, m):
                times[minute] = times[minute] + 1

            GUARDS[guard] = times
            start = True

    maxsum = 0
    maxguard = 0
    maxminute = 0
    maxminguard = 0

    for guard, minutes in GUARDS.items():
        if sum(minutes) > maxsum:
            maxsum = sum(minutes)
            maxguard = guard

        if max(minutes) > maxminute:
            maxminute = max(minutes)
            maxminguard = guard

    maxworked = 0
    maxmin = 0
    for minute, workedhours in enumerate(GUARDS[maxguard]):
        if workedhours > maxworked:
            maxworked = workedhours
            maxmin = minute


    for minute, workedhours in enumerate(GUARDS[maxminguard]):
        if workedhours == maxminute:
            print("part 2:", maxminguard, minute, maxminguard*minute)


    print(maxguard * maxmin)



def main():
    input = Input(4)
    lines: List[str] = input.lines(do_strip=True)
    part1(lines)


if __name__ == "__main__": main()