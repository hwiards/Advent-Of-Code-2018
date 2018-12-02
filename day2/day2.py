from Input import Input
from collections import Counter


def part2(lines):
    for i, line in enumerate(lines):
        for compline in lines[i + 1:]:
            diff = 0
            pos = 0
            for charpos in range(len(line)):
                if line[charpos] != compline[charpos]:
                    diff = diff + 1
                    pos = charpos

            if diff == 1:
                print(line[:pos] + line[pos + 1:])


def part1(lines):
    twos = 0
    threes = 0

    for line in lines:
        two = False
        three = False

        b = ''.join(sorted(line))
        S = b.lower()
        d = Counter(S)

        for item, ct in d.items():
            if ct == 2:
                two = True
            if ct == 3:
                three = True

        if two:
            twos = twos + 1
        if three:
            threes = threes + 1

    print(twos * threes)


def main():
    input = Input(2)
    lines = input.lines(do_strip=True)

    part1(lines)
    part2(lines)


if __name__ == "__main__": main()
