import re
from typing import List, Iterator


def getAllNumbers(lines: List[str]):
    numbers: Iterator[Iterator[int]] = map(lambda s: map(int, re.findall(r'-?\d+', s)), lines)
    return [list(x) for x in numbers]  # Leicht printbar

