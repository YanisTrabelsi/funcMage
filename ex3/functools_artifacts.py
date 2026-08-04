from collections.abc import Callable
from typing import Any
from operator import add, mul
from functools import reduce, partial, lru_cache, singledispatch


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
        return n
    return memoized_fibonacci(n - 2) + memoized_fibonacci(n - 1)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def spell(x: Any) -> str:
        return "Unknow spell type"

    @spell.register
    def _(x: int) -> str:
        return f"Damage spell: {x} damage"

    @spell.register
    def _(x: str) -> str:
        return f"Enchantment: {x}"

    @spell.register
    def _(x: list[Any]) -> str:
        return f"Multi-cast {len(x)} spells"

    return spell


def spell(power: int, element: str, target: str) -> str:
    return f"{element} spell deals {power} damages to {target} !"


if (__name__ == "__main__"):
    fire_spell = partial_enchanter(spell)["fire"]
    ice_spell = partial_enchanter(spell)["ice"]
    wind_spell = partial_enchanter(spell)["wind"]
    dispatcher = spell_dispatcher()

    print("== Spell Reducer ==")
    print(f"Sum: {spell_reducer([10, 20, 30, 40], 'add')}")
    print(f"Product: {spell_reducer([10, 20, 30, 40], 'multiply')}")
    print(f"Max: {spell_reducer([10, 20, 30, 40], 'max')}")

    print("\n== Partial_enchanter ==")
    print(fire_spell("Dragon"))
    print(ice_spell("Goblin"))
    print(wind_spell("Orc"))

    print("\n== Memoized fibonacci ==")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(20): {memoized_fibonacci(15)}")

    print("\n== Spell dispatcher ==")
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher([spell, spell, spell]))
    print(dispatcher((spell, spell)))
