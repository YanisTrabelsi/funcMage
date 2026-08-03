from collections.abc import Callable

def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combine(target: str, power: int):
        return ((spell1(target, power), spell2(target, power)))
    return (combine)


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplifie(target: str, power: int):
        return base_spell(target, power * multiplier)
    return amplifie


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional_cast(target: str, power: int):
        if (condition(target, power)):
            return spell(target, power)
        return "Spell fizzled"
    return conditional_cast


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int):
        result: list[str] = []
        for spell in spells:
            result.append(spell(target, power))
        return result
    return sequence


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power:int) -> str:
    return f"Fireball deals {power} damages to {target}"


if (__name__ == "__main__"):
    combined: Callable = spell_combiner(heal, fireball)
    amplified: Callable = power_amplifier(fireball, 3)
    conditioned: Callable = conditional_caster(lambda target, power: power >= 60, heal)
    sequenced: Callable = spell_sequence([heal, fireball, fireball, heal])
    print("== Spell combiner==")
    print(combined("Dragon", 60))
    print("\n== Power amplifier ==")
    print(amplified("Dragon", 30))
    print("\n== Conditional caster ==")
    print(conditioned("Dragon", 70))
    print("\n== Spell sequence ==")
    print(sequenced("Dragon", 20))
