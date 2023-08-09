from typing import List, Union


def unique_list(list_to_check: List[Union[str, int]]):
    """
    Unifies items in a list.
    """

    seen = set()
    seen_add = seen.add
    return [x for x in list_to_check if not (x in seen or seen_add(x))]
