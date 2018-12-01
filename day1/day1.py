from Input import Input

input = Input(1)
lines = input.lines()

vals = set()


def main():
    aktVal = 0
    double = False

    while not double:
        for line in lines:
            line = line.strip()
            val = int(line)
            aktVal += val

            # Part 2
            if aktVal in vals:
                print('double: ' + str(aktVal))
                double = True
                break
            vals.add(aktVal)
            # Ende Part 2

    print(aktVal)


if __name__ == "__main__": main()
