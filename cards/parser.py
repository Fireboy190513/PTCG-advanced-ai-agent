"""
parser.py

Converts rows from the Pokémon card database into structured Python objects.

Project Arceus
"""

import pandas as pd

from cards.card_models import (
    Attack,
    PokemonCard,
    EnergyCard,
    TrainerCard,
)


class CardParser:
    """
    Parses rows from the card database into Python objects.
    """

    def __init__(self):
        pass

    @staticmethod
    def _safe_value(value):
        """
        Convert pandas NaN into None.
        """
        if pd.isna(value):
            return None
        return value

    def parse(self, rows: pd.DataFrame):
        """
        Parse all rows belonging to one Card ID.

        Parameters
        ----------
        rows : pandas.DataFrame

        Returns
        -------
        PokemonCard | EnergyCard | TrainerCard
        """

        if rows.empty:
            return None

        first = rows.iloc[0]

        card_id = int(first["Card ID"])
        name = self._safe_value(first["Card Name"])
        expansion = self._safe_value(first["Expansion"])
        collection_number = self._safe_value(first["Collection No."])
        stage = self._safe_value(
            first["Stage (Pokémon)/Type (Energy and Trainer)"]
        )
        hp = self._safe_value(first["HP"])

        # ---------------------------------------------------
        # Determine card type
        # ---------------------------------------------------

        if hp is not None:
            card = PokemonCard(
                card_id=card_id,
                name=name,
                category="Pokemon",
                expansion=expansion,
                collection_number=collection_number,
                hp=int(hp),
                pokemon_type=self._safe_value(first["Type"]),
                stage=stage,
                previous_stage=self._safe_value(first["Previous stage"]),
                weakness=self._safe_value(first["Weakness"]),
                resistance=self._safe_value(first["Resistance (Type)"]),
                retreat_cost=self._safe_value(first["Retreat"]),
            )

            # Parse every attack
            for _, row in rows.iterrows():

                attack_name = self._safe_value(row["Move Name"])

                if attack_name is None:
                    continue

                attack = Attack(
                    name=attack_name,
                    cost=self._safe_value(row["Cost"]),
                    damage=self._safe_value(row["Damage"]),
                    effect=self._safe_value(
                        row["Effect Explanation"]
                    ),
                )

                card.attacks.append(attack)

            return card

        elif stage is not None and "Energy" in str(stage):

            return EnergyCard(
                card_id=card_id,
                name=name,
                category="Energy",
                expansion=expansion,
                collection_number=collection_number,
                energy_type=self._safe_value(first["Type"]),
            )

        else:

            return TrainerCard(
                card_id=card_id,
                name=name,
                category="Trainer",
                expansion=expansion,
                collection_number=collection_number,
                rule=self._safe_value(first["Rule"]),
            )