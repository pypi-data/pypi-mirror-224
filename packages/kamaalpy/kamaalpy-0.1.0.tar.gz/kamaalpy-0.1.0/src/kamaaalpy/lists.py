from typing import Iterable, TypeVar, Callable


ItemsTypeVar = TypeVar("ItemsTypeVar")


def all_satisfy(
    items: Iterable[ItemsTypeVar], predicate: Callable[[ItemsTypeVar], bool]
):
    for item in items:
        if not predicate(item):
            return False

    return True


def find_index(
    items: list[ItemsTypeVar], predicate: Callable[[ItemsTypeVar], bool]
) -> int | None:
    for index, item in enumerate(items):
        if predicate(item):
            return index


def removed(items: list[ItemsTypeVar], index: int) -> list[ItemsTypeVar]:
    if index >= len(items):
        return items

    new_list = items.copy()
    del new_list[index]
    return new_list
