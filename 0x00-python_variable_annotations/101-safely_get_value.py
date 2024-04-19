from typing import Mapping, Any, TypeVar, Union

# Define a type variable ~T to represent the type of the default value
T = TypeVar('T')

def safely_get_value(dct: Mapping[Any, Any], key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely retrieves a value from a dictionary `dct` based on `key`.
    If `key` is present in `dct`, returns the corresponding value.
    Otherwise, returns the specified `default` value (or `None` if not provided).

    Args:
        dct (Mapping[Any, Any]): The dictionary from which to retrieve the value.
        key (Any): The key to lookup in the dictionary `dct`.
        default (Union[T, None], optional): The default value to return if `key` is not found. Defaults to None.

    Returns:
        Union[Any, T]: The value corresponding to `key` in `dct` if present, otherwise `default`.
    """
    if key in dct:
        return dct[key]
    else:
        return default