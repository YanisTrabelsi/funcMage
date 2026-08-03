from collections.abc import Callable
from typing import Any
from operator import add, mul
from functools import reduce, partial, lru_cache


def spell_reducer(spells: list[int], operation: str) -> int:
    operator: Callable | None = None
    if (len(spells) == 0):
        return 0
    if (operation == "add"):
        operator = add
    elif (operation == "multiply"):
        operator = mul
    elif (operation == "max"):
        operator = max
    elif (operation == "min"):
        operator = min
    else:
        raise ValueError(f"Unknow operator '{operation}'")
        return
    return reduce(operator, spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fire_spell = partial(base_enchantment, 50, "fire")
    ice_spell = partial(base_enchantment, 50, "ice")
    wind_spell = partial(base_enchantment, 50, "wind")
    return {"fire": fire_spell,
            "ice": ice_spell,
            "wind": wind_spell}

@lru_cache
def memoized_fibonacci(n: int) -> int:
    if (n < 2):
        return 1
    return memoized_fibonacci(n - 2) + memoized_fibonacci(n - 1)


def spell_dispatcher() -> Callable[[Any], str]:
    ...


def spell(power: int, element: str, target: str):
    return f"{element} spell deals {power} damages to {target} !"


if (__name__ == "__main__"):
    fire_spell = partial_enchanter(spell)["fire"]
    ice_spell = partial_enchanter(spell)["ice"]
    wind_spell = partial_enchanter(spell)["wind"]

    print("== Spell Reducer ==")
    print(spell_reducer([1, 10, 4, 7], "add")) 

    print("\n== Partial_enchanter ==")
    print(fire_spell("Dragon"))
    print(ice_spell("Goblin"))
    print(wind_spell("Orc"))

    print("\n== Memoized fibonacci ==")
    print(memoized_fibonacci(1996))
