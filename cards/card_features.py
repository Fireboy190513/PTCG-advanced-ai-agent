from cards.card_database import CardDatabase


class CardFeatures:
    """
    Extract useful information from Pokémon TCG cards.

    This class provides helper methods that the AI will use later
    for board evaluation, move selection, and search.
    """

    def __init__(self, database: CardDatabase):
        self.db = database

    def _get_first_row(self, card_id):
        """
        Return the first row corresponding to a card.
        """
        card = self.db.get_card(card_id)

        if card is None or card.empty:
            return None

        return card.iloc[0]

    # ==========================================================
    # Card Category
    # ==========================================================

    def get_category(self, card_id):
        row = self._get_first_row(card_id)

        if row is None:
            return None

        return row["Category"]

    def is_pokemon(self, card_id):
        return self.get_category(card_id) == "Pokémon"

    def is_energy(self, card_id):
        return self.get_category(card_id) == "Energy"

    def is_trainer(self, card_id):
        return self.get_category(card_id) == "Trainer"

    # ==========================================================
    # Basic Pokémon Information
    # ==========================================================

    def get_name(self, card_id):
        row = self._get_first_row(card_id)

        if row is None:
            return None

        return row["Card Name"]

    def get_hp(self, card_id):
        row = self._get_first_row(card_id)

        if row is None:
            return None

        return row["HP"]

    def get_type(self, card_id):
        row = self._get_first_row(card_id)

        if row is None:
            return None

        return row["Type"]

    def get_stage(self, card_id):
        row = self._get_first_row(card_id)

        if row is None:
            return None

        return row["Stage (Pokémon)/Type (Energy and Trainer)"]

    def get_previous_stage(self, card_id):
        row = self._get_first_row(card_id)

        if row is None:
            return None

        return row["Previous stage"]

    # ==========================================================
    # Battle Information
    # ==========================================================

    def get_weakness(self, card_id):
        row = self._get_first_row(card_id)

        if row is None:
            return None

        return row["Weakness"]

    def get_resistance(self, card_id):
        row = self._get_first_row(card_id)

        if row is None:
            return None

        return row["Resistance (Type)"]

    def get_retreat_cost(self, card_id):
        row = self._get_first_row(card_id)

        if row is None:
            return None

        return row["Retreat"]

    # ==========================================================
    # Attack Information
    # ==========================================================

    def get_attack_name(self, card_id):
        row = self._get_first_row(card_id)

        if row is None:
            return None

        return row["Move Name"]

    def get_attack_cost(self, card_id):
        row = self._get_first_row(card_id)

        if row is None:
            return None

        return row["Cost"]

    def get_attack_damage(self, card_id):
        row = self._get_first_row(card_id)

        if row is None:
            return None

        return row["Damage"]

    def get_attack_effect(self, card_id):
        row = self._get_first_row(card_id)

        if row is None:
            return None

        return row["Effect Explanation"]

    # ==========================================================
    # Utility
    # ==========================================================

    def get_card_summary(self, card_id):
        """
        Return the most useful information about a card
        as a dictionary.
        """

        row = self._get_first_row(card_id)

        if row is None:
            return None

        return {
            "Card ID": card_id,
            "Name": self.get_name(card_id),
            "Category": self.get_category(card_id),
            "HP": self.get_hp(card_id),
            "Type": self.get_type(card_id),
            "Stage": self.get_stage(card_id),
            "Previous Stage": self.get_previous_stage(card_id),
            "Weakness": self.get_weakness(card_id),
            "Resistance": self.get_resistance(card_id),
            "Retreat": self.get_retreat_cost(card_id),
            "Attack Name": self.get_attack_name(card_id),
            "Attack Cost": self.get_attack_cost(card_id),
            "Attack Damage": self.get_attack_damage(card_id),
            "Attack Effect": self.get_attack_effect(card_id),
        }