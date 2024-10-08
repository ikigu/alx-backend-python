#!/usr/bin/env python3

"""Has element_length function"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list
    """
    return [(i, len(i)) for i in lst]
