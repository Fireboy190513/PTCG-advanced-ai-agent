from pathlib import Path
import pandas as pd


class CardDatabase:
    """
    Loads and provides fast access to the Pokémon card database.
    """

    def __init__(self, csv_path: str):
        self.csv_path = Path(csv_path)
        self.df = None
        self.cards_by_id = {}
        self.cards_by_name = {}

    def load(self):
        """Load the card database and build lookup indexes."""
        self.df = pd.read_csv(self.csv_path)

        # Fast lookup by Card ID
        self.cards_by_id = {
            card_id: group
            for card_id, group in self.df.groupby("Card ID")
        }

        # Fast lookup by Card Name
        self.cards_by_name = {
            name: group
            for name, group in self.df.groupby("Card Name")
        }

    def card_count(self) -> int:
        """Return total number of rows."""
        return len(self.df)

    def all_cards(self):
        """Return the full dataframe."""
        return self.df

    def get_card(self, card_id):
        """Return all rows for a given Card ID."""
        return self.cards_by_id.get(card_id)

    def get_card_by_name(self, name):
        """Return all rows for a given Card Name."""
        return self.cards_by_name.get(name)

    def exists(self, card_id) -> bool:
        """Check whether a card exists."""
        return card_id in self.cards_by_id