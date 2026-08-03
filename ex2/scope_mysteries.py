from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable[[], int]:
    x: int = 0

    def count() -> int:
        nonlocal x
        x += 1
        return x
    return count


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    def accumulate(power: int) -> int:
        nonlocal initial_power
        initial_power += power
        return initial_power
    return accumulate


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchant


def memory_vault() -> dict[str, Callable]:
    data: dict[str, Any] = {}

    def store(k: str, v: Any) -> None:
        data[k] = v

    def recall(k: str) -> Any:
        if (k in list(data.keys())):
            return data[k]
        else:
            return "Memory not found"

    return {'store': store,
            'recall': recall}


if (__name__ == "__main__"):
    counter: Callable[[], int] = mage_counter()
    accumulator: Callable[[int], int] = spell_accumulator(10)
    flame_enchanter: Callable[[str], str] = enchantment_factory("Flaming")
    memory: dict[str, Callable] = memory_vault()
    memory["store"]("hello", "Hello L-A")

    print("== Mage counter ==")
    print(f"call 1: {counter()}")
    print(f"call 2: {counter()}")
    print(f"call 3: {counter()}")

    print("\n== Spell accumulator")
    print(f"base value: {accumulator(0)}")
    print(f"       +42: {accumulator(42)}")
    print(f"       +48: {accumulator(48)}")

    print("\n== Enchantment_factory == ")
    print(flame_enchanter("sword"))

    print("\n== Memory vault ==")
    memory['store']("password", "myPassword")
    print("'password' stored")
    print("recall password: ", end="")
    print(memory["recall"]("password"))
    print("testing with unknow value: ", end="")
    print(memory["recall"]("unknow"))
