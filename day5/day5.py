from Input import Input as In
import Input
from typing import List
import time


def part1(lines):
    for line in lines:
        changed = True
        aktLine = line
        while changed:
            changed = False
            lenght = len(aktLine)
            # print(aktLine)
            # for start in range((len(aktLine) - 1)):
            #     # print("start: ", start, " lenLine: ", len(aktLine) - 1," Len(line): ", len(aktLine))
            #     if aktLine[start].islower() and aktLine[start + 1].isupper():
            #         if aktLine[start] == aktLine[start + 1].lower():
            #             aktLine = aktLine[:start] + (aktLine[start + 2:] if start + 2 < len(aktLine) else [])
            #             changed = True
            #             break
            #     elif aktLine[start].isupper() and aktLine[start + 1].islower():
            #         if aktLine[start].lower() == aktLine[start + 1]:
            #             aktLine = aktLine[:start] + (aktLine[start + 2:] if start + 2 < len(aktLine) else [])
            #             changed = True
            #             break
            for start in range(26):
                ch = chr(ord('a') + start)
                aktLine = aktLine.replace(ch+ch.upper(),"").replace(ch.upper()+ch,"")
            if len(aktLine) < lenght:
                changed = True


        return len(aktLine)


def part2(lines):
    for line in lines:
        shortest = len(line)
        for start in range(26):
            ch = chr(ord('a') + start)
            aktLine = line
            trimmed = [a for a in aktLine if a.lower() != ch]
            lenght = part1(["".join(trimmed)])
            if lenght < shortest:
                shortest = lenght

        return shortest


def main():
    start_time = time.time()
    input = In(5)
    lines: List[str] = input.lines(do_strip=True)

    testinput: List[str] = Input.linesTest(do_strip=True)

    assert part1(testinput) == 10
    print("Part1 with Testdata okay")
    print(part1(lines))

    assert part2(testinput) == 4
    print("Part2 with Testdata okay")
    print(part2(lines))

    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__": main()
