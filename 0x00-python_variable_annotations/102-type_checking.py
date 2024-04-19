from typing import Tuple, List, Sequence

def zoom_array(lst: Sequence[int], factor: int = 2) -> List[int]:
    """
    Zooms in on the elements of a given sequence by duplicating each element
    according to the specified factor.

    Args:
        lst (Sequence[int]): The input sequence of integers to be zoomed in.
        factor (int): The factor by which to zoom in (default is 2).

    Returns:
        List[int]: The zoomed-in list of integers.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in