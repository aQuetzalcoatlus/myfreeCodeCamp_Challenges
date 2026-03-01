"""
Given an array, determine if it is flat.

An array is flat if none of its elements are arrays.
"""


def is_flat(arr: list) -> bool:
    item_flag: int = 0
    for item in arr:
        if isinstance(item, list):
            item_flag += 1
    print(f"Item flag value = {item_flag}")
    if item_flag == 0:
        return True
    else:
        return False


print(is_flat([1, [2, 3], 4]))
