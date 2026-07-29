from cards.card_database import CardDatabase


def main():
    db = CardDatabase("data/EN_Card_Data.csv")
    db.load()

    print("=" * 80)
    print("First 50 Cards")
    print("=" * 80)

    print(
        db.all_cards()[
            [
                "Card ID",
                "Card Name",
                "Stage (Pokémon)/Type (Energy and Trainer)",
                "Category",
                "HP",
                "Type",
            ]
        ].head(50)
    )


if __name__ == "__main__":
    main()