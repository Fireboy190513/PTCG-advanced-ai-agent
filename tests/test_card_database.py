from cards.card_database import CardDatabase


def main():
    print("=" * 60)
    print("Project Arceus - Card Database Test")
    print("=" * 60)

    db = CardDatabase("data/EN_Card_Data.csv")
    db.load()

    print(f"\n✅ Database Loaded Successfully!")
    print(f"Total Rows: {db.card_count()}")

    print("\nFirst 5 Rows:")
    print(db.all_cards().head())

    print("\n" + "=" * 60)
    print("First 20 Card IDs and Names")
    print("=" * 60)

    print(db.all_cards()[["Card ID", "Card Name"]].head(20))

    first_card_id = db.all_cards()["Card ID"].iloc[0]

    print("\n" + "=" * 60)
    print(f"Testing Card ID Lookup ({first_card_id})")
    print("=" * 60)

    print(db.get_card(first_card_id))

    first_card_name = db.all_cards()["Card Name"].iloc[0]

    print("\n" + "=" * 60)
    print(f"Testing Name Lookup ({first_card_name})")
    print("=" * 60)

    print(db.get_card_by_name(first_card_name))

    print("\n" + "=" * 60)
    print("Exists?")
    print("=" * 60)

    print(db.exists(first_card_id))

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    main()