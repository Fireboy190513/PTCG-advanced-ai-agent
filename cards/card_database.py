from pathlib import Path
import pandas as pd


class CardDatabase:
    """
    Loads and provides fast access to the Pokémon card database.
    """

    def __init__(self, csv_path: str):
        self.csv_path = Path(csv_path)
        self.df = None

    def load(self):
        """Load the CSV file."""
        self.df = pd.read_csv(self.csv_path)

    def all_cards(self):
        """Return the complete dataframe."""
        return self.df

    def get_card(self, card_id):
        """Return all rows belonging to a card."""
        return self.df[self.df["Card ID"] == card_id]

    def get_card_by_name(self, name):
        """Return all rows matching a card name."""
        return self.df[self.df["Card Name"] == name]