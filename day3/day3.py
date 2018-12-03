from Input import Input


def day3(lines):
    w, h = 1000, 1000;
    Matrix = [[0 for x in range(w)] for y in range(h)]
    Claims = [[[] for x in range(w)] for y in range(h)]
    claims = [0 for x in range(len(lines) + 1)]
    claims[0] = -1

    for line in lines:
        claim = int(line.split(' @ ')[0][1:])
        secondPart = line.split(' @ ')[1]
        dimensions = secondPart.split(': ')
        starts = dimensions[0].split(',')
        lengths = dimensions[1].split('x')

        startx = int(starts[0])
        starty = int(starts[1])
        width = int(lengths[0])
        height = int(lengths[1])

        for x in range(startx, startx + width):
            for y in range(starty, starty + height):
                Matrix[x][y] = Matrix[x][y] + 1
                Claims[x][y].append(claim)


    #Part 1
    count = 0

    for x in range(w):
        for y in range(h):
            if Matrix[x][y] > 1:
                count = count + 1

    print("Part 1: ", count)


    #Part 2
    for x in range(w):
        for y in range(h):
            if len(Claims[x][y]) > 1:
                for claima in Claims[x][y]:
                    claims[claima] = 1

    for claima, value in enumerate(claims):
        if value == 0:
            print("Part 2: ", claima)



def main():
    input = Input(3)
    lines = input.lines(do_strip=True)
    day3(lines)


if __name__ == "__main__": main()
