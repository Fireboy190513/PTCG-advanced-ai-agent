from cards.card_database import CardDatabase

db = CardDatabase("data/EN_Card_Data.csv")
db.load()

print(db.all_cards().head())
print()
print(db.get_card_by_name("Pikachu"))