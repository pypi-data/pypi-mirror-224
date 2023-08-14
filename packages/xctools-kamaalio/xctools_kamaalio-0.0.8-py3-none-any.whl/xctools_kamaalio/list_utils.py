from typing import TypeVar, Callable


ItemsTypeVar = TypeVar("ItemsTypeVar")


def find_index(
    items: list[ItemsTypeVar], predicate: Callable[[ItemsTypeVar], bool]
) -> int | None:
    for index, item in enumerate(items):
        if predicate(item):
            return index


def removed(items: list[ItemsTypeVar], index: int) -> list[ItemsTypeVar]:
    new_list: list[ItemsTypeVar] = []
    for items_index, item in enumerate(items):
        if items_index != index:
            new_list.append(item)
    return new_list
