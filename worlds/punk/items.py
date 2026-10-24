from BaseClasses import Item, ItemClassification
from typing import NamedTuple, Optional

class PunkItem(Item):
    game: str = "PUNK"

class PunkItemData(NamedTuple):
    category: str
    code: int
    item_type: ItemClassification
    weight: Optional[int]

module_table: dict[str, PunkItemData] = {
    "Common Ship Module": PunkItemData("Module", 101, ItemClassification.progression, 32),
    "Common Weapon Module": PunkItemData("Module", 102, ItemClassification.progression, 32),
    "Good Weapon Module": PunkItemData("Module", 103, ItemClassification.progression, 8),
    "Resource Module": PunkItemData("Module", 104, ItemClassification.progression, 16),
    "On-hit Module": PunkItemData("Module", 105, ItemClassification.progression, 8),
    "Basic Regen Module": PunkItemData("Module", 106, ItemClassification.progression, 4),
    "Stamina Regen Module": PunkItemData("Module", 107, ItemClassification.progression, 1)
}
currency_table: dict[str, PunkItemData] = {
    "Powerstar": PunkItemData("Currency", 201, ItemClassification.useful, 4),
    "Fiber": PunkItemData("Currency", 202, ItemClassification.useful, 8),
    "Gland": PunkItemData("Currency", 203, ItemClassification.useful, 6),
    "Chip": PunkItemData("Currency", 204, ItemClassification.useful, 2),
    "Generator": PunkItemData("Currency", 205, ItemClassification.useful, 1),
}
filler_table: dict[str, PunkItemData] = {
    "Health": PunkItemData("Filler", 301, ItemClassification.filler, 4),
    "Fuel": PunkItemData("Filler", 302, ItemClassification.filler, 4),
    "1000 Gold": PunkItemData("Filler", 303, ItemClassification.filler, 8),
    "Gel": PunkItemData("Filler", 304, ItemClassification.filler, 2),
    "Caps": PunkItemData("Filler", 305, ItemClassification.filler, 2),
    "Tech": PunkItemData("Filler", 306, ItemClassification.filler, 1),
    "Consumable": PunkItemData("Filler", 307, ItemClassification.filler, 2)
}

item_table = {**module_table, **currency_table, **filler_table}