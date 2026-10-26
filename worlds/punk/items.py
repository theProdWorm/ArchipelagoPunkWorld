from BaseClasses import Item, ItemClassification
from typing import NamedTuple, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from . import PunkWorld

class PunkItem(Item):
    game: str = "PUNK"

class PunkItemData(NamedTuple):
    category: str
    id: int
    item_type: ItemClassification
    weight: Optional[int]

module_table: dict[str, PunkItemData] = {
    "Common Ship Module": PunkItemData("Module", 101, ItemClassification.progression, 24),
    "Common Weapon Module": PunkItemData("Module", 102, ItemClassification.progression, 24),
    "Good Weapon Module": PunkItemData("Module", 103, ItemClassification.progression, 8),
    "Resource Module": PunkItemData("Module", 104, ItemClassification.progression, 16),
    "On-hit Module": PunkItemData("Module", 105, ItemClassification.progression, 8),
    "Basic Regen Module": PunkItemData("Module", 106, ItemClassification.progression, 6),
    "Stamina Regen Module": PunkItemData("Module", 107, ItemClassification.progression, 4)
}
currency_table: dict[str, PunkItemData] = {
    "Powerstar": PunkItemData("Currency", 201, ItemClassification.useful, 24),
    "Fiber": PunkItemData("Currency", 202, ItemClassification.useful, 32),
    "Gland": PunkItemData("Currency", 203, ItemClassification.useful, 24),
    "Chip": PunkItemData("Currency", 204, ItemClassification.useful, 12),
    "Generator": PunkItemData("Currency", 205, ItemClassification.useful, 8),
}
filler_table: dict[str, PunkItemData] = {
    "Health": PunkItemData("Filler", 301, ItemClassification.filler, 16),
    "Fuel": PunkItemData("Filler", 302, ItemClassification.filler, 16),
    "1000 Gold": PunkItemData("Filler", 303, ItemClassification.filler, 32),
    "Gel": PunkItemData("Filler", 304, ItemClassification.filler, 8),
    "Caps": PunkItemData("Filler", 305, ItemClassification.filler, 8),
    "Tech": PunkItemData("Filler", 306, ItemClassification.filler, 4),
    "Consumable": PunkItemData("Filler", 307, ItemClassification.filler, 8)
}
boss_table: dict[str, PunkItemData] = {
    "Completed Small Encounter": PunkItemData("Boss", 401, ItemClassification.progression, None),
    "Completed Advanced Encounter": PunkItemData("Boss", 402, ItemClassification.progression, None),
    "Completed Final Boss": PunkItemData("Boss", 403, ItemClassification.progression, None)
}

item_table = {**module_table, **currency_table, **filler_table, **boss_table}