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
            length = len(aktLine)
            for start in range(26):
                ch = chr(ord('a') + start)
                aktLine = aktLine.replace(ch+ch.upper(),"").replace(ch.upper()+ch,"")
            if len(aktLine) < length:
                changed = True


        return len(aktLine)


def part2(lines):
    for line in lines:
        shortest = len(line)
        for start in range(26):
            ch = chr(ord('a') + start)
            aktLine = line
            trimmed = aktLine.replace(ch, "").replace(ch.upper(),"")
            lenght = part1([trimmed])
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
