from collections.abc import Callable


def spell_combiner(spell1: Callable[[str, int], str],
                   spell2: Callable[[str, int], str])\
                   -> Callable[[str, int], tuple[str, str]]:
    def combine(target: str, power: int) -> tuple[str, str]:
        return ((spell1(target, power), spell2(target, power)))
    return (combine)


def power_amplifier(base_spell: Callable[[str, int], str],
                    multiplier: int) -> Callable[[str, int], str]:
    def amplifie(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplifie


def conditional_caster(condition: Callable[[str, int], bool],
                       spell: Callable[[str, int], str])\
                       -> Callable[[str, int], str]:
    def conditional_cast(target: str, power: int) -> str:
        if (condition(target, power)):
            return spell(target, power)
        return "Spell fizzled"
    return conditional_cast


def spell_sequence(spells: list[Callable[[str, int], str]])\
                   -> Callable[[str, int], list[str]]:
    def sequence(target: str, power: int) -> list[str]:
        result: list[str] = []
        for spell in spells:
            result.append(spell(target, power))
        return result
    return sequence


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball deals {power} damages to {target}"


if (__name__ == "__main__"):
    combined: Callable[[str, int], tuple[str, str]] =\
        spell_combiner(heal, fireball)
    amplified: Callable[[str, int], str] = power_amplifier(fireball, 3)
    conditioned: Callable[[str, int], str] =\
        conditional_caster(lambda target, power: power >= 60, heal)
    sequenced: Callable[[str, int], list[str]] =\
        spell_sequence([heal, fireball, fireball, heal])
    print("== Spell combiner==")
    print(combined("Dragon", 60))
    print("\n== Power amplifier ==")
    print(amplified("Dragon", 30))
    print("\n== Conditional caster ==")
    print(conditioned("Dragon", 70))
    print("\n== Spell sequence ==")
    print(sequenced("Dragon", 20))
