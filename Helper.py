import re
from typing import List, Iterator

alphabet = "abcdefghijklmnopqrstuvwxyz"

def getAllNumbers(lines: List[str]):
    numbers: Iterator[Iterator[int]] = map(lambda s: map(int, re.findall(r'-?\d+', s)), lines)
    return [list(x) for x in numbers]  # Leicht printbar


## Coordinaten

def X(point): return point[0]
def Y(point): return point[1]

HEADINGS = UP, LEFT, DOWN, RIGHT = (0, -1), (-1, 0), (0, 1), (1, 0)

def turn_right(heading): return HEADINGS[HEADINGS.index(heading) - 1]
def turn_around(heading): return HEADINGS[HEADINGS.index(heading) - 2]
def turn_left(heading):  return HEADINGS[HEADINGS.index(heading) - 3]


origin = (0, 0)

def manhatten_distance(P, Q=origin):
    "Manhatten distance between two points."
    return sum(abs(p - q) for p, q in zip(P, Q))


def euklidian_distance(P, Q=origin):
    "Straight-line (hypotenuse) distance between two points."
    return sum((p - q) ** 2 for p, q in zip(P, Q)) ** 0.5
