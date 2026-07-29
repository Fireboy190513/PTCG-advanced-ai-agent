from pathlib import Path

import pandas as pd

from cards.parser import CardParser


class CardDatabase:
    """
    Loads and provides fast access to the Pokémon card database.
    """

    def __init__(self, csv_path: str):
        self.csv_path = Path(csv_path)

        self.df = None

        self.cards_by_id = {}
        self.cards_by_name = {}

        # New parser
        self.parser = CardParser()

        # Cache parsed objects
        self.card_objects = {}

    def load(self):
        """
        Load the CSV and build lookup indexes.
        """

        self.df = pd.read_csv(self.csv_path)

        self.cards_by_id = {
            card_id: group
            for card_id, group in self.df.groupby("Card ID")
        }

        self.cards_by_name = {
            name: group
            for name, group in self.df.groupby("Card Name")
        }

    def card_count(self) -> int:
        """
        Total rows in CSV.
        """
        return len(self.df)

    def unique_card_count(self) -> int:
        """
        Number of unique cards.
        """
        return len(self.cards_by_id)

    def all_cards(self):
        """
        Return the full dataframe.
        """
        return self.df

    def get_card(self, card_id):
        """
        Return dataframe rows for a Card ID.
        """
        return self.cards_by_id.get(card_id)

    def get_card_by_name(self, name):
        """
        Return dataframe rows for a Card Name.
        """
        return self.cards_by_name.get(name)

    def exists(self, card_id) -> bool:
        """
        Check if card exists.
        """
        return card_id in self.cards_by_id

    def get_card_object(self, card_id):
        """
        Return a parsed Python object.

        Results are cached after the first parse.
        """

        if card_id in self.card_objects:
            return self.card_objects[card_id]

        rows = self.get_card(card_id)

        if rows is None:
            return None

        obj = self.parser.parse(rows)

        self.card_objects[card_id] = obj

        return obj

    def clear_cache(self):
        """
        Clear parsed object cache.
        """
        self.card_objects.clear()