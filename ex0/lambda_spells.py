def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return (sorted(artifacts, key=lambda dic: dic["power"], reverse=True))


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return (list(filter(lambda spell: spell["power"] >= min_power, mages)))


def spell_transformer(spells: list[str]) -> list[str]:
    return (list(map(lambda spell: "* " + spell + " *", spells)))


def mage_stats(mages: list[dict]) -> dict:
    high: int = max(mages, key=lambda arr: arr["power"])["power"]
    low: int = min(mages, key=lambda arr: arr["power"])["power"]
    avg: float = round(sum(map(lambda mage: mage['power'], mages))
                       / len(mages), 2)

    return {
        'max_power': high,
        'min_power': low,
        'avg_power': avg
    }


if (__name__ == "__main__"):
    artifacts = [{'name': 'Shadow Blade', 'power': 79, 'type': 'relic'},
                 {'name': 'Lightning Rod', 'power': 77, 'type': 'weapon'},
                 {'name': 'Ice Wand', 'power': 63, 'type': 'focus'},
                 {'name': 'Fire Staff', 'power': 86, 'type': 'weapon'}]
    mages = [{'name': 'Kai', 'power': 96, 'element': 'light'},
             {'name': 'Alex', 'power': 69, 'element': 'lightning'},
             {'name': 'Ember', 'power': 93, 'element': 'water'},
             {'name': 'Casey', 'power': 93, 'element': 'wind'},
             {'name': 'Ember', 'power': 61, 'element': 'lightning'}]
    spells = ['fireball', 'meteor', 'blizzard', 'heal']

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    print(f"{sorted_artifacts[0]['name']} "
          f"({sorted_artifacts[0]['power']} power) "
          f"comes before {sorted_artifacts[1]['name']} "
          f"({sorted_artifacts[1]['power']} power)")
    print("\nTesting spell transformer...")
    transformed = spell_transformer(spells)
    print(f"({transformed})")
    print("\nTesting power filter...")
    strong_mages = power_filter(mages, 70)
    for mage in strong_mages:
        print(f"{mage['name']} ({mage['power']} power)")
    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(f"Max power: {stats['max_power']}")
    print(f"Min power: {stats['min_power']}")
    print(f"Average power: {stats['avg_power']}")
