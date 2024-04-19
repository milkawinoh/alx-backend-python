from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the specified multiplier.

    Args:
        multiplier (float): The multiplier to be used in the returned function.

    Returns:
        Callable[[float], float]: A function that takes a float and returns its product with the multiplier.
    """
    def multiplier_func(x: float) -> float:
        return x * multiplier
    
    return multiplier_func