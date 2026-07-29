from cards.card_database import CardDatabase


def main():
    db = CardDatabase("data/EN_Card_Data.csv")
    db.load()

    print("=" * 60)
    print("Project Arceus - Card Database Test")
    print("=" * 60)

    print(f"Rows         : {db.card_count()}")
    print(f"Unique Cards : {db.unique_card_count()}")

    print()

    test_card = db.get_card_object(26)

    print("Card Object")
    print("-" * 60)

    print("Name :", test_card.name)
    print("HP   :", test_card.hp)
    print("Type :", test_card.pokemon_type)

    print()

    print("Attacks")
    print("-" * 60)

    if not test_card.attacks:
        print("No attacks")

    for attack in test_card.attacks:
        print(f"- {attack.name}")
        print(f"  Cost   : {attack.cost}")
        print(f"  Damage : {attack.damage}")
        print(f"  Effect : {attack.effect}")
        print()

    print("✅ Test Passed")


if __name__ == "__main__":
    main()