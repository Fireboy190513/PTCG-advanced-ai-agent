"""
card_models.py

Data models used throughout Project Arceus.

These classes represent cards after they have been parsed from the CSV.
The rest of the AI should work with these objects instead of directly
reading pandas DataFrames.
"""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Attack:
    """
    Represents one attack on a Pokémon.
    """

    name: str
    cost: Optional[str] = None
    damage: Optional[str] = None
    effect: Optional[str] = None


@dataclass
class Card:
    """
    Generic Pokémon TCG card.
    """

    card_id: int
    name: str
    category: str

    expansion: Optional[str] = None
    collection_number: Optional[str] = None


@dataclass
class PokemonCard(Card):
    """
    Represents a Pokémon card.
    """

    hp: Optional[int] = None

    pokemon_type: Optional[str] = None

    stage: Optional[str] = None

    previous_stage: Optional[str] = None

    weakness: Optional[str] = None

    resistance: Optional[str] = None

    retreat_cost: Optional[str] = None

    attacks: List[Attack] = field(default_factory=list)


@dataclass
class EnergyCard(Card):
    """
    Represents an Energy card.
    """

    energy_type: Optional[str] = None


@dataclass
class TrainerCard(Card):
    """
    Represents a Trainer card.
    """

    rule: Optional[str] = None