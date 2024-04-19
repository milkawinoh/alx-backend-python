from typing import Union

def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    """
    Create a tuple with a key-value pair where the value is squared.

    Args:
        k (str): The key as a string.
        v (Union[int, float]): The value, which can be an integer or a float.

    Returns:
        tuple[str, float]: A tuple containing the key `k` and the square of `v` as a float.
    """
    squared_value = float(v * v)  # Calculate the square of `v` and convert to float
    return (k, squared_value)